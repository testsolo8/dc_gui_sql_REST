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

path = "https://" + base_url_dc() + ":9088/datacenter/api/v2/attributes/doc_name"
body = {"protocolIds": ["8b09411d-2145-477d-b781-2bd2b679cf93"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Request document name in attribute store by indexes")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени документа в хранилище атрибутов по индексу DropBox")
class TestRequestDocumentNameInAttributeStoreByIndexes:
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
            "html\\helpcmdsm.htm",
            "html\\helptoolbarbuttons.htm",
            "html\\helparcnonrar.htm",
            "html\\helprar5format.htm",
            "html\\helpsfxlicense.htm",
            "show_tree.htm",
            "+_plus_n34_t7_печати_штампы_гпи.tif",
            "html\\helparcpassword.htm",
            "воина и мир_1_1013.txt",
            "+_plus_n11_t7_печати_штампы_к.104_29122014_160633.jpg",
            "html\\helpcommandlinesyntax.htm",
            "dlg_unpack.htm",
            "signtool.exe",
            "html\\helporganizethemes.htm",
            "dlg_internalzipconfig.htm",
            "about_box.htm",
            "html\\helpswieml.htm",
            "putty-64bit-0.70-installer.msi",
            "ocam\\app\\ocam\\language\\spanish.ini",
            "html\\helpswrv.htm",
            "windows\\rar.pif",
            "html\\helphelpmenu.htm",
            "html\\helpcmdr.htm",
            "internal_associations.htm",
            "html\\helpcommandsbenchmark.htm",
            "html\\helpwizardarcextract.htm",
            "html\\helpsfxoptlicense.htm",
            "winconen.sfx",
            "ocam\\app\\ocam\\language\\dutch.ini",
            "define_server_type.htm",
            "unacev2.dll",
            "html\\helpswsl.htm",
            "html\\helpsimplecommandlinearchiving.htm",
            "dlg_verifysfv.htm",
            "html\\helpswibck.htm",
            "воина и мир_1_5_671.txt",
            "dlg_configbuttonbar.htm",
            "ocam\\app\\ocam\\v414.0x86\\hooksurfacedll.dll",
            "html\\helpgetarctime.htm",
            "menu_starter.htm",
            "cglptnt.sys",
            "html\\helpmasterpasswordprof.htm",
            "rarlng.dll",
            "html\\helpswioff.htm",
        ]
        data_dict = r.json()
        data_str = json.dumps(data_dict)
        parsed_data = json.loads(data_str)
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(parsed_data))
        with allure.step("Кол-во данных"):
            check.equal(len(parsed_data), 751)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
