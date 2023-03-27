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
def handle(start_test_page):
    send_keys("{VK_MENU down}Y4Y09{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def addition_of_controlled_information_resource_window(start_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y09{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=RVisionGosSOPKAPage.add[title_key]).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Additionalfeatures
class TestRVisionGosSOPKAPage:
    @allure.story("тест главного окна настройки ГосСОПКА")
    class TestRVisionGosSOPKAMainPage:
        def test_cancel(self, handle, title_key):
            cancel = handle.by(name=RVisionGosSOPKAPage.cancel[title_key]).find().window_text()
            check.equal(cancel, RVisionGosSOPKAPage.cancel[title_key])

        def test_apply(self, handle, title_key):
            apply = handle.by(name=RVisionGosSOPKAPage.apply[title_key]).find().window_text()
            check.equal(apply, RVisionGosSOPKAPage.apply[title_key])

        def test_gosSOPKA(self, handle, title_key):
            gosSOPKA = handle.by(name=RVisionGosSOPKAPage.gosSOPKA[title_key]).find().window_text()
            check.equal(gosSOPKA, RVisionGosSOPKAPage.gosSOPKA[title_key])

        def test_edit(self, handle, title_key):
            edit = handle.by(name=RVisionGosSOPKAPage.edit[title_key]).find().window_text()
            check.equal(edit, RVisionGosSOPKAPage.edit[title_key])

        def test_delete(self, handle, title_key):
            delete = handle.by(name=RVisionGosSOPKAPage.delete[title_key]).find().window_text()
            check.equal(delete, RVisionGosSOPKAPage.delete[title_key])

        def test_add(self, handle, title_key):
            add = handle.by(name=RVisionGosSOPKAPage.add[title_key]).find().window_text()
            check.equal(add, RVisionGosSOPKAPage.add[title_key])

        def test_controlled_information_resources(self, handle, title_key):
            controlled_information_resources = (
                handle.by(name=RVisionGosSOPKAPage.controlled_information_resources[title_key]).find().window_text()
            )
            check.equal(controlled_information_resources, RVisionGosSOPKAPage.controlled_information_resources[title_key])

        def test_check_connection(self, handle, title_key, attribute_key):
            check_connection = (
                handle.__getattribute__(RVisionGosSOPKAPage.check_connection[attribute_key]).find().window_text()
            )
            check.equal(check_connection, RVisionGosSOPKAPage.check_connection[title_key])

        def test_token(self, handle, title_key, attribute_key):
            token = handle.__getattribute__(RVisionGosSOPKAPage.token[attribute_key]).find().window_text()
            check.equal(token, RVisionGosSOPKAPage.token[title_key])

        def test_server(self, handle, title_key):
            server = handle.by(name=RVisionGosSOPKAPage.server[title_key]).find().window_text()
            check.equal(server, RVisionGosSOPKAPage.server[title_key])

        def test_connection_settings(self, handle, title_key, attribute_key):
            connection_settings = (
                handle.__getattribute__(RVisionGosSOPKAPage.connection_settings[attribute_key]).find().window_text()
            )
            check.equal(connection_settings, RVisionGosSOPKAPage.connection_settings[title_key])

        def test_creation_of_incidents_in_R_Vision(self, handle, title_key):
            creation_of_incidents_in_R_Vision = (
                handle.by(name=RVisionGosSOPKAPage.creation_of_incidents_in_R_Vision[title_key]).find().window_text()
            )
            check.equal(creation_of_incidents_in_R_Vision, RVisionGosSOPKAPage.creation_of_incidents_in_R_Vision[title_key])

        def test_settings_of_components_for_incidents_creation(self, handle, title_key):
            settings_of_components_for_incidents_creation = (
                handle.by(name=RVisionGosSOPKAPage.settings_of_components_for_incidents_creation[title_key])
                .find()
                .window_text()
            )
            check.equal(
                settings_of_components_for_incidents_creation,
                RVisionGosSOPKAPage.settings_of_components_for_incidents_creation[title_key],
            )

        def test_connection_settings2(self, handle, title_key, attribute_key):
            connection_settings2 = (
                handle.__getattribute__(RVisionGosSOPKAPage.connection_settings2[attribute_key]).find().window_text()
            )
            check.equal(connection_settings2, RVisionGosSOPKAPage.connection_settings2[title_key])

        def test_category(self, handle, title_key, attribute_key):
            category = handle.__getattribute__(RVisionGosSOPKAPage.category[attribute_key]).find().window_text()
            check.equal(category, RVisionGosSOPKAPage.category[title_key])

        def test_company(self, handle, title_key, attribute_key):
            company = handle.__getattribute__(RVisionGosSOPKAPage.company[attribute_key]).find().window_text()
            check.equal(company, RVisionGosSOPKAPage.company[title_key])

        def test_category2(self, handle, title_key, attribute_key):
            category2 = handle.__getattribute__(RVisionGosSOPKAPage.category2[attribute_key]).find().window_text()
            check.equal(category2, RVisionGosSOPKAPage.category2[title_key])

        def test_company2(self, handle, title_key, attribute_key):
            company2 = handle.__getattribute__(RVisionGosSOPKAPage.company2[attribute_key]).find().window_text()
            check.equal(company2, RVisionGosSOPKAPage.company2[title_key])

        def test_siem(self, handle, title_key):
            siem = handle.by(name=RVisionGosSOPKAPage.siem[title_key]).find().window_text()
            check.equal(siem, RVisionGosSOPKAPage.siem[title_key])

        def test_category3(self, handle, title_key, attribute_key):
            category3 = handle.__getattribute__(RVisionGosSOPKAPage.category3[attribute_key]).find().window_text()
            check.equal(category3, RVisionGosSOPKAPage.category3[title_key])

        def test_company3(self, handle, title_key, attribute_key):
            company3 = handle.__getattribute__(RVisionGosSOPKAPage.company3[attribute_key]).find().window_text()
            check.equal(company3, RVisionGosSOPKAPage.company3[title_key])

        def test_alert_center(self, handle, title_key):
            alert_center = handle.by(name=RVisionGosSOPKAPage.alert_center[title_key]).find().window_text()
            check.equal(alert_center, RVisionGosSOPKAPage.alert_center[title_key])

        def test_analytic_console(self, handle, title_key):
            analytic_console = handle.by(name=RVisionGosSOPKAPage.analytic_console[title_key]).find().window_text()
            check.equal(analytic_console, RVisionGosSOPKAPage.analytic_console[title_key])

        def test_r_vision_server(self, handle, title_key):
            r_vision_server = handle.by(name=RVisionGosSOPKAPage.r_vision_server[title_key]).find().window_text()
            check.equal(r_vision_server, RVisionGosSOPKAPage.r_vision_server[title_key])

        def test_token2(self, handle, title_key, attribute_key):
            token2 = handle.__getattribute__(RVisionGosSOPKAPage.token2[attribute_key]).find().window_text()
            check.equal(token2, RVisionGosSOPKAPage.token2[title_key])

        def test_check_connection2(self, handle, title_key, attribute_key):
            check_connection2 = (
                handle.__getattribute__(RVisionGosSOPKAPage.check_connection2[attribute_key]).find().window_text()
            )
            check.equal(check_connection2, RVisionGosSOPKAPage.check_connection2[title_key])

    @allure.story("тест окна настройки добавления контролируемого информационного ресурса ГосСОПКА")
    class TestRVisionGosSOPKAAddControlledInformationResourceWindow:
        def test_addition_of_controlled_information_resource(self, addition_of_controlled_information_resource_window, title_key):
            addition_of_controlled_information_resource = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.addition_of_controlled_information_resource[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(
                addition_of_controlled_information_resource,
                RVisionGosSOPKAPage.addition_of_controlled_information_resource[title_key],
            )

        def test_category_in_GosSOPKA(self, addition_of_controlled_information_resource_window, title_key):
            category_in_GosSOPKA = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.category_in_GosSOPKA[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(category_in_GosSOPKA, RVisionGosSOPKAPage.category_in_GosSOPKA[title_key])

        def test_component(self, addition_of_controlled_information_resource_window, title_key):
            component = (
                addition_of_controlled_information_resource_window.by(name=RVisionGosSOPKAPage.component[title_key])
                .find()
                .window_text()
            )
            check.equal(component, RVisionGosSOPKAPage.component[title_key])

        def test_setup_of_components_to_create_incidents(self, addition_of_controlled_information_resource_window, title_key):
            setup_of_components_to_create_incidents = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.setup_of_components_to_create_incidents[title_key],
                    found_index=RVisionGosSOPKAPage.setup_of_components_to_create_incidents["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(
                setup_of_components_to_create_incidents,
                RVisionGosSOPKAPage.setup_of_components_to_create_incidents[title_key],
            )

        def test_cancel2(self, addition_of_controlled_information_resource_window, title_key):
            cancel2 = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.cancel2[title_key],
                    found_index=RVisionGosSOPKAPage.cancel2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel2, RVisionGosSOPKAPage.cancel2[title_key])

        def test_save(self, addition_of_controlled_information_resource_window, title_key):
            save = (
                addition_of_controlled_information_resource_window.by(name=RVisionGosSOPKAPage.save[title_key])
                .find()
                .window_text()
            )
            check.equal(save, RVisionGosSOPKAPage.save[title_key])

        def test_email(self, addition_of_controlled_information_resource_window, title_key):
            email = (
                addition_of_controlled_information_resource_window.by(name=RVisionGosSOPKAPage.email[title_key])
                .find()
                .window_text()
            )
            check.equal(email, RVisionGosSOPKAPage.email[title_key])

        def test_phone(self, addition_of_controlled_information_resource_window, title_key):
            phone = (
                addition_of_controlled_information_resource_window.by(name=RVisionGosSOPKAPage.phone[title_key])
                .find()
                .window_text()
            )
            check.equal(phone, RVisionGosSOPKAPage.phone[title_key])

        def test_position_role(self, addition_of_controlled_information_resource_window, title_key):
            position_role = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.position_role[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(position_role, RVisionGosSOPKAPage.position_role[title_key])

        def test_full_name(self, addition_of_controlled_information_resource_window, title_key):
            full_name = (
                addition_of_controlled_information_resource_window.by(name=RVisionGosSOPKAPage.full_name[title_key])
                .find()
                .window_text()
            )
            check.equal(full_name, RVisionGosSOPKAPage.full_name[title_key])

        def test_responsible_for_incident_alert(self, addition_of_controlled_information_resource_window, title_key):
            responsible_for_incident_alert = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.responsible_for_incident_alert[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(responsible_for_incident_alert, RVisionGosSOPKAPage.responsible_for_incident_alert[title_key])

        def test_building_number(self, addition_of_controlled_information_resource_window, title_key):
            building_number = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.building_number[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(building_number, RVisionGosSOPKAPage.building_number[title_key])

        def test_street(self, addition_of_controlled_information_resource_window, title_key):
            street = (
                addition_of_controlled_information_resource_window.by(name=RVisionGosSOPKAPage.street[title_key])
                .find()
                .window_text()
            )
            check.equal(street, RVisionGosSOPKAPage.street[title_key])

        def test_city(self, addition_of_controlled_information_resource_window, title_key):
            city = (
                addition_of_controlled_information_resource_window.by(name=RVisionGosSOPKAPage.city[title_key])
                .find()
                .window_text()
            )
            check.equal(city, RVisionGosSOPKAPage.city[title_key])

        def test_country_geocode(self, addition_of_controlled_information_resource_window, title_key):
            country_geocode = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.country_geocode[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(country_geocode, RVisionGosSOPKAPage.country_geocode[title_key])

        def test_location(self, addition_of_controlled_information_resource_window, title_key):
            location = (
                addition_of_controlled_information_resource_window.by(name=RVisionGosSOPKAPage.location[title_key])
                .find()
                .window_text()
            )
            check.equal(location, RVisionGosSOPKAPage.location[title_key])

        def test_name(self, addition_of_controlled_information_resource_window, title_key, attribute_key):
            name = (
                addition_of_controlled_information_resource_window.__getattribute__(
                    RVisionGosSOPKAPage.name[attribute_key]
                )
                .find()
                .window_text()
            )
            check.equal(name, RVisionGosSOPKAPage.name[title_key])

        def test_object_owner(self, addition_of_controlled_information_resource_window, title_key):
            object_owner = (
                addition_of_controlled_information_resource_window.by(name=RVisionGosSOPKAPage.object_owner[title_key])
                .find()
                .window_text()
            )
            check.equal(object_owner, RVisionGosSOPKAPage.object_owner[title_key])

        def test_no(self, addition_of_controlled_information_resource_window, title_key):
            no = (
                addition_of_controlled_information_resource_window.by(name=RVisionGosSOPKAPage.no[title_key])
                .find()
                .window_text()
            )
            check.equal(no, RVisionGosSOPKAPage.no[title_key])

        def test_yes(self, addition_of_controlled_information_resource_window, title_key):
            yes = (
                addition_of_controlled_information_resource_window.by(name=RVisionGosSOPKAPage.yes[title_key])
                .find()
                .window_text()
            )
            check.equal(yes, RVisionGosSOPKAPage.yes[title_key])

        def test_telecommunication_networks_connection(self, addition_of_controlled_information_resource_window, title_key):
            telecommunication_networks_connection = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.telecommunication_networks_connection[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(
                telecommunication_networks_connection,
                RVisionGosSOPKAPage.telecommunication_networks_connection[title_key],
            )

        def test_field_of_activity(self, addition_of_controlled_information_resource_window, title_key):
            field_of_activity = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.field_of_activity[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(field_of_activity, RVisionGosSOPKAPage.field_of_activity[title_key])

        def test_category4(self, addition_of_controlled_information_resource_window, title_key):
            category4 = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.category4[title_key],
                    found_index=RVisionGosSOPKAPage.category4["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(category4, RVisionGosSOPKAPage.category4[title_key])

        def test_name2(self, addition_of_controlled_information_resource_window, title_key, attribute_key):
            name2 = (
                addition_of_controlled_information_resource_window.__getattribute__(
                    RVisionGosSOPKAPage.name2[attribute_key]
                )
                .find()
                .window_text()
            )
            check.equal(name2, RVisionGosSOPKAPage.name2[title_key])

        def test_controlled_information_object(self, addition_of_controlled_information_resource_window, title_key):
            controlled_information_object = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.controlled_information_object[title_key]
                )
                .find()
                .window_text()
            )
            check.equal(controlled_information_object, RVisionGosSOPKAPage.controlled_information_object[title_key])
