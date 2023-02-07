# Standart libraries
import json

# Third party packages
import requests
from jsonschema import validate

# My packages
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import base_url_dc

path = (
    "https://"
    + base_url_dc()
    + ":9082/datacenter/api/v3/license/statuses?LicenseID=7848DC5B-7EFD-4ED2-8116-5CC43664CC4F&StatusID=4"
)
r = requests.get(path, verify=False)


def test_status_code_200():
    assert r.status_code == 200


def test_content_type():
    con_type = r.headers["content-type"]
    assert con_type == "application/json; charset=utf-8"


def test_response_time():
    resp_time = r.elapsed.total_seconds()
    assert resp_time <= 30


def test_checking_no_revoked_Skype_licenses():
    data_dict = r.json()
    data_str = json.dumps(data_dict)
    parsed_data = json.loads(data_str)
    assert parsed_data is None
