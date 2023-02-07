# Standart libraries
import json

# Third party packages
import allure
import pytest
from jsonschema import validate

# My packages
from pytest_DataCenter_functional.test_REST_API.tools import schema_models
from pytest_DataCenter_functional.test_REST_API.tools.dc_base_url import DcApiWithToken

url_tail = "/api/v2/data_center/user_cards/user_resume?userID=5"


@allure.epic("DataService API v2 (user_cards)")
@allure.feature("Resume for user REST_test_user_admin")
@pytest.mark.testRESTAPI
@allure.story("Резюме пользователя REST_test_user_admin")
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

    @allure.title("Данные резюме пользователя REST_test_user_admin")
    def test_resume_REST_test_user_admin(self, dc_api: DcApiWithToken):
        data_dict = dc_api.req_get(url_tail).json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        assert (
            parsed_data["data"][0]["jsonData"]
            == '{"keySkills":{"languageLevel":[{"name":"English","level":"b1"}],"professionalSkills":"","drivingExperience":"","skills":[{"skill":"UC.summary.professionalSkills","description":"Those '
            "same professional "
            'skills"}]},"education":[{"level":"higher","year":"2020","name":"Those same '
            'professional skills","faculty":"The same faculty","specialty":"Same '
            'specialty"}],"courses":[{"year":"2021","month":8,"name":"That same '
            'course","place":"That same '
            'place"}],"experience":[{"start":1661126400,"end":1661299200,"workTime":"( 2 '
            'дня )","company":"The same company","companyUrl":"The very '
            'site","city":"That very city","position":"The same '
            'position","description":"The same '
            'description"}],"ageAndConditions":{"birthDate":966988800,"age":"(22 '
            'года)","salary":"The same RFP '
            '2000","busyness":"full","schedules":"fullDay","coditions":null,"conditions":"office"},"adress":{"country":"The '
            'same country","city":"That very city","street":"The same '
            'street","house":"Same house 5","building":"The same building '
            '5","apartment":"The same flat 5","zipCode":"The same index '
            '555555","citizenship":"The same '
            'citizenship","maritalStatus":1,"childrensCount":"5","relocateReadiness":"relocation_possible","businessTripReadiness":"sometimes"},"additionalInfo":"The '
            'same additional information"}'
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
