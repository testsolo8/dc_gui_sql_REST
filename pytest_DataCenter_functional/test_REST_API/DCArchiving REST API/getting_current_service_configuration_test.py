# Standart libraries
import json
from typing import List

# Third party packages
import allure
import pytest
import pytest_check as check
import requests
from jsonschema import validate
from pydantic import ValidationError, parse_obj_as

# My packages
from pytest_DataCenter_functional.test_REST_API.tools import schema_models
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import base_url_dc

path = "https://" + base_url_dc() + ":9082/archiving/api/v1/config"
r = requests.get(path, verify=False)


@allure.epic("DCArchiving REST API")
@allure.feature("Getting current service configuration")
@pytest.mark.testRESTAPI
@allure.story("Получение текущей конфигурации сервиса")
class TestGettingCurrentServiceConfiguration:
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

    @allure.title("Получение текущей конфигурации сервиса архивирования")
    def test_service_configuration(self):
        data_dict = r.json()
        with allure.step("Хост почтового сервиса 'dcmailservice'"):
            check.equal(data_dict["MailServiceHost"], "localhost")
        with allure.step("Порт почтового сервиса 'dcmailservice'"):
            check.equal(data_dict["MailServicePort"], 9083)
        with allure.step("Количество одновременно выполняемых задач"):
            check.equal(data_dict["WorkerCount"], 4)
        with allure.step(
            "Количество секунд ожидания до успешного начала операции с удаленным файлом"
        ):
            check.equal(data_dict["RemoteOperationTimeout"], 10)
        with allure.step("DefaultDBAgentPort"):
            check.equal(data_dict["DefaultDBAgentPort"], 9085)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "object",
            "required": [
                "MailServiceHost",
                "MailServicePort",
                "WorkerCount",
                "RemoteOperationTimeout",
                "DefaultDBAgentPort",
            ],
        }
        resp = r.json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema2(self):
        data_dict = requests.get(path, verify=False).json()
        error_list = []
        for row in data_dict:
            try:
                parse_obj_as(
                    List[
                        schema_models.SchemaModelsDCArchivingRESTAPI.GettingCurrentServiceConfiguration
                    ],
                    data_dict,
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDCArchivingRESTAPI.GettingCurrentServiceConfiguration.parse_obj(
                data_dict
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
