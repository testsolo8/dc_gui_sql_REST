# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import UserCardsPage


@pytest.fixture(scope="class")
def handle(start_test_page_en):
    send_keys("{VK_MENU down}Y4Y06{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def confirm_clear_db(start_test_page_en):
    send_keys("{VK_MENU down}Y4Y06{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    handle.by(name=UserCardsPage.clear_database["title_en"]).click()
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("ENG Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsEN
@pytest.mark.testGUI_EngVersionDCTest_ControlsTest_Additionalfeatures
class TestUserCardsPage:
    @allure.story("тест главного окна UserCards")
    class TestUserCardsMainPage:
        def test_cancel_button(self, handle):
            cancel_button = (
                handle.by(name=UserCardsPage.cancel_button["title_en"])
                .find()
                .window_text()
            )
            check.equal(cancel_button, "Cancel")

        def test_apply_button(self, handle):
            apply_button = (
                handle.by(name=UserCardsPage.apply_button["title_en"])
                .find()
                .window_text()
            )
            check.equal(apply_button, "Apply")

        def test_clear_database(self, handle):
            clear_database = (
                handle.by(name=UserCardsPage.clear_database["title_en"])
                .find()
                .window_text()
            )
            check.equal(clear_database, "Clear database")

        def test_configure_connection_to_the_selected_server(self, handle):
            configure_connection_to_the_selected_server = (
                handle.by(
                    name=UserCardsPage.configure_connection_to_the_selected_server[
                        "title_en"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                configure_connection_to_the_selected_server,
                "Configure connection to the selected server",
            )

        def test_stop(self, handle):
            stop = handle.by(name=UserCardsPage.stop["title_en"]).find().window_text()
            check.equal(stop, "Stop")

        def test_only_from_the_selected_indexes(self, handle):
            only_from_the_selected_indexes = (
                handle.by(name=UserCardsPage.only_from_the_selected_indexes["title_en"])
                .find()
                .window_text()
            )
            check.equal(
                only_from_the_selected_indexes, "Only from the selected indexes"
            )

        def test_all_available_indexes_from_the_list(self, handle):
            all_available_indexes_from_the_list = (
                handle.by(
                    name=UserCardsPage.all_available_indexes_from_the_list["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(
                all_available_indexes_from_the_list,
                "All available indexes from the list",
            )

        def test_user_cards_fetcher(self, handle):
            user_cards_fetcher = (
                handle.by(name=UserCardsPage.user_cards_fetcher["title_en"])
                .find()
                .window_text()
            )
            check.equal(user_cards_fetcher, "UserCardsFetcher")

        def test_create_card_for_external_contacts(self, handle):
            create_card_for_external_contacts = (
                handle.by(
                    name=UserCardsPage.create_card_for_external_contacts["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(
                create_card_for_external_contacts, "Create a card for external contacts"
            )

        def test_import_data_starting_from_the_date(self, handle):
            import_data_starting_from_the_date = (
                handle.by(
                    name=UserCardsPage.import_data_starting_from_the_date["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(
                import_data_starting_from_the_date,
                "Import data starting from the date",
            )

        def test_indexes_reading_and_synchronization(self, handle):
            indexes_reading_and_synchronization = (
                handle.by(
                    name=UserCardsPage.indexes_reading_and_synchronization["title_en"]
                )
                .find()
                .window_text()
            )
            check.equal(
                indexes_reading_and_synchronization,
                "Indexes reading and synchronization",
            )

        def test_sources(self, handle):
            sources = (
                handle.by(name=UserCardsPage.sources["title_en"]).find().window_text()
            )
            check.equal(
                sources,
                "Mail;HTTP IM;Lync;Viber;Telegram;Skype;WhatsApp;ProgramController;KeyLogger",
            )

    @allure.story("тест окна подтверждения очистки БД UserCards")
    class TestConfirmClearDBWindow:
        def test_confirm(self, confirm_clear_db):
            confirm = (
                confirm_clear_db.by(name=UserCardsPage.confirm["title_en"])
                .find()
                .window_text()
            )
            check.equal(confirm, "Confirm")

        def test_no_button(self, confirm_clear_db):
            no_button = (
                confirm_clear_db.by(name=UserCardsPage.no_button["title_en"])
                .find()
                .window_text()
            )
            check.equal(no_button, "No")

        def test_yes_button(self, confirm_clear_db):
            yes_button = (
                confirm_clear_db.by(name=UserCardsPage.yes_button["title_en"])
                .find()
                .window_text()
            )
            check.equal(yes_button, "Yes")
