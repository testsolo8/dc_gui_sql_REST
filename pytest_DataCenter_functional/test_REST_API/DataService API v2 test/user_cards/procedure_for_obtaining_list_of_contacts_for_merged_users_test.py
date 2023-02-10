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

url_tail = "/api/v2/data_center/user_cards/users_concat?userIDList=1,7"


@allure.epic("DataService API v2 (user_cards)")
@allure.feature("Procedure for obtaining list of contacts for merged users")
@pytest.mark.testRESTAPI
@allure.story(
    "Процедура получения списка контактов по объединяемым пользователям REST_test_user_diff_param и REST_test_user_кириллик"
)
class TestProcedureForObtainingListContactsForMergedUsers:
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

    @allure.title("Контакт 1")
    def test_list_of_merged_contact_1(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Тип аккаунта - UC_AccountsType"):
            check.equal(data_dict["data"][0]["accountTypeID"], 1)
        with allure.step("Тип контакта: 3 Мессенджеры, 4 Соц.Сети"):
            check.equal(data_dict["data"][0]["contactTypeID"], 2)
        with allure.step("Имя контакта"):
            check.equal(
                data_dict["data"][0]["displayName"],
                "REST_test_user_кириллик@test.lan",
            )
        with allure.step("Идентификатор пользователя"):
            check.equal(data_dict["data"][0]["userID"], 1)

    @allure.title("Контакт 2")
    def test_list_of_merged_contact_2(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Тип аккаунта - UC_AccountsType"):
            check.equal(data_dict["data"][1]["accountTypeID"], 1)
        with allure.step("Тип контакта: 3 Мессенджеры, 4 Соц.Сети"):
            check.equal(data_dict["data"][1]["contactTypeID"], 2)
        with allure.step("Имя контакта"):
            check.equal(
                data_dict["data"][1]["displayName"],
                "REST_test_user_diff_param@test.lan",
            )
        with allure.step("Идентификатор пользователя"):
            check.equal(data_dict["data"][1]["userID"], 7)

    @allure.title("Контакт 3")
    def test_list_of_merged_contact_3(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Тип аккаунта - UC_AccountsType"):
            check.equal(data_dict["data"][2]["accountTypeID"], 13)
        with allure.step("Тип контакта: 3 Мессенджеры, 4 Соц.Сети"):
            check.equal(data_dict["data"][2]["contactTypeID"], 3)
        with allure.step("Имя контакта"):
            check.equal(
                data_dict["data"][2]["displayName"],
                "WhatsApp_REST_test_user_cyrillic",
            )
        with allure.step("Идентификатор пользователя"):
            check.equal(data_dict["data"][2]["userID"], 1)

    @allure.title("Контакт 4")
    def test_list_of_merged_contact_4(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Тип аккаунта - UC_AccountsType"):
            check.equal(data_dict["data"][3]["accountTypeID"], 5)
        with allure.step("Тип контакта: 3 Мессенджеры, 4 Соц.Сети"):
            check.equal(data_dict["data"][3]["contactTypeID"], 3)
        with allure.step("Имя контакта"):
            check.equal(
                data_dict["data"][3]["displayName"],
                "Mail.ru Agent_REST_test_user_cyrillic",
            )
        with allure.step("Идентификатор пользователя"):
            check.equal(data_dict["data"][3]["userID"], 1)

    @allure.title("Контакт 5")
    def test_list_of_merged_contact_5(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Тип аккаунта - UC_AccountsType"):
            check.equal(data_dict["data"][4]["accountTypeID"], 3)
        with allure.step("Тип контакта: 3 Мессенджеры, 4 Соц.Сети"):
            check.equal(data_dict["data"][4]["contactTypeID"], 3)
        with allure.step("Имя контакта"):
            check.equal(
                data_dict["data"][4]["displayName"], "Viber_REST_test_user_cyrillic"
            )
        with allure.step("Идентификатор пользователя"):
            check.equal(data_dict["data"][4]["userID"], 1)

    @allure.title("Контакт 6")
    def test_list_of_merged_contact_6(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Тип аккаунта - UC_AccountsType"):
            check.equal(data_dict["data"][5]["accountTypeID"], 7)
        with allure.step("Тип контакта: 3 Мессенджеры, 4 Соц.Сети"):
            check.equal(data_dict["data"][5]["contactTypeID"], 4)
        with allure.step("Имя контакта"):
            check.equal(
                data_dict["data"][5]["displayName"], "Mamba_REST_test_user_cyrillic"
            )
        with allure.step("Идентификатор пользователя"):
            check.equal(data_dict["data"][5]["userID"], 1)

    @allure.title("Контакт 7")
    def test_list_of_merged_contact_7(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Тип аккаунта - UC_AccountsType"):
            check.equal(data_dict["data"][6]["accountTypeID"], 5)
        with allure.step("Тип контакта: 3 Мессенджеры, 4 Соц.Сети"):
            check.equal(data_dict["data"][6]["contactTypeID"], 4)
        with allure.step("Имя контакта"):
            check.equal(
                data_dict["data"][6]["displayName"],
                "Linkedln_REST_test_user_cyrillic",
            )
        with allure.step("Идентификатор пользователя"):
            check.equal(data_dict["data"][6]["userID"], 1)

    @allure.title("Контакт 8")
    def test_list_of_merged_contact_8(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        with allure.step("Тип аккаунта - UC_AccountsType"):
            check.equal(data_dict["data"][7]["accountTypeID"], 3)
        with allure.step("Тип контакта: 3 Мессенджеры, 4 Соц.Сети"):
            check.equal(data_dict["data"][7]["contactTypeID"], 4)
        with allure.step("Имя контакта"):
            check.equal(
                data_dict["data"][7]["displayName"],
                "Facebook_REST_test_user_cyrillic",
            )
        with allure.step("Идентификатор пользователя"):
            check.equal(data_dict["data"][7]["userID"], 1)

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
                schema_models.SchemaModelsDataServiceAPIv2.ProcedureForObtainingListContactsForMergedUsers.parse_obj(
                    row
                )
            except ValidationError as e:
                error_list.append(f"Error found in object: {row}\n{e.json()}\n")
        try:
            schema_models.SchemaModelsDataServiceAPIv2.ProcedureForObtainingListContactsForMergedUsers.parse_obj(
                data_dict["data"][0]
            )
        except Exception as e:
            if error_list:
                raise Exception(f"{''.join(error_list)}\n{e}")
            else:
                raise Exception(e)
