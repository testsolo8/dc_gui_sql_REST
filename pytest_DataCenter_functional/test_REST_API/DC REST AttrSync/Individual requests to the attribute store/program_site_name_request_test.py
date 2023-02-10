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

path = "https://" + base_url_dc() + ":9088/datacenter/api/v2/attributes/url"
body = {"protocolIds": ["fd165b6f-63ca-413d-a3c0-109a9906a491"], "limit": 1000}
r = requests.post(url=path, json=body, verify=False)


@allure.epic("DC REST AttrSync")
@allure.feature("Individual requests to the attribute store")
@pytest.mark.testRESTAPI
@allure.story("Запрос имени сайта в хранилище атрибутов по бд Program")
class TestRequestProgramSiteNameInAttributeStoreByIndexes:
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
        check.greater_equal(len(data_dict), 1)
        check.less_equal(len(data_dict), 1000)

    @allure.title("Возвращаемые данные")
    def test_return_data(self):
        data = [
            "https://www.devart.com/dbforge/postgresql/studio/download.html",
            "ixbt.com/mobile/tecno-spark-9-pro-review.html",
            "devart.com/dbforge/mysql/studio/download.html",
            "devart.com/dbforge/sql/sql-tools/ordering.html",
            "ixbt.com/news/2022/08/18/k-rszo-himars-dobavilis-eshe-i-harm--protivoradiolokacionnye-rakety-kotorye-ssha-postavljajut-ukraine.html",
            "Hola VPN - The Website Unblocker - Интернет-магазин Chrome - Google Chrome",
            "devart.com/dbforge/sql/studio/download.html",
            "ixbt.com/infopages/recovery-toolbox-for-rar.html",
            "url:empty",
            "https://www.msn.com/en-xl/feed?ocid=winp1taskbar\u0026cvid=5e57eb471ec04100b4437daa6b05cbef",
            "about:addons",
            "ixbt.com/sw/",
            "devart.com/dbforge/sql/studio/ordering.html",
            "citilink.ru/product/kolonki-sven-ms-1821-2-1-chernyi-44vt-1724908/",
            "chrome-extension://gkojfkhlekighikafcpjkiklfbnlmeio/js/popup.html",
            "chrome://extensions/?id=gkojfkhlekighikafcpjkiklfbnlmeio",
            "chrome://read-later.top-chrome/",
            "ixbt.photo/?id=album:67227",
            "ixbt.photo/?id=photo:1513561",
            "yandex.ru/search/?text=как+узнать+версию+офиса\u0026lr=39",
            "nnmclub.to",
            "ixbt.com/mobile/",
            "yandex.ru/search/?text=Sven+MS-1821\u0026",
            "yandex.ru/search/?text=dbforge+studio+for+mysql\u0026",
            "https://www.devart.com/dbforge/sql/studio/successful-install.html?utm_source=DevartStudioMSSql\u0026utm_medium=install\u0026utm_campaign=UI_products_setup",
            "mail.google.com/mail/u/0/#inbox",
            "accounts.google.com/Logout",
            "chrome://extensions",
            "ixbt.games/page/about.html",
            "ixbt.com/3dv/nvidia-geforce-gtx-1630-review.html",
            "https://chrome.google.com/webstore/detail/hola-vpn-the-website-unbl/gkojfkhlekighikafcpjkiklfbnlmeio",
            "ixbt.com",
            "chrome.google.com/webstore/search/vpn",
            "ixbt.photo/?id=photo:1514182",
            "ixbt.com/news/2022/08/30/xiaomi-redmi-11-prime-5g-redmi-10-prime.html",
            "devart.com/dbforge/postgresql/",
            "ixbt.photo/?id=photo:1513963",
            "yandex.ru/search/?text=power+shell+генерация+бд+ms+sql\u0026lr=39\u0026suggest_reqid=397935640164758835046493635895253",
            "devart.com/dbforge/postgresql/studio/download.html",
            "http://fz139.ttk.ru/",
            "ixbt.photo/?id=photo:1513562",
            "https://www.msn.com/en-xl/feed?ocid=winp1taskbar\u0026cvid=0205cb40024c4016b4d48bc326508875",
            "chrome://extensions/",
            "mail.google.com/mail/u/0/",
            "disk.yandex.ru/client/disk/15-08-2022",
            "ixbt.games",
            "chrome-extension://bihmplhobchoageeokmgbdihknkjbknd/panel/index.html",
            "docs.microsoft.com/ru-ru/powershell/module/sqlserver/?view=sqlserver-ps",
            "accounts.google.com/ServiceLogin?elo=1",
            "hola.org/unblock_demo?ext_ver=1.201.563\u0026uuid=d656aa30f8c5c9a198f9e578f4d4fa18",
            "ixbt.com/infopages/recovery-toolbox-for-sql-server.html",
            "citilink.ru/product/kolonki-sven-ms-2055-2-1-chernyi-sv-016609-1081451/",
            "hola.org/access/popular/russia?utm_source=holaext",
            "dns-shop.ru/product/7e7deb8be0002ff4/kolonki-21-sven-ms-1821/",
            "ixbt.com/live/market/item/sven/blog/32550.html?yrwinfo=1661864481259354-6262400748590111079-vla1-1510-vla-l7-balancer-8080-BAL-6377",
            "https://disk.yandex.ru/d/x9WDp9c-NCJeQw",
            "ixbt.com/home/makita-dtm51z-review.html",
            "chrome.google.com/webstore/category/extensions",
            "yandex.ru/search/?text=nnm-club.me\u0026",
            "forum.ixbt.com",
            "chrome.google.com/webstore/detail/hola-vpn-the-website-unbl/gkojfkhlekighikafcpjkiklfbnlmeio",
        ]
        data_dict = r.json()
        with allure.step("Возвращаемые данные"):
            check.is_true(set(data).issubset(data_dict))
        with allure.step("Кол-во данных"):
            check.equal(len(data_dict), 102)

    @allure.title("Проверка возвращаемой схемы JSON")
    def test_schema(self):
        schema = {
            "type": "array",
        }
        resp = r.json()
        validate(resp, schema=schema)
