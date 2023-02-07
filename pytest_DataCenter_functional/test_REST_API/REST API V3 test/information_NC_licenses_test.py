# Standart libraries
import datetime
import hashlib
import json

# Third party packages
import allure
import pytest
import pytest_check as check
import requests
from jsonschema import validate

# My packages
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import base_url_dc

today_time_str = datetime.date.today().strftime("%Y-%m-%d")
encode_to_byte = today_time_str.encode()
hash_md5 = hashlib.md5(encode_to_byte)
tomorrow_str = (
    str(datetime.date.today() + datetime.timedelta(days=1)) + "T00:00:00+03:00"
)

path = (
    "https://"
    + base_url_dc()
    + ":9082/datacenter/api/v3/license/info?SINonce="
    + hash_md5.hexdigest()
    + "&ComponentID=4"
)
r = requests.get(path, verify=False)


@allure.epic("REST API V3")
@allure.feature("Information NC licenses")
@pytest.mark.testRESTAPI
@allure.story("Информация по лицензиям NetworkController")
class TestInformationNCLicenses:
    @allure.title("Успешность запроса")
    def test_status_code_200(self):
        assert r.status_code == 200

    @allure.title("Headers 'content-type'")
    def test_content_type(self):
        con_type = r.headers["content-type"]
        assert con_type == "application/json; charset=utf-8"

    @allure.title("Время ответа запроса")
    def test_response_time(self):
        resp_time = r.elapsed.total_seconds()
        assert resp_time <= 30

    @pytest.mark.skip(reason="в текущей реализации среды для тестов не реализовано")
    def test_count_component_license(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        assert len(parsed_data["88033CCD-6360-41F0-98CA-BDDB08532119"]["Licenses"]) == 6

    @pytest.mark.skip(reason="в текущей реализации среды для тестов не реализовано")
    def test_information_about_NC_license(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        check.equal(
            parsed_data["88033CCD-6360-41F0-98CA-BDDB08532119"]["Date"], tomorrow_str
        )
        check.equal(parsed_data["88033CCD-6360-41F0-98CA-BDDB08532119"]["Mode"], 2)
        check.greater_equal(
            parsed_data["88033CCD-6360-41F0-98CA-BDDB08532119"]["Expiration"], 1
        )
        check.equal(
            parsed_data["88033CCD-6360-41F0-98CA-BDDB08532119"]["SupportTo"],
            "2113-01-01T02:59:59+03:00",
        )

    @pytest.mark.skip(reason="в текущей реализации среды для тестов не реализовано")
    def test_information_about_mail_integration_license(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        check.equal(
            parsed_data["88033CCD-6360-41F0-98CA-BDDB08532119"]["Licenses"][
                "0047A5B7-8195-4A5F-BAEA-D01708EDE0C5"
            ]["StartDate"],
            "0001-01-01T00:00:00Z",
        )
        check.equal(
            parsed_data["88033CCD-6360-41F0-98CA-BDDB08532119"]["Licenses"][
                "0047A5B7-8195-4A5F-BAEA-D01708EDE0C5"
            ]["EndDate"],
            "2113-01-01T02:59:59+03:00",
        )
        check.equal(
            parsed_data["88033CCD-6360-41F0-98CA-BDDB08532119"]["Licenses"][
                "0047A5B7-8195-4A5F-BAEA-D01708EDE0C5"
            ]["ProductName"],
            "MailController (Integration)",
        )
        check.equal(
            parsed_data["88033CCD-6360-41F0-98CA-BDDB08532119"]["Licenses"][
                "0047A5B7-8195-4A5F-BAEA-D01708EDE0C5"
            ]["ProductID"],
            6,
        )
        check.equal(
            parsed_data["88033CCD-6360-41F0-98CA-BDDB08532119"]["Licenses"][
                "0047A5B7-8195-4A5F-BAEA-D01708EDE0C5"
            ]["Coefficient"],
            3,
        )
        check.greater(
            len(
                parsed_data["88033CCD-6360-41F0-98CA-BDDB08532119"]["Products"][
                    "0047A5B7-8195-4A5F-BAEA-D01708EDE0C5"
                ]
            ),
            0,
        )

    @pytest.mark.skip(reason="в текущей реализации среды для тестов не реализовано")
    def test_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "1D2AA87B-27C8-48C6-9631-0082CDBCA910": {"type": "object"},
                "88033CCD-6360-41F0-98CA-BDDB08532119": {"type": "object"},
                "AE2CC2A1-0350-4387-B297-07EC2EAFADB2": {
                    "type": "object",
                    "properties": {
                        "Date": {"type": "string"},
                        "Mode": {"type": "number"},
                        "Expiration": {"type": "number"},
                        "Licenses": {"type": "object"},
                        "Products": {"type": "object"},
                        "SupportTo": {"type": "string"},
                    },
                    "required": [
                        "Date",
                        "Mode",
                        "Expiration",
                        "Licenses",
                        "Products",
                        "SupportTo",
                    ],
                },
            },
            "required": [
                "1D2AA87B-27C8-48C6-9631-0082CDBCA910",
                "88033CCD-6360-41F0-98CA-BDDB08532119",
                "AE2CC2A1-0350-4387-B297-07EC2EAFADB2",
            ],
        }
        resp = r.json()
        validate(resp, schema=schema)
