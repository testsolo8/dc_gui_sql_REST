# Standart libraries
import random
import time

# Third party packages
import allure
import pytest
from assertpy import assert_that, soft_assertions
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import EmailNotificationsPage


@pytest.fixture(scope="module")
def handle(start_test_page_ru):
    send_keys("{VK_MENU down}Y3Y7{VK_MENU up}")
    app = start_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(3)
@allure.epic("Various independent tests")
@allure.feature("Настройка адресов почтовых уведомлений")
@pytest.mark.testGUI_VariousIndependentTests_ConfiguringEmailNotificationAddresses
class TestConfiguringEmailNotificationAddresses:
    @allure.story(
        "Настройка адресов почтовых уведомлений (добавление двух адресов в каждую строку)"
    )
    def test_configuring_email_notification_addresses(self, handle):
        handle.by(
            name="Отправлять отчеты по почте",
            class_name="TcxCheckBox",
            control_type="Pane",
        ).click_input()
        handle.__getattribute__("Edit26").set_focus().type_keys("1.1.1.1")
        handle.__getattribute__("Edit24").set_focus().type_keys("test" "+2" "test.mail")
        handle.by(
            name="Отметить все", class_name="TcxCheckBox", control_type="Pane"
        ).click_input()
        # Первый блок
        handle.__getattribute__("Pane64").click_input()
        handle.__getattribute__("Edit23").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        handle.__getattribute__("Pane63").click_input()
        handle.__getattribute__("Edit22").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        handle.__getattribute__("Pane62").click_input()
        handle.__getattribute__("Edit21").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        handle.__getattribute__("Pane61").click_input()
        handle.__getattribute__("Edit20").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        handle.__getattribute__("Pane60").click_input()
        handle.__getattribute__("Edit19").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        handle.__getattribute__("Pane23").click_input()
        handle.__getattribute__("Edit6").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        handle.__getattribute__("Pane57").click_input()
        handle.__getattribute__("Edit17").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        handle.__getattribute__("Pane51").click_input()
        handle.__getattribute__("Edit15").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        handle.__getattribute__("Pane59").click_input()
        handle.__getattribute__("Edit18").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        handle.__getattribute__("Pane53").click_input()
        handle.__getattribute__("Edit5").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        handle.__getattribute__("Pane20").click_input()
        handle.__getattribute__("Edit4").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        handle.__getattribute__("Pane26").click_input()
        handle.__getattribute__("Edit7").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        # Второй блок
        handle.__getattribute__("Pane41").click_input()
        handle.__getattribute__("Edit12").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        handle.__getattribute__("Pane32").click_input()
        handle.__getattribute__("Edit9").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        handle.__getattribute__("Pane29").click_input()
        handle.__getattribute__("Edit8").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        # Третий блок
        handle.__getattribute__("Pane44").click_input()
        handle.__getattribute__("Edit13").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        handle.__getattribute__("Pane47").click_input()
        handle.__getattribute__("Edit14").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        handle.__getattribute__("Pane38").click_input()
        handle.__getattribute__("Edit11").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        handle.__getattribute__("Pane35").click_input()
        handle.__getattribute__("Edit10").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        # Общие параметры
        handle.__getattribute__("Edit16").set_focus().type_keys(
            "test" "+2" "test.mail," "{VK_SPACE}" "test2" "+2" "test2.mail2"
        )
        handle.by(name=EmailNotificationsPage.apply_button["title_ru"]).click()
        time.sleep(5)
        list_of_mail_fields = [
            "Pane18",
            "Pane19",
            "Pane22",
            "Pane25",
            "Pane28",
            "Pane31",
            "Pane34",
            "Pane37",
            "Pane40",
            "Pane43",
            "Pane46",
            "Pane50",
            "Pane55",
            "Pane56",
            "Pane65",
            "Pane66",
            "Pane69",
            "Pane70",
            "Pane71",
            "Pane72",
        ]
        with soft_assertions():
            field = random.choice(list_of_mail_fields)
            assert_that(handle.__getattribute__(str(field)).texts()).described_as(
                "Некорректный адрес почтовых уведомлений"
            ).is_equal_to(["test@test.mail, test2@test2.mail2"])
            field = random.choice(list_of_mail_fields)
            assert_that(handle.__getattribute__(str(field)).texts()).described_as(
                "Некорректный адрес почтовых уведомлений"
            ).is_equal_to(["test@test.mail, test2@test2.mail2"])
            field = random.choice(list_of_mail_fields)
            assert_that(handle.__getattribute__(str(field)).texts()).described_as(
                "Некорректный адрес почтовых уведомлений"
            ).is_equal_to(["test@test.mail, test2@test2.mail2"])
        handle.by(
            name="Отметить все", class_name="TcxCheckBox", control_type="Pane"
        ).click_input()
        handle.by(
            name="Отправлять отчеты по почте",
            class_name="TcxCheckBox",
            control_type="Pane",
        ).click_input()
        time.sleep(3)
        handle.by(name=EmailNotificationsPage.apply_button["title_ru"]).click()
        time.sleep(3)
