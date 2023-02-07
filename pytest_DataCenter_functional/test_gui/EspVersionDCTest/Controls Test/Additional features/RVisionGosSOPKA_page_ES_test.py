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
def handle(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y09{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def addition_of_controlled_information_resource_window(start_fast_test_page_es):
    send_keys("{VK_MENU down}Y4Y09{VK_MENU up}")
    app = start_fast_test_page_es
    handle = app.window(name_re="DataCenter*")
    handle.by(name=RVisionGosSOPKAPage.add["title_es"]).click_input()
    time.sleep(2)
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("ESP Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsES
@pytest.mark.testGUI_EspVersionDCTest_ControlsTest_Additionalfeatures
class TestRVisionGosSOPKAPage:
    @allure.story("тест главного окна настройки ГосСОПКА")
    class TestRVisionGosSOPKAMainPage:
        def test_cancel(self, handle):
            cancel = (
                handle.by(name=RVisionGosSOPKAPage.cancel["title_es"])
                .find()
                .window_text()
            )
            check.equal(cancel, "Cancelar")

        def test_apply(self, handle):
            apply = (
                handle.by(name=RVisionGosSOPKAPage.apply["title_es"])
                .find()
                .window_text()
            )
            check.equal(apply, "Aplicar")

        def test_gosSOPKA(self, handle):
            gosSOPKA = (
                handle.by(name=RVisionGosSOPKAPage.gosSOPKA["title_es"])
                .find()
                .window_text()
            )
            check.equal(gosSOPKA, "GosSOPKA")

        def test_edit(self, handle):
            edit = (
                handle.by(name=RVisionGosSOPKAPage.edit["title_es"])
                .find()
                .window_text()
            )
            check.equal(edit, "Editar")

        def test_delete(self, handle):
            delete = (
                handle.by(name=RVisionGosSOPKAPage.delete["title_es"])
                .find()
                .window_text()
            )
            check.equal(delete, "Borrar")

        def test_add(self, handle):
            add = (
                handle.by(name=RVisionGosSOPKAPage.add["title_es"]).find().window_text()
            )
            check.equal(add, "Añadir")

        def test_controlled_information_resources(self, handle):
            controlled_information_resources = (
                handle.by(
                    name=RVisionGosSOPKAPage.controlled_information_resources[
                        "title_es"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                controlled_information_resources, "Recursos de información controlados"
            )

        def test_check_connection(self, handle):
            check_connection = (
                handle.__getattribute__(
                    RVisionGosSOPKAPage.check_connection["attribute_es"]
                )
                .find()
                .window_text()
            )
            check.equal(check_connection, "Probar conexión")

        def test_token(self, handle):
            token = (
                handle.__getattribute__(RVisionGosSOPKAPage.token["attribute_es"])
                .find()
                .window_text()
            )
            check.equal(token, "Token")

        def test_server(self, handle):
            server = (
                handle.by(name=RVisionGosSOPKAPage.server["title_es"])
                .find()
                .window_text()
            )
            check.equal(server, "Servidor")

        def test_connection_settings(self, handle):
            connection_settings = (
                handle.__getattribute__(
                    RVisionGosSOPKAPage.connection_settings["attribute_es"]
                )
                .find()
                .window_text()
            )
            check.equal(connection_settings, "Ajustes de conexión:")

        def test_creation_of_incidents_in_R_Vision(self, handle):
            creation_of_incidents_in_R_Vision = (
                handle.by(
                    name=RVisionGosSOPKAPage.creation_of_incidents_in_R_Vision[
                        "title_es"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                creation_of_incidents_in_R_Vision, "Creación de incidentes en R-Vision "
            )

        def test_settings_of_components_for_incidents_creation(self, handle):
            settings_of_components_for_incidents_creation = (
                handle.by(
                    name=RVisionGosSOPKAPage.settings_of_components_for_incidents_creation[
                        "title_es"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                settings_of_components_for_incidents_creation,
                "Ajustes de componentes para la creación de incidentes:",
            )

        def test_connection_settings2(self, handle):
            connection_settings2 = (
                handle.__getattribute__(
                    RVisionGosSOPKAPage.connection_settings2["attribute_es"]
                )
                .find()
                .window_text()
            )
            check.equal(connection_settings2, "Ajustes de conexión:")

        def test_category(self, handle):
            category = (
                handle.__getattribute__(RVisionGosSOPKAPage.category["attribute_es"])
                .find()
                .window_text()
            )
            check.equal(category, "Categoría")

        def test_company(self, handle):
            company = (
                handle.__getattribute__(RVisionGosSOPKAPage.company["attribute_es"])
                .find()
                .window_text()
            )
            check.equal(company, "Empresa")

        def test_category2(self, handle):
            category2 = (
                handle.__getattribute__(RVisionGosSOPKAPage.category2["attribute_es"])
                .find()
                .window_text()
            )
            check.equal(category2, "Categoría")

        def test_company2(self, handle):
            company2 = (
                handle.__getattribute__(RVisionGosSOPKAPage.company2["attribute_es"])
                .find()
                .window_text()
            )
            check.equal(company2, "Empresa")

        def test_siem(self, handle):
            siem = (
                handle.by(name=RVisionGosSOPKAPage.siem["title_es"])
                .find()
                .window_text()
            )
            check.equal(siem, "SIEM")

        def test_category3(self, handle):
            category3 = (
                handle.__getattribute__(RVisionGosSOPKAPage.category3["attribute_es"])
                .find()
                .window_text()
            )
            check.equal(category3, "Categoría")

        def test_company3(self, handle):
            company3 = (
                handle.__getattribute__(RVisionGosSOPKAPage.company3["attribute_es"])
                .find()
                .window_text()
            )
            check.equal(company3, "Empresa")

        def test_alert_center(self, handle):
            alert_center = (
                handle.by(name=RVisionGosSOPKAPage.alert_center["title_es"])
                .find()
                .window_text()
            )
            check.equal(alert_center, "Alert Center")

        def test_analytic_console(self, handle):
            analytic_console = (
                handle.by(name=RVisionGosSOPKAPage.analytic_console["title_es"])
                .find()
                .window_text()
            )
            check.equal(analytic_console, "Analytic Console")

        def test_r_vision_server(self, handle):
            r_vision_server = (
                handle.by(name=RVisionGosSOPKAPage.r_vision_server["title_es"])
                .find()
                .window_text()
            )
            check.equal(r_vision_server, "Servidor R-Vision")

        def test_token2(self, handle):
            token2 = (
                handle.__getattribute__(RVisionGosSOPKAPage.token2["attribute_es"])
                .find()
                .window_text()
            )
            check.equal(token2, "Token")

        def test_check_connection2(self, handle):
            check_connection2 = (
                handle.__getattribute__(
                    RVisionGosSOPKAPage.check_connection2["attribute_es"]
                )
                .find()
                .window_text()
            )
            check.equal(check_connection2, "Probar conexión")

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
                        "title_es"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                addition_of_controlled_information_resource,
                "Adición del recurso de información controlado",
            )

        def test_category_in_GosSOPKA(
            self, addition_of_controlled_information_resource_window
        ):
            category_in_GosSOPKA = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.category_in_GosSOPKA["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(category_in_GosSOPKA, "Categoría en GosSOPKA:")

        def test_component(self, addition_of_controlled_information_resource_window):
            component = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.component["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(component, "Componente:")

        def test_setup_of_components_to_create_incidents(
            self, addition_of_controlled_information_resource_window
        ):
            setup_of_components_to_create_incidents = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.setup_of_components_to_create_incidents[
                        "title_es"
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
                "Configuración de componentes para crear incidentes:",
            )

        def test_cancel2(self, addition_of_controlled_information_resource_window):
            cancel2 = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.cancel2["title_es"],
                    found_index=RVisionGosSOPKAPage.cancel2["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(cancel2, "Cancelar")

        def test_save(self, addition_of_controlled_information_resource_window):
            save = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.save["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(save, "Guardar")

        def test_email(self, addition_of_controlled_information_resource_window):
            email = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.email["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(email, "Email:")

        def test_phone(self, addition_of_controlled_information_resource_window):
            phone = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.phone["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(phone, "Teléfono:")

        def test_position_role(
            self, addition_of_controlled_information_resource_window
        ):
            position_role = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.position_role["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(position_role, "Posición/ función:")

        def test_full_name(self, addition_of_controlled_information_resource_window):
            full_name = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.full_name["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(full_name, "Nombre completo:")

        def test_responsible_for_incident_alert(
            self, addition_of_controlled_information_resource_window
        ):
            responsible_for_incident_alert = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.responsible_for_incident_alert["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(
                responsible_for_incident_alert, "Responsable de alerta de incidente:"
            )

        def test_building_number(
            self, addition_of_controlled_information_resource_window
        ):
            building_number = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.building_number["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(building_number, "Número de edificio:")

        def test_street(self, addition_of_controlled_information_resource_window):
            street = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.street["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(street, "Calle:")

        def test_city(self, addition_of_controlled_information_resource_window):
            city = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.city["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(city, "Ciudad:")

        def test_country_geocode(
            self, addition_of_controlled_information_resource_window
        ):
            country_geocode = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.country_geocode["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(country_geocode, "Código geográfico:")

        def test_location(self, addition_of_controlled_information_resource_window):
            location = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.location["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(location, "Ubicación:")

        def test_name(self, addition_of_controlled_information_resource_window):
            name = (
                addition_of_controlled_information_resource_window.__getattribute__(
                    RVisionGosSOPKAPage.name["attribute_es"]
                )
                .find()
                .window_text()
            )
            check.equal(name, "Nombre:")

        def test_object_owner(self, addition_of_controlled_information_resource_window):
            object_owner = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.object_owner["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(object_owner, "Propietario de objeto:")

        def test_no(self, addition_of_controlled_information_resource_window):
            no = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.no["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(no, "No")

        def test_yes(self, addition_of_controlled_information_resource_window):
            yes = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.yes["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(yes, "Sí")

        def test_telecommunication_networks_connection(
            self, addition_of_controlled_information_resource_window
        ):
            telecommunication_networks_connection = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.telecommunication_networks_connection[
                        "title_es"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                telecommunication_networks_connection,
                "Conexión a redes de telecomunicación:",
            )

        def test_field_of_activity(
            self, addition_of_controlled_information_resource_window
        ):
            field_of_activity = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.field_of_activity["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(field_of_activity, "Campo de actividad:")

        def test_category4(self, addition_of_controlled_information_resource_window):
            category4 = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.category4["title_es"],
                    found_index=RVisionGosSOPKAPage.category4["found_index"],
                )
                .find()
                .window_text()
            )
            check.equal(category4, "Categoría:")

        def test_name2(self, addition_of_controlled_information_resource_window):
            name2 = (
                addition_of_controlled_information_resource_window.__getattribute__(
                    RVisionGosSOPKAPage.name2["attribute_es"]
                )
                .find()
                .window_text()
            )
            check.equal(name2, "Nombre:")

        def test_controlled_information_object(
            self, addition_of_controlled_information_resource_window
        ):
            controlled_information_object = (
                addition_of_controlled_information_resource_window.by(
                    name=RVisionGosSOPKAPage.controlled_information_object["title_es"]
                )
                .find()
                .window_text()
            )
            check.equal(
                controlled_information_object, "Objeto de información controlado"
            )
