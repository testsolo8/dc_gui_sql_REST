# Standart libraries
import json

# Third party packages
import pytest_check as check
import requests
from jsonschema import validate

# My packages
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import base_url_dc

path = (
    "https://"
    + base_url_dc()
    + ":9088/datacenter/api/v4/product/settings/?product_id=0&server_id=BEA25266-"
    "8417-42EC-BB9F-2C2398CE97D0&custom_id=91484937-80aa-4d90-857b-dbb71cf15500&name=config"
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


def test_datastore_connection_setting():
    data_dict = r.json()
    data_str = json.dumps(data_dict)
    parsed_data = json.loads(data_str)
    check.equal(parsed_data[0]["product_id"], 0)
    check.equal(parsed_data[0]["server_id"], "bea25266-8417-42ec-bb9f-2c2398ce97d0")
    check.equal(parsed_data[0]["name"], "config")
    check.equal(parsed_data[0]["custom_id"], "91484937-80aa-4d90-857b-dbb71cf15500")
    check.equal(parsed_data[0]["value_id"], "6965b1d2-78af-4559-8aca-3e1f7c212ae2")
    check.equal(
        parsed_data[0]["value"],
        "eyJzeW5jLWZyb20iOjYsImF0dHJpYnV0ZS1kYi1wYXJhbSI6IlRnQWdBQklBQUFBSUFEZ0FCZ0"
        "I3QURNQVFRQTJBRFlBUWdBeEFEY0FPQUF0QURFQVFnQTBBRUVBTFFBMEFHRUFPQUF3QUMwQU9B"
        "QXdBRVlBTVFBdEFEa0FOd0F5QUVVQU13QTFBRUVBTUFBNEFEWUFOQUExQUgwQUFBQkVBR2tBWn"
        "dCbEFITUFkQUJCQUhRQWRBQnlBR2tBWWdCMUFIUUFaUUFBQUZRQVFRQkxBRVVBTFFCVEFGRUFU"
        "QUFBQUc0QWN3QmhBQUFBQVFBMkFEZ0FPUUJCQUVNQU1RQXdBRGdBTWdBeUFFUUFPQUJHQURnQV"
        "JRQkVBRUVBTVFCQ0FEa0FOd0ExQURBQVFRQTNBRGtBQUFCT0FHOEFBQUE9IiwibG9nLWxldmVs"
        "IjoidHJhY2UiLCJlbmFibGVkIjoidHJ1ZSJ9",
    )
    check.equal(parsed_data[0]["timestamp"], 1656073941)


def test_schema():
    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "product_id": {"type": "number"},
                "server_id": {"type": "string"},
                "name": {"type": "string"},
                "custom_id": {"type": "string"},
                "value_id": {"type": "string"},
                "value": {"type": "string"},
                "timestamp": {"type": "number"},
            },
            "required": ["product_id", "server_id", "custom_id", "value_id"],
        },
    }
    resp = r.json()
    validate(resp, schema=schema)
