# Standart libraries
import json

# Third party packages
import allure
import pytest
from jsonschema import validate

# My packages
from pytest_DataCenter_functional.test_REST_API.tools import schema_models
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import DcApiWithToken

url_tail = "/api/v2/data_center/user_cards/user_resume?userID=1"


@allure.epic("DataService API v2 (user_cards)")
@allure.feature("Resume for user REST_test_user_cyrillic")
@pytest.mark.testRESTAPI
@allure.story("Резюме пользователя REST_test_user_cyrillic")
class TestResumeForUser:
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

    @allure.title("Данные резюме пользователя REST_test_user_cyrillic")
    def test_resume_REST_test_user_admin(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        assert (
            data_dict["data"][0]["jsonData"]
            == '{"keySkills":{"languageLevel":[{"name":"Русский","level":"l1"}],"professionalSkills":"","drivingExperience":"","skills":[{"skill":"UC.summary.professionalSkills","description":"Те '
            "самые профессиональные "
            'навыки"}]},"education":[{"level":"doctor","year":"2020","name":"То самое '
            'заведение","faculty":"Тот самый факультет","specialty":"Та самая '
            'специальность"}],"courses":[{"year":"2021","month":10,"name":"Тот самый '
            'курс","place":"То самое '
            'место"}],"experience":[{"start":1598832000,"end":1661212800,"workTime":"( 2 '
            'года 24 дня )","company":"Та самая компания","companyUrl":"Тот самый '
            'сайт","city":"Тот самый город","position":"Та самая '
            'должность","description":"То самое '
            'описание"}],"ageAndConditions":{"birthDate":1280793600,"age":"(12 '
            'года)","salary":"Та самая ЗП '
            '50000","busyness":"volunteer","schedules":"shift","coditions":null,"conditions":"remotely"},"adress":{"country":"Та '
            'самая страна","city":"Тот самый город","street":"Та самая '
            'улица","house":"Тот самый дом 33","building":"Тот самый корпус '
            '2","apartment":"Та самая квартира 154","zipCode":"Тот самый почтовый индекс '
            '509826","citizenship":"То самое '
            'гражданство","maritalStatus":3,"childrensCount":"То самое кол-во детей '
            '22","relocateReadiness":"relocation_desirable","businessTripReadiness":"never"},"additionalInfo":"Та '
            'самая дополнительная информация"}'
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
        schema_models.SchemaModelsDataServiceAPIv2.ResumeForUser.parse_obj(data_dict)
