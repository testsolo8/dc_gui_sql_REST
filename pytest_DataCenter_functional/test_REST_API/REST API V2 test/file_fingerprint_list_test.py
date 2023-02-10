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

path = "http://" + base_url_dc() + ":9096/api/v1/fgpfiles"
r = requests.get(path, verify=False)


@allure.epic("REST API V2")
@allure.feature("File fingerprint list")
@pytest.mark.testRESTAPI
@allure.story("Получение отпечатков файлов")
class TestfileFingerprintList:
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
    def test_response_array_0(self):
        data_dict = r.json()
        check.equal(data_dict[0]["FileID"], "{142D4028-A7B0-C83B-A2DF-000256E7B562}")
        check.equal(
            data_dict[0]["FileName"],
            "C:\\Users\\m.bondar\\Documents\\Документы для фингерпринтов\\SHYAM - PASSPORT1.pdf",
        )
        check.equal(
            data_dict[0]["BinHashe"],
            "maam5korhkpqsstz3b2bp1b4vknoqynehdsafwzawgqfasxupi3op1wc0ui2odkgolwrs1eet2d2"
            "aa4bsl1f3bxaxg1m2skibr1zsmxafq1d4wodpqq50knpgpdcjpeo130hvezo3cyvuo3d0uf5zyjls"
            "um4y5g41051nyyuaxak13jbp5jkk35st5uhfygmxmbbqruvkai2s",
        )
        check.equal(data_dict[0]["TextHashe"], "")

    @pytest.mark.skip(reason="в текущей реализации среды для тестов не реализовано")
    def test_response_array_1(self):
        data_dict = r.json()
        check.equal(data_dict[1]["FileID"], "{15289097-192F-7255-7E9E-0088F81529B0}")
        check.equal(
            data_dict[1]["FileName"],
            "C:\\Users\\m.bondar\\Documents\\Документы для фингерпринтов\\INVITATION TO BIDS-Toyota.doc",
        )
        check.equal(
            data_dict[1]["BinHashe"],
            "aimk3brllyikv3vftumku4iedxzedq5bruszuyqqxn2sxjmtruy403fwgwduhzi3kmvmk4wvkj"
            "ia5n4msmbn4hqj5tztg0tt25drf2od2hymrr00i0ivihyiwc3ptxvphpiozmauacvqh1frjsbky"
            "jozbgesz05fb01vxkcdbjfmhl5x0qfumqov3fotp0v33frc53oxaocl2",
        )
        check.equal(
            data_dict[1]["TextHashe"],
            "u241mjvwp4j3rsmkjohsffpzss44tydsrd43kgmz4srua110cufabuhnb0tcklshuyh4kw2v5"
            "lmaz1q5pkqt5ooepu5jb0attsc435gbjnenpbdrc5wj01po10yhxijikpausa2k3dhlpe5sk2ozse"
            "xf2xgnxwwcyf2ytqnmumjuppur22mejk1cdrzvmoy4rsi3finjjgggt",
        )

    @pytest.mark.skip(reason="в текущей реализации среды для тестов не реализовано")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
