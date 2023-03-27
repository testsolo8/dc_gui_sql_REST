# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import UserCardsPage


@pytest.fixture(scope="class")
def handle(start_test_page):
    send_keys("{VK_MENU down}Y4Y06{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def confirm_clear_db(start_test_page, title_key):
    send_keys("{VK_MENU down}Y4Y06{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    handle.by(name=UserCardsPage.clear_database[title_key]).click()
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Additionalfeatures
class TestUserCardsPage:
    @allure.story("тест главного окна UserCards")
    class TestUserCardsMainPage:
        def test_cancel_button(self, handle, title_key):
            cancel_button = handle.by(name=UserCardsPage.cancel_button[title_key]).find().window_text()
            check.equal(cancel_button, UserCardsPage.cancel_button[title_key])

        def test_apply_button(self, handle, title_key):
            apply_button = handle.by(name=UserCardsPage.apply_button[title_key]).find().window_text()
            check.equal(apply_button, UserCardsPage.apply_button[title_key])

        def test_clear_database(self, handle, title_key):
            clear_database = handle.by(name=UserCardsPage.clear_database[title_key]).find().window_text()
            check.equal(clear_database, UserCardsPage.clear_database[title_key])

        def test_configure_connection_to_the_selected_server(self, handle, title_key):
            configure_connection_to_the_selected_server = (
                handle.by(name=UserCardsPage.configure_connection_to_the_selected_server[title_key])
                .find()
                .window_text()
            )
            check.equal(
                configure_connection_to_the_selected_server,
                UserCardsPage.configure_connection_to_the_selected_server[title_key],
            )

        def test_stop(self, handle, title_key):
            stop = handle.by(name=UserCardsPage.stop[title_key]).find().window_text()
            check.equal(stop, UserCardsPage.stop[title_key])

        def test_only_from_the_selected_indexes(self, handle, title_key):
            only_from_the_selected_indexes = (
                handle.by(name=UserCardsPage.only_from_the_selected_indexes[title_key]).find().window_text()
            )
            check.equal(only_from_the_selected_indexes, UserCardsPage.only_from_the_selected_indexes[title_key])

        def test_all_available_indexes_from_the_list(self, handle, title_key):
            all_available_indexes_from_the_list = (
                handle.by(name=UserCardsPage.all_available_indexes_from_the_list[title_key]).find().window_text()
            )
            check.equal(
                all_available_indexes_from_the_list,
                UserCardsPage.all_available_indexes_from_the_list[title_key],
            )

        def test_user_cards_fetcher(self, handle, title_key):
            user_cards_fetcher = handle.by(name=UserCardsPage.user_cards_fetcher[title_key]).find().window_text()
            check.equal(user_cards_fetcher, UserCardsPage.user_cards_fetcher[title_key])

        def test_create_card_for_external_contacts(self, handle, title_key):
            create_card_for_external_contacts = (
                handle.by(name=UserCardsPage.create_card_for_external_contacts[title_key]).find().window_text()
            )
            check.equal(create_card_for_external_contacts, UserCardsPage.create_card_for_external_contacts[title_key])

        def test_import_data_starting_from_the_date(self, handle, title_key):
            import_data_starting_from_the_date = (
                handle.by(name=UserCardsPage.import_data_starting_from_the_date[title_key]).find().window_text()
            )
            check.equal(
                import_data_starting_from_the_date,
                UserCardsPage.import_data_starting_from_the_date[title_key],
            )

        def test_indexes_reading_and_synchronization(self, handle, title_key):
            indexes_reading_and_synchronization = (
                handle.by(name=UserCardsPage.indexes_reading_and_synchronization[title_key]).find().window_text()
            )
            check.equal(
                indexes_reading_and_synchronization,
                UserCardsPage.indexes_reading_and_synchronization[title_key],
            )

        def test_sources(self, handle, title_key):
            sources = handle.by(name=UserCardsPage.sources[title_key]).find().window_text()
            check.equal(
                sources,
                UserCardsPage.sources[title_key],
            )

    @allure.story("тест окна подтверждения очистки БД UserCards")
    class TestConfirmClearDBWindow:
        def test_confirm(self, confirm_clear_db, title_key):
            confirm = confirm_clear_db.by(name=UserCardsPage.confirm[title_key]).find().window_text()
            check.equal(confirm, UserCardsPage.confirm[title_key])

        def test_no_button(self, confirm_clear_db, title_key):
            no_button = confirm_clear_db.by(name=UserCardsPage.no_button[title_key]).find().window_text()
            check.equal(no_button, UserCardsPage.no_button[title_key])

        def test_yes_button(self, confirm_clear_db, title_key):
            yes_button = confirm_clear_db.by(name=UserCardsPage.yes_button[title_key]).find().window_text()
            check.equal(yes_button, UserCardsPage.yes_button[title_key])
