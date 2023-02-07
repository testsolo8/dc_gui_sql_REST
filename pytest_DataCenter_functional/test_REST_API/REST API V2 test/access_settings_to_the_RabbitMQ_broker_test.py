# Standart libraries
import json

# Third party packages
import allure
import pytest
import pytest_check as check
import requests
from jsonschema import validate

# My packages
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import base_url_dc

path = "http://" + base_url_dc() + ":9096/api/v2/settings/RabbitMQ"
r = requests.get(path, verify=False)


@allure.epic("REST API V2")
@allure.feature("Access settings to the RabbitMQ broker")
@pytest.mark.testRESTAPI
@allure.story("Получение настроек доступа к брокеру RabbitMQ")
class TestAccessSettingsToRabbitMQBroker:
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
    def test_port_connection(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        check.equal(parsed_data["WEBUIPort"], "9076")
        check.equal(parsed_data["AMQPPort"], "9075")
        check.equal(parsed_data["STOMPPort"], "9077")

    @pytest.mark.skip(reason="в текущей реализации среды для тестов не реализовано")
    def test_connection(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        check.equal(
            parsed_data["Pwd"],
            "AQBEAEUARABBADcANQA2AEIAOQA1AEMAOABFADkAQgBEADIANAA1AEIAMgA1AEQAOAA5ADkANgBDAEIANQAz"
            "AEMANwAyAEYARgAxAEYAMgBEAEIAMgA3AEMAMQA1ADIARQA5ADkAQwBEAEMANQA0AEIANQA1ADkARgA4AEUAQ"
            "QBEADYANQAzAEIAMAAyAEUAOAA",
        )
        check.equal(parsed_data["VHost"], "DataCenter")
        check.equal(parsed_data["User"], "SearchinformUser")
        check.equal(parsed_data["Host"], "DC-RC.minsk.searchinform.net")

    @pytest.mark.skip(reason="в текущей реализации среды для тестов не реализовано")
    def test_schema(self):
        schema = {
            "type": "object",
            "required": [
                "Pwd",
                "WEBUIPort",
                "AMQPPort",
                "STOMPPort",
                "VHost",
                "User",
                "Host",
            ],
        }
        resp = r.json()
        validate(resp, schema=schema)
