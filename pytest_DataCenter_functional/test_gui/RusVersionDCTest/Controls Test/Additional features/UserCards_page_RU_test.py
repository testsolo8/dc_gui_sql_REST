# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import UserCardsPage


@pytest.fixture(scope="class")
def handle(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y06{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.fixture(scope="class")
def confirm_clear_db(start_fast_test_page_ru):
    send_keys("{VK_MENU down}Y4Y06{VK_MENU up}")
    app = start_fast_test_page_ru
    handle = app.window(name_re="DataCenter*")
    handle.by(name=UserCardsPage.clear_database["title_ru"]).click()
    yield handle
    send_keys("%{F4}")


@pytest.mark.order(1)
@allure.epic("RUS Controls Test")
@allure.feature("Additional features")
@pytest.mark.testGUI_TestControlsRU
@pytest.mark.testGUI_RusVersionDCTest_ControlsTest_Additionalfeatures
class TestUserCardsPage:
    @allure.story("тест главного окна UserCards")
    class TestUserCardsMainPage:
        def test_cancel_button(self, handle):
            cancel_button = (
                handle.by(name=UserCardsPage.cancel_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(cancel_button, "Отменить")

        def test_apply_button(self, handle):
            apply_button = (
                handle.by(name=UserCardsPage.apply_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(apply_button, "Применить")

        def test_clear_database(self, handle):
            clear_database = (
                handle.by(name=UserCardsPage.clear_database["title_ru"])
                .find()
                .window_text()
            )
            check.equal(clear_database, "Очистить базу данных")

        def test_configure_connection_to_the_selected_server(self, handle):
            configure_connection_to_the_selected_server = (
                handle.by(
                    name=UserCardsPage.configure_connection_to_the_selected_server[
                        "title_ru"
                    ]
                )
                .find()
                .window_text()
            )
            check.equal(
                configure_connection_to_the_selected_server,
                "Настроить подключение к выбранному серверу",
            )

        def test_stop(self, handle):
            stop = handle.by(name=UserCardsPage.stop["title_ru"]).find().window_text()
            check.equal(stop, "Остановить")

        def test_only_from_the_selected_indexes(self, handle):
            only_from_the_selected_indexes = (
                handle.by(name=UserCardsPage.only_from_the_selected_indexes["title_ru"])
                .find()
                .window_text()
            )
            check.equal(only_from_the_selected_indexes, "Только из выбранных индексов")

        def test_all_available_indexes_from_the_list(self, handle):
            all_available_indexes_from_the_list = (
                handle.by(
                    name=UserCardsPage.all_available_indexes_from_the_list["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                all_available_indexes_from_the_list, "Все доступные индексы из списка"
            )

        def test_user_cards_fetcher(self, handle):
            user_cards_fetcher = (
                handle.by(name=UserCardsPage.user_cards_fetcher["title_ru"])
                .find()
                .window_text()
            )
            check.equal(user_cards_fetcher, "UserCardsFetcher")

        def test_create_card_for_external_contacts(self, handle):
            create_card_for_external_contacts = (
                handle.by(
                    name=UserCardsPage.create_card_for_external_contacts["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                create_card_for_external_contacts,
                "Создавать карточку для внешних контактов",
            )

        def test_import_data_starting_from_the_date(self, handle):
            import_data_starting_from_the_date = (
                handle.by(
                    name=UserCardsPage.import_data_starting_from_the_date["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                import_data_starting_from_the_date,
                "Импортировать данные начиная с даты",
            )

        def test_indexes_reading_and_synchronization(self, handle):
            indexes_reading_and_synchronization = (
                handle.by(
                    name=UserCardsPage.indexes_reading_and_synchronization["title_ru"]
                )
                .find()
                .window_text()
            )
            check.equal(
                indexes_reading_and_synchronization, "Вычитка индексов и синхронизация"
            )

        def test_sources(self, handle):
            sources = (
                handle.by(name=UserCardsPage.sources["title_ru"]).find().window_text()
            )
            check.equal(
                sources,
                "Mail;HTTP IM;Lync;Viber;Telegram;Skype;WhatsApp;ProgramController;KeyLogger",
            )

    @allure.story("тест окна подтверждения очистки БД UserCards")
    class TestConfirmClearDBWindow:
        def test_confirm(self, confirm_clear_db):
            confirm = (
                confirm_clear_db.by(name=UserCardsPage.confirm["title_ru"])
                .find()
                .window_text()
            )
            check.equal(confirm, "Подтверждение")

        def test_no_button(self, confirm_clear_db):
            no_button = (
                confirm_clear_db.by(name=UserCardsPage.no_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(no_button, "Нет")

        def test_yes_button(self, confirm_clear_db):
            yes_button = (
                confirm_clear_db.by(name=UserCardsPage.yes_button["title_ru"])
                .find()
                .window_text()
            )
            check.equal(yes_button, "Да")
