# Standart libraries
import json

# Third party packages
import allure
import pytest
import pytest_check as check
from jsonschema import validate
from pydantic import ValidationError

# My packages
from pytest_DataCenter_functional.test_REST_API.tools import schema_models
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import DcApiWithToken

url_tail = "/api/v2/data_center/user_cards/contacts/phones?userID=5"


@allure.epic("DataService API v2 (user_cards)")
@allure.feature("Phones list for REST_test_user_admin")
@pytest.mark.testRESTAPI
@allure.story("Список телефонов по пользователю REST_test_user_admin")
class TestPhonesListForUser:
    @allure.title("Успешность запроса")
    def test_status_code_200(self, dc_api: DcApiWithToken):
        r = dc_api.req_get(url_tail)
        assert r.status_code == 200

    @allure.title("Headers 'content-type'")
    def test_content_type(self, dc_api: DcApiWithToken):
        con_type = dc_api.req_get(url_tail).headers["content-type"]
        assert con_type == r"application/json; charset=utf-8"

    @allure.title("Время ответа запроса")
    def test_response_time(self, dc_api: DcApiWithToken):
        resp_time = dc_api.req_get(url_tail).elapsed.total_seconds()
        assert resp_time <= 30

    @allure.title("Телефонный номер 1")
    def test_phone_number_1(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Идентификатор документа в индексе"):
            check.equal(
                data_dict["data"][0]["docID"], "01279DC6-381E-4F6A-9E86-60AEA3514067"
            )
        with allure.step("Отображать в шапке"):
            check.is_none(data_dict["data"][0]["inHeader"])
        with allure.step("Идентификатор телефона"):
            check.equal(data_dict["data"][0]["phoneID"], 3)
        with allure.step("Номер телефона"):
            check.equal(data_dict["data"][0]["phoneNumber"], "+34234234234234")
        with allure.step("Тип номера телефона"):
            check.equal(data_dict["data"][0]["phoneType"], 1)
        with allure.step("UDL документа"):
            check.equal(
                data_dict["data"][0]["signID"], "01279DC6-381E-4F6A-9E86-60AEA3514067"
            )

    @allure.title("Телефонный номер 2")
    def test_phone_number_2(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Идентификатор документа в индексе"):
            check.is_none(data_dict["data"][1]["docID"])
        with allure.step("Отображать в шапке"):
            check.is_none(data_dict["data"][1]["inHeader"])
        with allure.step("Идентификатор телефона"):
            check.equal(data_dict["data"][1]["phoneID"], 2)
        with allure.step("Номер телефона"):
            check.equal(data_dict["data"][1]["phoneNumber"], "+345345345345553")
        with allure.step("Тип номера телефона"):
            check.equal(data_dict["data"][1]["phoneType"], 1)
        with allure.step("UDL документа"):
            check.is_none(data_dict["data"][1]["signID"])

    @allure.title("Телефонный номер 3")
    def test_phone_number_3(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Идентификатор документа в индексе"):
            check.is_none(data_dict["data"][2]["docID"])
        with allure.step("Отображать в шапке"):
            check.is_true(data_dict["data"][2]["inHeader"])
        with allure.step("Идентификатор телефона"):
            check.equal(data_dict["data"][2]["phoneID"], 1)
        with allure.step("Номер телефона"):
            check.equal(data_dict["data"][2]["phoneNumber"], "+435345234523452345")
        with allure.step("Тип номера телефона"):
            check.equal(data_dict["data"][2]["phoneType"], 2)
        with allure.step("UDL документа"):
            check.is_none(data_dict["data"][2]["signID"])

    @allure.title("Телефонный номер 4 cellphone")
    def test_phone_number_4_cellphone(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Идентификатор документа в индексе"):
            check.equal(
                data_dict["data"][3]["docID"], "01279DC6-381E-4F6A-9E86-60AEA3514067"
            )
        with allure.step("Отображать в шапке"):
            check.is_none(data_dict["data"][3]["inHeader"])
        with allure.step("Идентификатор телефона"):
            check.equal(data_dict["data"][3]["phoneID"], 4)
        with allure.step("Номер телефона"):
            check.equal(data_dict["data"][3]["phoneNumber"], "cellphone")
        with allure.step("Тип номера телефона"):
            check.equal(data_dict["data"][3]["phoneType"], 1)
        with allure.step("UDL документа"):
            check.equal(
                data_dict["data"][3]["signID"], "01279DC6-381E-4F6A-9E86-60AEA3514067"
            )

    @allure.title("Телефонный номер 5 home")
    def test_phone_number_5_home(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Идентификатор документа в индексе"):
            check.equal(
                data_dict["data"][4]["docID"], "01279DC6-381E-4F6A-9E86-60AEA3514067"
            )
        with allure.step("Отображать в шапке"):
            check.is_none(data_dict["data"][4]["inHeader"])
        with allure.step("Идентификатор телефона"):
            check.equal(data_dict["data"][4]["phoneID"], 5)
        with allure.step("Номер телефона"):
            check.equal(data_dict["data"][4]["phoneNumber"], "home")
        with allure.step("Тип номера телефона"):
            check.equal(data_dict["data"][4]["phoneType"], 1)
        with allure.step("UDL документа"):
            check.equal(
                data_dict["data"][4]["signID"], "01279DC6-381E-4F6A-9E86-60AEA3514067"
            )

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self, dc_api: DcApiWithToken):
        schema = {
            "type": "object",
            "properties": {"data": {"type": "array"}},
            "required": ["data"],
        }
        resp = dc_api.req_get(url_tail).json()
        validate(resp, schema=schema)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema2(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        error_list = []
        for row in data_dict["data"]:
            try:
                schema_models.SchemaModelsDataServiceAPIv2.PhonesListForUser.parse_obj(
                    row
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.PhonesListForUser.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
