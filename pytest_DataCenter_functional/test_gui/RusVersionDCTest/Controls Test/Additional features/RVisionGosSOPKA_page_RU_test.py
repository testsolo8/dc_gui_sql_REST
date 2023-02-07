# Standart libraries
import time

# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import RVisionGosSOPKAPage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y09{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def addition_of_controlled_information_resource_window(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y09{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=RVisionGosSOPKAPage.add["title_ru"]).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("RUS Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsRU
@pytest.mark.testGUI_RusVersionDCTest_ControlsTest_Additionalfeatures
class TestRVisionGosSOPKAPage:
    @allure.story("тест главного окна настройки ГосСОПКА")
    class TestRVisionGosSOPKAMainPage:
        def test_cancel(self, handle):
            cancel = (
                handle.by(name=RVisionGosSOPKAPage.cancel["title_ru"])
                .find()
                .window_text()
            )
            check.equal(cancel, "Отменить")

        def test_apply(self, handle):
            apply = (
                handle.by(name=RVisionGosSOPKAPage.apply["title_ru"])
                .find()
                .window_text()
            )
            check.equal(apply, "Применить")

        def test_gosSOPKA(self, handle):
            gosSOPKA = (
                handle.by(name=RVisionGosSOPKAPage.gosSOPKA["title_ru"])
                .find()
                .window_text()
            )
            check.equal(gosSOPKA, "ГосСОПКА")

        def test_edit(self, handle):
            edit = (
                handle.by(name=RVisionGosSOPKAPage.edit["title_ru"])
                .find()
                .window_text()
            )
            check.equal(edit, "Редактировать")

        def test_delete(self, handle):
            delete = (
                handle.by(name=RVisionGosSOPKAPage.delete["title_ru"])
                .find()
                .window_text()
            )
            check.equal(delete, "Удалить")

        def test_add(self, handle):
            add = (
                handle.by(name=RVisionGosSOPKAPage.add["title_ru"]).find().window_text()
            )
            check.equal(add, "Добавить")

        def test_controlled_information_resources(self, handle):
            controlled_information_resources = (
                handle.by(
                    name=RVisionGosSOPKAPage.controlled_information_resources[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                controlled_information_resources,
                "Контролируемые информационные ресурсы",
            )

        def test_check_connection(self, handle):
            check_connection = (
                handle.__getattribute__(
                    RVisionGosSOPKAPage.check_connection["attribute_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(check_connection, "Проверить соединение")

        def test_token(self, handle):
            token = (
                handle.__getattribute__(RVisionGosSOPKAPage.token["attribute_ru"])
                .find()
                .window_text()
            )
            check.equal(token, "Токен")

        def test_server(self, handle):
            server = (
                handle.by(name=RVisionGosSOPKAPage.server["title_ru"])
                .find()
                .window_text()
            )
            check.equal(server, "Сервер")

        def test_connection_settings(self, handle):
            connection_settings = (
                handle.__getattribute__(
                    RVisionGosSOPKAPage.connection_settings["attribute_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(connection_settings, "Настройки подключения:")

        def test_creation_of_incidents_in_R_Vision(self, handle):
            creation_of_incidents_in_R_Vision = (
                handle.by(
                    name=RVisionGosSOPKAPage.creation_of_incidents_in_R_Vision[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                creation_of_incidents_in_R_Vision, "Создание инцидентов в R-Vision"
            )

        def test_settings_of_components_for_incidents_creation(self, handle):
            settings_of_components_for_incidents_creation = (
                handle.by(
                    name=RVisionGosSOPKAPage.settings_of_components_for_incidents_creation[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                settings_of_components_for_incidents_creation,
                "Настройки компонентов для создания инцидентов:",
            )

        def test_connection_settings2(self, handle):
            connection_settings2 = (
                handle.__getattribute__(
                    RVisionGosSOPKAPage.connection_settings2["attribute_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(connection_settings2, "Настройки подключения:")

        def test_category(self, handle):
            category = (
                handle.__getattribute__(RVisionGosSOPKAPage.category["attribute_ru"])
                .find()
                .window_text()
            )
            check.equal(category, "Категория")

        def test_company(self, handle):
            company = (
                handle.__getattribute__(RVisionGosSOPKAPage.company["attribute_ru"])
                .find()
                .window_text()
            )
            check.equal(company, "Организация")

        def test_category2(self, handle):
            category2 = (
                handle.__getattribute__(RVisionGosSOPKAPage.category2["attribute_ru"])
                .find()
                .window_text()
            )
            check.equal(category2, "Категория")

        def test_company2(self, handle):
            company2 = (
                handle.__getattribute__(RVisionGosSOPKAPage.company2["attribute_ru"])
                .find()
                .window_text()
            )
            check.equal(company2, "Организация")

        def test_siem(self, handle):
            siem = (
                handle.by(name=RVisionGosSOPKAPage.siem["title_ru"])
                .find()
                .window_text()
            )
            check.equal(siem, "SIEM")

        def test_category3(self, handle):
            category3 = (
                handle.__getattribute__(RVisionGosSOPKAPage.category3["attribute_ru"])
                .find()
                .window_text()
            )
            check.equal(category3, "Категория")

        def test_company3(self, handle):
            company3 = (
                handle.__getattribute__(RVisionGosSOPKAPage.company3["attribute_ru"])
                .find()
                .window_text()
            )
            check.equal(company3, "Организация")

        def test_alert_center(self, handle):
            alert_center = (
                handle.by(name=RVisionGosSOPKAPage.alert_center["title_ru"])
                .find()
                .window_text()
            )
            check.equal(alert_center, "Alert Center")

        def test_analytic_console(self, handle):
            analytic_console = (
                handle.by(name=RVisionGosSOPKAPage.analytic_console["title_ru"])
                .find()
                .window_text()
            )
            check.equal(analytic_console, "Analytic Console")

        def test_r_vision_server(self, handle):
            r_vision_server = (
                handle.by(name=RVisionGosSOPKAPage.r_vision_server["title_ru"])
                .find()
                .window_text()
            )
            check.equal(r_vision_server, "R-Vision сервер")

        def test_token2(self, handle):
            token2 = (
                handle.__getattribute__(RVisionGosSOPKAPage.token2["attribute_ru"])
                .find()
                .window_text()
            )
            check.equal(token2, "Токен")

        def test_check_connection2(self, handle):
            check_connection2 = (
                handle.__getattribute__(
                    RVisionGosSOPKAPage.check_connection2["attribute_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(check_connection2, "Проверить соединение")

    @allure.story(
        "тест окна настройки добавления контролируемого информационного ресурса ГосСОПКА"
    )
    class TestRVisionGosSOPKAAddControlledInformationResourceWindow:
        def test_addition_of_controlled_information_resource(
            self, addition_of_controlled_information_resource_window
        ):
            addition_of_controlled_information_resource = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.addition_of_controlled_information_resource[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                addition_of_controlled_information_resource,
                "Добавление контролируемого информационного ресурса",
            )

        def test_category_in_GosSOPKA(
            self, addition_of_controlled_information_resource_window
        ):
            category_in_GosSOPKA = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.category_in_GosSOPKA["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(category_in_GosSOPKA, "Категория в ГосСОПКА:")

        def test_component(self, addition_of_controlled_information_resource_window):
            component = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.component["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(component, "Компонент:")

        def test_setup_of_components_to_create_incidents(
            self, addition_of_controlled_information_resource_window
        ):
            setup_of_components_to_create_incidents = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.setup_of_components_to_create_incidents[
                        "title_ru"
                    ],
                    found_index=RVisionGosSOPKAPage.setup_of_components_to_create_incidents[
                        "found_index"
                    ],
                )
                .find()
                .window_text()
            )
            check.equal(
                setup_of_components_to_create_incidents,
                "Настройки компонентов для создания инцидентов:",
            )

        def test_cancel2(self, addition_of_controlled_information_resource_window):
            cancel2 = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.cancel2["title_ru"],
                    found_index=RVisionGosSOPKAPage.cancel2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel2, "Отменить")

        def test_save(self, addition_of_controlled_information_resource_window):
            save = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.save["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(save, "Сохранить")

        def test_email(self, addition_of_controlled_information_resource_window):
            email = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.email["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(email, "Email:")

        def test_phone(self, addition_of_controlled_information_resource_window):
            phone = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.phone["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(phone, "Контактный телефон:")

        def test_position_role(
            self, addition_of_controlled_information_resource_window
        ):
            position_role = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.position_role["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(position_role, "Должность/роль:")

        def test_full_name(self, addition_of_controlled_information_resource_window):
            full_name = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.full_name["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(full_name, "ФИО:")

        def test_responsible_for_incident_alert(
            self, addition_of_controlled_information_resource_window
        ):
            responsible_for_incident_alert = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.responsible_for_incident_alert["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                responsible_for_incident_alert,
                "Ответственный за уведомление об инциденте:",
            )

        def test_building_number(
            self, addition_of_controlled_information_resource_window
        ):
            building_number = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.building_number["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(building_number, "Номер здания:")

        def test_street(self, addition_of_controlled_information_resource_window):
            street = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.street["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(street, "Улица:")

        def test_city(self, addition_of_controlled_information_resource_window):
            city = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.city["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(city, "Город:")

        def test_country_geocode(
            self, addition_of_controlled_information_resource_window
        ):
            country_geocode = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.country_geocode["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(country_geocode, "Геокод страны:")

        def test_location(self, addition_of_controlled_information_resource_window):
            location = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.location["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(location, "Месторасположение:")

        def test_name(self, addition_of_controlled_information_resource_window):
            name = (
                addition_of_controlled_information_resource_window.__getattribute__(
                    RVisionGosSOPKAPage.name["attribute_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(name, "Наименование:")

        def test_object_owner(self, addition_of_controlled_information_resource_window):
            object_owner = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.object_owner["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(object_owner, "Владелец объекта:")

        def test_no(self, addition_of_controlled_information_resource_window):
            no = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.no["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(no, "Нет")

        def test_yes(self, addition_of_controlled_information_resource_window):
            yes = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.yes["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(yes, "Да")

        def test_telecommunication_networks_connection(
            self, addition_of_controlled_information_resource_window
        ):
            telecommunication_networks_connection = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.telecommunication_networks_connection[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                telecommunication_networks_connection,
                "Подключение к сетям электросвязи:",
            )

        def test_field_of_activity(
            self, addition_of_controlled_information_resource_window
        ):
            field_of_activity = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.field_of_activity["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(field_of_activity, "Сфера деятельности:")

        def test_category4(self, addition_of_controlled_information_resource_window):
            category4 = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.category4["title_ru"],
                    found_index=RVisionGosSOPKAPage.category4["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(category4, "Категория:")

        def test_name2(self, addition_of_controlled_information_resource_window):
            name2 = (
                addition_of_controlled_information_resource_window.__getattribute__(
                    RVisionGosSOPKAPage.name2["attribute_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(name2, "Наименование КИИ:")

        def test_controlled_information_object(
            self, addition_of_controlled_information_resource_window
        ):
            controlled_information_object = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.controlled_information_object["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                controlled_information_object,
                "Контролируемый объект информации инфраструктуры",
            )
