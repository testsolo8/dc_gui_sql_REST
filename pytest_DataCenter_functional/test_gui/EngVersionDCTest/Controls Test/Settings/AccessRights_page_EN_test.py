# Standart libraries
import locale

# Third party packages
import allure
import pytest
import pytest_check as check
from pywinauto.keyboard import send_keys

# My packages
from DataCenter.buttons import AccessRightsPage


@pytest.fixture(scope="class")
def handle(start_test_page_en):
    send_keys("{VK_MENU down}Y3Y6{VK_MENU up}")
    app = start_test_page_en
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("ENG Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControlsEN
@pytest.mark.testGUI_EngVersionDCTest_ControlsTest_Settings
@allure.story("тест главного окна настройки прав доступа")
class TestAccessRightsPage:
    def test_cancel_button(self, handle):
        cancel_button = (
            handle.by(name=AccessRightsPage.cancel_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(cancel_button, "Cancel")

    def test_apply_button(self, handle):
        apply_button = (
            handle.by(name=AccessRightsPage.apply_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(apply_button, "Apply")

    def test_export_button(self, handle):
        export_button = (
            handle.by(name=AccessRightsPage.export_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(export_button, "Export")

    def test_import_button(self, handle):
        import_button = (
            handle.by(name=AccessRightsPage.import_button["title_en"])
            .find()
            .window_text()
        )
        check.equal(import_button, "Import")

    def test_select_button(self, handle):
        select_button = (
            handle.by(
                name=AccessRightsPage.select_button["title_en"],
                found_index=AccessRightsPage.select_button["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(select_button, "Select")

    def test_select_button2(self, handle):
        select_button2 = (
            handle.by(
                name=AccessRightsPage.select_button2["title_en"],
                found_index=AccessRightsPage.select_button2["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(select_button2, "Select")

    def test_enable_access_restrictions(self, handle):
        enable_access_restrictions = (
            handle.by(name=AccessRightsPage.enable_access_restrictions["title_en"])
            .find()
            .window_text()
        )
        check.equal(
            enable_access_restrictions,
            "Enable access restrictions to view search results and incidents",
        )

    def test_allow_access_to_following_servers(self, handle):
        allow_access_to_following_servers = (
            handle.by(
                name=AccessRightsPage.allow_access_to_following_servers["title_en"]
            )
            .find()
            .window_text()
        )
        check.equal(
            allow_access_to_following_servers, "Allow access to the following servers "
        )

    def test_allowed_to_all(self, handle):
        allowed_to_all = (
            handle.by(name=AccessRightsPage.allowed_to_all["title_en"])
            .find()
            .window_text()
        )
        check.equal(allowed_to_all, "Allowed to all")

    def test_including_unknown_users(self, handle):
        including_unknown_users = (
            handle.by(
                name=AccessRightsPage.including_unknown_users["title_en"],
                found_index=AccessRightsPage.including_unknown_users["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(including_unknown_users, "Including unknown users")

    def test_including_unknown_users2(self, handle):
        including_unknown_users2 = (
            handle.by(
                name=AccessRightsPage.including_unknown_users2["title_en"],
                found_index=AccessRightsPage.including_unknown_users2["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(including_unknown_users2, "Including unknown users")

    def test_data_sources(self, handle):
        data_sources = (
            handle.by(name=AccessRightsPage.data_sources["title_en"])
            .find()
            .window_text()
        )
        check.equal(data_sources, "Data sources")

    def test_select_data_sources_available_to_this_auditor(self, handle):
        select_data_sources_available_to_this_auditor = (
            handle.by(
                name=AccessRightsPage.select_data_sources_available_to_this_auditor[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            select_data_sources_available_to_this_auditor,
            "Select data sources available to this auditor",
        )

    def test_auditors(self, handle):
        auditors = (
            handle.by(name=AccessRightsPage.auditors["title_en"]).find().window_text()
        )
        check.equal(auditors, "Auditors")

    def test_select_security_officers_and_assign_them_role(self, handle):
        select_security_officers_and_assign_them_role = (
            handle.by(
                name=AccessRightsPage.select_security_officers_and_assign_them_role[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            select_security_officers_and_assign_them_role,
            "Select Security Officers and assign them a role",
        )

    def test_users_and_computers(self, handle):
        users_and_computers = (
            handle.by(name=AccessRightsPage.users_and_computers["title_en"])
            .find()
            .window_text()
        )
        check.equal(users_and_computers, "Users and computers")

    def test_users_and_computers_monitored_by_auditor(self, handle):
        users_and_computers_monitored_by_auditor = (
            handle.by(
                name=AccessRightsPage.users_and_computers_monitored_by_auditor[
                    "title_en"
                ]
            )
            .find()
            .window_text()
        )
        check.equal(
            users_and_computers_monitored_by_auditor,
            "Users and computers monitored by the auditor",
        )

    def test_role_edit(self, handle):
        role_edit = (
            handle.by(name=AccessRightsPage.role_edit["title_en"]).find().window_text()
        )
        check.equal(role_edit, "Role edit")

    def test_user_and_auditor(self, handle):
        user_and_auditor = (
            handle.by(name=AccessRightsPage.user_and_auditor["title_en"])
            .find()
            .window_text()
        )
        check.equal(user_and_auditor, "UserAndAuditor")

    # @pytest.mark.skip(reason="временно отключен из-за разности операционных систем ENG-RUS")
    def test_restrict_for_servers(self, handle):
        version = locale.getdefaultlocale()
        if version[0] == "ru_R":
            restrict_for_servers = (
                handle.by(name=AccessRightsPage.restrict_for_servers["title_en"])
                .find()
                .window_text()
            )
            check.equal(restrict_for_servers, "Ограничение по серверам отсутствует")

    def test_access_servers(self, handle):
        access_servers = (
            handle.by(name=AccessRightsPage.access_servers["title_en"])
            .find()
            .window_text()
        )
        check.equal(access_servers, "AccessServers")

    def test_allowed_to_selected(self, handle):
        allowed_to_selected = (
            handle.by(name=AccessRightsPage.allowed_to_selected["title_en"])
            .find()
            .window_text()
        )
        check.equal(allowed_to_selected, "Allowed to selected")

    def test_disallowed_to_selected(self, handle):
        disallowed_to_selected = (
            handle.by(name=AccessRightsPage.disallowed_to_selected["title_en"])
            .find()
            .window_text()
        )
        check.equal(disallowed_to_selected, "Disallowed to selected")

    def test_source_data(self, handle):
        source_data = (
            handle.by(name=AccessRightsPage.source_data["title_en"])
            .find()
            .window_text()
        )
        check.equal(source_data, "Source data")

    def test_source_data_select(self, handle):
        source_data_select = (
            handle.by(name=AccessRightsPage.source_data_select["title_en"])
            .find()
            .window_text()
        )
        check.equal(source_data_select, "Source data select")

    def test_iws(self, handle):
        iws = handle.by(name=AccessRightsPage.iws["title_en"]).find().window_text()
        check.equal(iws, "IWS")

    def test_local_files(self, handle):
        local_files = (
            handle.by(name=AccessRightsPage.local_files["title_en"])
            .find()
            .window_text()
        )
        check.equal(local_files, "Local files")

    def test_databases(self, handle):
        databases = (
            handle.by(name=AccessRightsPage.databases["title_en"]).find().window_text()
        )
        check.equal(databases, "DataBases")

    def test_sharepoint(self, handle):
        sharepoint = (
            handle.by(name=AccessRightsPage.sharepoint["title_en"]).find().window_text()
        )
        check.equal(sharepoint, "SharePoint")

    def test_cmis(self, handle):
        cmis = handle.by(name=AccessRightsPage.cmis["title_en"]).find().window_text()
        check.equal(cmis, "CMIS")

    def test_dropbox(self, handle):
        dropbox = (
            handle.by(name=AccessRightsPage.dropbox["title_en"]).find().window_text()
        )
        check.equal(dropbox, "DropBox")

    def test_yandexdisk(self, handle):
        yandexdisk = (
            handle.by(name=AccessRightsPage.yandexdisk["title_en"]).find().window_text()
        )
        check.equal(yandexdisk, "YandexDisk")

    def test_onedrive(self, handle):
        onedrive = (
            handle.by(name=AccessRightsPage.onedrive["title_en"]).find().window_text()
        )
        check.equal(onedrive, "OneDrive")

    def test_mail(self, handle):
        mail = handle.by(name=AccessRightsPage.mail["title_en"]).find().window_text()
        check.equal(mail, "Mail")

    def test_im(self, handle):
        im = handle.by(name=AccessRightsPage.im["title_en"]).find().window_text()
        check.equal(im, "IM")

    def test_lync(self, handle):
        lync = handle.by(name=AccessRightsPage.lync["title_en"]).find().window_text()
        check.equal(lync, "Lync")

    def test_viber(self, handle):
        viber = handle.by(name=AccessRightsPage.viber["title_en"]).find().window_text()
        check.equal(viber, "Viber")

    def test_telegram(self, handle):
        telegram = (
            handle.by(name=AccessRightsPage.telegram["title_en"]).find().window_text()
        )
        check.equal(telegram, "Telegram")

    def test_whatsapp(self, handle):
        whatsapp = (
            handle.by(name=AccessRightsPage.whatsapp["title_en"]).find().window_text()
        )
        check.equal(whatsapp, "WhatsApp")

    def test_skype(self, handle):
        skype = handle.by(name=AccessRightsPage.skype["title_en"]).find().window_text()
        check.equal(skype, "Skype")

    def test_device(self, handle):
        device = (
            handle.by(name=AccessRightsPage.device["title_en"]).find().window_text()
        )
        check.equal(device, "Device")

    def test_ftp(self, handle):
        ftp = handle.by(name=AccessRightsPage.ftp["title_en"]).find().window_text()
        check.equal(ftp, "FTP")

    def test_print(self, handle):
        print = handle.by(name=AccessRightsPage.print["title_en"]).find().window_text()
        check.equal(print, "Print")

    def test_cloud(self, handle):
        cloud = handle.by(name=AccessRightsPage.cloud["title_en"]).find().window_text()
        check.equal(cloud, "Cloud")

    def test_http(self, handle):
        http = handle.by(name=AccessRightsPage.http["title_en"]).find().window_text()
        check.equal(http, "HTTP")

    def test_microphone_index(self, handle):
        microphone_index = (
            handle.by(name=AccessRightsPage.microphone_index["title_en"])
            .find()
            .window_text()
        )
        check.equal(microphone_index, "Microphone (index)")

    def test_keylogger_index(self, handle):
        keylogger_index = (
            handle.by(name=AccessRightsPage.keylogger_index["title_en"])
            .find()
            .window_text()
        )
        check.equal(keylogger_index, "Keylogger (index)")

    def test_actionslog(self, handle):
        actionslog = (
            handle.by(name=AccessRightsPage.actionslog["title_en"]).find().window_text()
        )
        check.equal(actionslog, "ActionsLog")

    def test_microphone(self, handle):
        microphone = (
            handle.by(name=AccessRightsPage.microphone["title_en"]).find().window_text()
        )
        check.equal(microphone, "Microphone")

    def test_keyLogger(self, handle):
        keyLogger = (
            handle.by(name=AccessRightsPage.keyLogger["title_en"]).find().window_text()
        )
        check.equal(keyLogger, "KeyLogger")

    def test_monitor(self, handle):
        monitor = (
            handle.by(name=AccessRightsPage.monitor["title_en"]).find().window_text()
        )
        check.equal(monitor, "Monitor")

    def test_webcam(self, handle):
        webcam = (
            handle.by(name=AccessRightsPage.webcam["title_en"]).find().window_text()
        )
        check.equal(webcam, "WebCam")

    def test_deviceaudit(self, handle):
        deviceaudit = (
            handle.by(name=AccessRightsPage.deviceaudit["title_en"])
            .find()
            .window_text()
        )
        check.equal(deviceaudit, "DeviceAudit")

    def test_files(self, handle):
        files = handle.by(name=AccessRightsPage.files["title_en"]).find().window_text()
        check.equal(files, "Files")

    def test_program(self, handle):
        program = (
            handle.by(name=AccessRightsPage.program["title_en"]).find().window_text()
        )
        check.equal(program, "Program")

    def test_database_monitor(self, handle):
        database_monitor = (
            handle.by(name=AccessRightsPage.database_monitor["title_en"])
            .find()
            .window_text()
        )
        check.equal(database_monitor, "Database Monitor")

    def test_profilecenter(self, handle):
        profilecenter = (
            handle.by(name=AccessRightsPage.profilecenter["title_en"])
            .find()
            .window_text()
        )
        check.equal(profilecenter, "ProfileCenter")
