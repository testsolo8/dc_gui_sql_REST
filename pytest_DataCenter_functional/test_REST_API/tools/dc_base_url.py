# Standart libraries
import configparser
import json
from pathlib import Path

# Third party packages
import requests
import urllib3

# My packages
from DataCenter.tools.get_project_root import get_project_root


def base_url_dc(url="localhost"):
    return url


urllib3.disable_warnings()

config_path = str(
    Path(get_project_root(), "pytest_DataCenter_functional", "test_REST_API")
)


class DcApiWithToken:
    def __init__(self, srv_addr=base_url_dc()):
        parser = configparser.ConfigParser()
        parser.read(config_path + "\config.ini")
        self.username = parser.get("login", "username")
        self.password = parser.get("login", "password")
        self.srv_addr = srv_addr
        self.auth()

    def auth(self):
        auth_server_url = f"https://{self.srv_addr}/api/v2/auth"
        client_id = self.username
        client_secret = self.password
        token_req_payload = {"grant_type": "client_credentials"}
        token_response = requests.post(
            auth_server_url,
            data=token_req_payload,
            verify=False,
            allow_redirects=False,
            auth=(client_id, client_secret),
        )
        self.token = json.loads(token_response.text)["access_token"]

    def req_get(self, url_tail):
        path = f"https://{self.srv_addr}{url_tail}"
        if self.token is None:
            self.auth()
        api_call_headers = {"Authorization": "Bearer " + self.token}
        return requests.get(path, headers=api_call_headers, verify=False)

    def req_post(self, url, body):
        path = f"https://{self.srv_addr}{url}"
        if self.token is None:
            self.auth()
        api_call_headers = {"Authorization": "Bearer " + self.token}
        return requests.post(
            url=path, json=body, headers=api_call_headers, verify=False
        )
