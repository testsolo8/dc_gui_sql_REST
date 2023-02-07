# Standart libraries
import time

# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto import Application
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import DataCenterServerPage
from DataCenter.settingsXML import SettingsXML


@pytest.fixture(scope="class")
def handle(start_test_page_en):
    send_keys("{VK_MENU down}Y3Y1{VK_MENU up}")
    app = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(3)
@allure.epic("Various independent tests")
@allure.feature("Изменения уровня логирования сервера DataCenter")
@pytest.mark.testGUI_VariousIndependentTests_CheckServerLogLevel
class TestServerLogLevel:
    @allure.story("уровень логирования сервера DataCenter Disabled")
    def test_server_log_level_disable(self, handle):
        if handle.__getattribute__("ComboBox3").texts()[0] == "Disabled":
            handle.__getattribute__("ComboBox3").type_keys("mi")
            handle.__getattribute__("ComboBox3").set_focus()
            handle.__getattribute__("ComboBox3").type_keys("di")
        else:
            handle.__getattribute__("ComboBox3").type_keys("di")
        time.sleep(1)
        handle.by(name="Notify if:").click_input()
        time.sleep(1)
        handle.by(name=DataCenterServerPage.apply_button["title_en"]).click()
        time.sleep(5)
        settings_xml = SettingsXML(
            "C:\\ProgramData\\Searchinform\\Searchinform DataCenter\\Settings.xml"
        )
        log_level = settings_xml.get_server_loglevel()
        settings_xml.push(False)
        check.equal(log_level, 0)

    @allure.story("уровень логирования сервера DataCenter Minimal")
    def test_server_log_level_minimal(self, handle):
        if handle.__getattribute__("ComboBox3").texts()[0] == "Minimal":
            handle.__getattribute__("ComboBox3").type_keys("di")
            handle.__getattribute__("ComboBox3").set_focus()
            handle.__getattribute__("ComboBox3").type_keys("mi")
        else:
            handle.__getattribute__("ComboBox3").type_keys("mi")
        time.sleep(1)
        handle.by(name="Notify if:").click_input()
        time.sleep(1)
        handle.by(name=DataCenterServerPage.apply_button["title_en"]).click()
        time.sleep(5)
        settings_xml = SettingsXML(
            "C:\\ProgramData\\Searchinform\\Searchinform DataCenter\\Settings.xml"
        )
        log_level = settings_xml.get_server_loglevel()
        settings_xml.push(False)
        check.equal(log_level, 1)

    @allure.story("уровень логирования сервера DataCenter Normal")
    def test_server_log_level_normal(self, handle):
        if handle.__getattribute__("ComboBox3").texts()[0] == "Normal":
            handle.__getattribute__("ComboBox3").type_keys("di")
            handle.__getattribute__("ComboBox3").set_focus()
            handle.__getattribute__("ComboBox3").type_keys("no")
        else:
            handle.__getattribute__("ComboBox3").type_keys("no")
        time.sleep(1)
        handle.by(name="Notify if:").click_input()
        time.sleep(1)
        handle.by(name=DataCenterServerPage.apply_button["title_en"]).click()
        time.sleep(5)
        settings_xml = SettingsXML(
            "C:\\ProgramData\\Searchinform\\Searchinform DataCenter\\Settings.xml"
        )
        log_level = settings_xml.get_server_loglevel()
        settings_xml.push(False)
        check.equal(log_level, 2)

    @allure.story("уровень логирования сервера DataCenter Detailed")
    def test_server_log_level_detailed(self, handle):
        if handle.__getattribute__("ComboBox3").texts()[0] == "Detailed":
            handle.__getattribute__("ComboBox3").type_keys("di")
            handle.__getattribute__("ComboBox3").set_focus()
            handle.__getattribute__("ComboBox3").type_keys("de")
        else:
            handle.__getattribute__("ComboBox3").type_keys("de")
        time.sleep(1)
        handle.by(name="Notify if:").click_input()
        time.sleep(1)
        handle.by(name=DataCenterServerPage.apply_button["title_en"]).click()
        time.sleep(5)
        settings_xml = SettingsXML(
            "C:\\ProgramData\\Searchinform\\Searchinform DataCenter\\Settings.xml"
        )
        log_level = settings_xml.get_server_loglevel()
        settings_xml.push(False)
        check.equal(log_level, 3)
