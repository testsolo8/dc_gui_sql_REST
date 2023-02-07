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

path = "https://" + base_url_dc() + ":9088/datacenter/api/v2/attributes/prog"
body = {"protocolIds": ["fd165b6f-63ca-413d-a3c0-109a9906a491"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Individual requests to the attribute store")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени процесса в хранилище атрибутов по бд Program")
class TestRequestProgramProcessNameInAttributeStoreByIndexes:
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

    @allure.title("Ограничение на кол-во возвращаемых данных")
    def test_number_of_strings(self):
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        check.greater_equal(len(parsed_data), 1)
        check.less_equal(len(parsed_data), 1000)

    @allure.title("Возвращаемые данные")
    def test_return_data(self):
        data = [
            "c:\\program files\\winrar\\winrar.exe",
            "c:\\program files\\tracker software\\pdf editor\\pdfxedit.exe",
            "c:\\users\\admin1.test\\appdata\\local\\temp\\is-mtsp0.tmp\\dbforgepostgresql22_shareappscrack.com.tmp",
            "c:\\users\\admin1.test\\appdata\\roaming\\utorrent\\utorrent.exe",
            "c:\\windows\\system32\\mmc.exe",
            "c:\\windows\\system32\\cmd.exe",
            "c:\\program files\\microsoft office\\root\\office16\\winword.exe",
            "c:\\windows\\syswow64\\notepad.exe",
            "c:\\users\\admin1.test\\appdata\\local\\temp\\is-sl5ct.tmp\\dbforgepostgresql23.tmp",
            "c:\\users\\admin1.test\\appdata\\local\\slack\\app-4.28.171\\slack.exe",
            "c:\\program files\\windowsapps\\38526medialife.photosopenerforwin10_0.0.14.0_x64__1crh1k73ty8mg\\magickviewer\\magickviewer.exe",
            "c:\\program files (x86)\\total commander\\plugins\\exe\\akelpad.exe",
            "c:\\program files\\7-zip\\7zg.exe",
            "c:\\program files\\the bat!\\thebat.exe",
            "\\\\dc\\soft\\_sql\\dbforge studio 2.2.207 for postgresql\\crack\\devart_dbforge_trialloader.exe",
            "c:\\users\\admin1.test\\appdata\\local\\temp\\is-espop.tmp\\dbforgesql58ent_downloadly.ir.tmp",
            "c:\\users\\admin1.test\\appdata\\local\\temp\\_iu14d2n.tmp",
            "c:\\program files\\microsoft office\\root\\office16\\excel.exe",
            "c:\\windows\\explorer.exe",
            "c:\\windows\\systemapps\\shellexperiencehost_cw5n1h2txyewy\\shellexperiencehost.exe",
            "c:\\program files\\vmware\\vmware tools\\vmtoolsd.exe",
            "c:\\program files\\dbeaver\\dbeaver.exe",
            "c:\\program files\\google\\chrome\\application\\chrome.exe",
            "c:\\program files\\mozilla firefox\\firefox.exe",
            "c:\\program files (x86)\\total commander\\totalcmd.exe",
            "c:\\program files\\devart\\dbforge studio for sql server\\dbforgesql.exe",
            "c:\\users\\admin1.test\\appdata\\local\\slack\\app-4.27.154\\slack.exe",
            "c:\\windows\\systemapps\\microsoft.windows.search_cw5n1h2txyewy\\searchapp.exe",
            "c:\\program files\\devart\\dbforge studio for postgresql\\dbforgepostgresql.exe",
            "c:\\windows\\system32\\systempropertiesadvanced.exe",
        ]
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(parsed_data))
        with allure.step("Кол-во данных"):
            check.equal(len(parsed_data), 30)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
