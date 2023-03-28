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
def handle(start_test_page):
    send_keys("{VK_MENU down}Y3Y6{VK_MENU up}")
    app = start_test_page
    handle = app.window(name_re="DataCenter*")
    yield handle


@pytest.mark.order(1)
@allure.epic("Controls Test")
@allure.feature("Settings")
@pytest.mark.testGUI_TestControls
@pytest.mark.testGUI_DCTest_ControlsTest_Settings
@allure.story("тест главного окна настройки прав доступа")
class TestAccessRightsPage:
    def test_cancel_button(self, handle, title_key):
        cancel_button = handle.by(name=AccessRightsPage.cancel_button[title_key]).find().window_text()
        check.equal(cancel_button, AccessRightsPage.cancel_button[title_key])

    def test_apply_button(self, handle, title_key):
        apply_button = handle.by(name=AccessRightsPage.apply_button[title_key]).find().window_text()
        check.equal(apply_button, AccessRightsPage.apply_button[title_key])

    def test_export_button(self, handle, title_key):
        export_button = handle.by(name=AccessRightsPage.export_button[title_key]).find().window_text()
        check.equal(export_button, AccessRightsPage.export_button[title_key])

    def test_import_button(self, handle, title_key):
        import_button = handle.by(name=AccessRightsPage.import_button[title_key]).find().window_text()
        check.equal(import_button, AccessRightsPage.import_button[title_key])

    def test_select_button(self, handle, title_key):
        select_button = (
            handle.by(
                name=AccessRightsPage.select_button[title_key],
                found_index=AccessRightsPage.select_button["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(select_button, AccessRightsPage.select_button[title_key])

    def test_select_button2(self, handle, title_key):
        select_button2 = (
            handle.by(
                name=AccessRightsPage.select_button2[title_key],
                found_index=AccessRightsPage.select_button2["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(select_button2, AccessRightsPage.select_button2[title_key])

    def test_enable_access_restrictions(self, handle, title_key):
        enable_access_restrictions = (
            handle.by(name=AccessRightsPage.enable_access_restrictions[title_key]).find().window_text()
        )
        check.equal(
            enable_access_restrictions,
            AccessRightsPage.enable_access_restrictions[title_key],
        )

    def test_allow_access_to_following_servers(self, handle, title_key):
        allow_access_to_following_servers = (
            handle.by(name=AccessRightsPage.allow_access_to_following_servers[title_key]).find().window_text()
        )
        check.equal(allow_access_to_following_servers, AccessRightsPage.allow_access_to_following_servers[title_key])

    def test_allowed_to_all(self, handle, title_key):
        allowed_to_all = handle.by(name=AccessRightsPage.allowed_to_all[title_key]).find().window_text()
        check.equal(allowed_to_all, AccessRightsPage.allowed_to_all[title_key])

    def test_including_unknown_users(self, handle, title_key):
        including_unknown_users = (
            handle.by(
                name=AccessRightsPage.including_unknown_users[title_key],
                found_index=AccessRightsPage.including_unknown_users["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(including_unknown_users, AccessRightsPage.including_unknown_users[title_key])

    def test_including_unknown_users2(self, handle, title_key):
        including_unknown_users2 = (
            handle.by(
                name=AccessRightsPage.including_unknown_users2[title_key],
                found_index=AccessRightsPage.including_unknown_users2["found_index"],
            )
            .find()
            .window_text()
        )
        check.equal(including_unknown_users2, AccessRightsPage.including_unknown_users2[title_key])

    def test_data_sources(self, handle, title_key):
        data_sources = handle.by(name=AccessRightsPage.data_sources[title_key]).find().window_text()
        check.equal(data_sources, AccessRightsPage.data_sources[title_key])

    def test_select_data_sources_available_to_this_auditor(self, handle, title_key):
        select_data_sources_available_to_this_auditor = (
            handle.by(name=AccessRightsPage.select_data_sources_available_to_this_auditor[title_key])
            .find()
            .window_text()
        )
        check.equal(
            select_data_sources_available_to_this_auditor,
            AccessRightsPage.select_data_sources_available_to_this_auditor[title_key],
        )

    def test_auditors(self, handle, title_key):
        auditors = handle.by(name=AccessRightsPage.auditors[title_key]).find().window_text()
        check.equal(auditors, AccessRightsPage.auditors[title_key])

    def test_select_security_officers_and_assign_them_role(self, handle, title_key):
        select_security_officers_and_assign_them_role = (
            handle.by(name=AccessRightsPage.select_security_officers_and_assign_them_role[title_key])
            .find()
            .window_text()
        )
        check.equal(
            select_security_officers_and_assign_them_role,
            AccessRightsPage.select_security_officers_and_assign_them_role[title_key],
        )

    def test_users_and_computers(self, handle, title_key):
        users_and_computers = handle.by(name=AccessRightsPage.users_and_computers[title_key]).find().window_text()
        check.equal(users_and_computers, AccessRightsPage.users_and_computers[title_key])

    def test_users_and_computers_monitored_by_auditor(self, handle, title_key):
        users_and_computers_monitored_by_auditor = (
            handle.by(name=AccessRightsPage.users_and_computers_monitored_by_auditor[title_key]).find().window_text()
        )
        check.equal(
            users_and_computers_monitored_by_auditor,
            AccessRightsPage.users_and_computers_monitored_by_auditor[title_key],
        )

    def test_role_edit(self, handle, title_key):
        role_edit = handle.by(name=AccessRightsPage.role_edit[title_key]).find().window_text()
        check.equal(role_edit, AccessRightsPage.role_edit[title_key])

    def test_user_and_auditor(self, handle, title_key):
        user_and_auditor = handle.by(name=AccessRightsPage.user_and_auditor[title_key]).find().window_text()
        check.equal(user_and_auditor, AccessRightsPage.user_and_auditor[title_key])

    # @pytest.mark.skip(reason="временно отключен из-за разности операционных систем ENG-RUS")
    def test_restrict_for_servers(self, handle, title_key):
        version = locale.getdefaultlocale()
        if version[0] == "ru_R":
            restrict_for_servers = (
                handle.by(name=AccessRightsPage.restrict_for_servers[title_key]).find().window_text()
            )
            check.equal(restrict_for_servers, AccessRightsPage.restrict_for_servers[title_key])

    def test_access_servers(self, handle, title_key):
        access_servers = handle.by(name=AccessRightsPage.access_servers[title_key]).find().window_text()
        check.equal(access_servers, AccessRightsPage.access_servers[title_key])

    def test_allowed_to_selected(self, handle, title_key):
        allowed_to_selected = handle.by(name=AccessRightsPage.allowed_to_selected[title_key]).find().window_text()
        check.equal(allowed_to_selected, AccessRightsPage.allowed_to_selected[title_key])

    def test_disallowed_to_selected(self, handle, title_key):
        disallowed_to_selected = (
            handle.by(name=AccessRightsPage.disallowed_to_selected[title_key]).find().window_text()
        )
        check.equal(disallowed_to_selected, AccessRightsPage.disallowed_to_selected[title_key])

    def test_source_data(self, handle, title_key):
        source_data = handle.by(name=AccessRightsPage.source_data[title_key]).find().window_text()
        check.equal(source_data, AccessRightsPage.source_data[title_key])

    def test_source_data_select(self, handle, title_key):
        source_data_select = handle.by(name=AccessRightsPage.source_data_select[title_key]).find().window_text()
        check.equal(source_data_select, AccessRightsPage.source_data_select[title_key])

    def test_iws(self, handle, title_key):
        iws = handle.by(name=AccessRightsPage.iws[title_key]).find().window_text()
        check.equal(iws, AccessRightsPage.iws[title_key])

    def test_local_files(self, handle, title_key):
        local_files = handle.by(name=AccessRightsPage.local_files[title_key]).find().window_text()
        check.equal(local_files, AccessRightsPage.local_files[title_key])

    def test_databases(self, handle, title_key):
        databases = handle.by(name=AccessRightsPage.databases[title_key]).find().window_text()
        check.equal(databases, AccessRightsPage.databases[title_key])

    def test_sharepoint(self, handle, title_key):
        sharepoint = handle.by(name=AccessRightsPage.sharepoint[title_key]).find().window_text()
        check.equal(sharepoint, AccessRightsPage.sharepoint[title_key])

    def test_cmis(self, handle, title_key):
        cmis = handle.by(name=AccessRightsPage.cmis[title_key]).find().window_text()
        check.equal(cmis, AccessRightsPage.cmis[title_key])

    def test_dropbox(self, handle, title_key):
        dropbox = handle.by(name=AccessRightsPage.dropbox[title_key]).find().window_text()
        check.equal(dropbox, AccessRightsPage.dropbox[title_key])

    def test_yandexdisk(self, handle, title_key):
        yandexdisk = handle.by(name=AccessRightsPage.yandexdisk[title_key]).find().window_text()
        check.equal(yandexdisk, AccessRightsPage.yandexdisk[title_key])

    def test_onedrive(self, handle, title_key):
        onedrive = handle.by(name=AccessRightsPage.onedrive[title_key]).find().window_text()
        check.equal(onedrive, AccessRightsPage.onedrive[title_key])

    def test_mail(self, handle, title_key):
        mail = handle.by(name=AccessRightsPage.mail[title_key]).find().window_text()
        check.equal(mail, AccessRightsPage.mail[title_key])

    def test_im(self, handle, title_key):
        im = handle.by(name=AccessRightsPage.im[title_key]).find().window_text()
        check.equal(im, AccessRightsPage.im[title_key])

    def test_lync(self, handle, title_key):
        lync = handle.by(name=AccessRightsPage.lync[title_key]).find().window_text()
        check.equal(lync, AccessRightsPage.lync[title_key])

    def test_viber(self, handle, title_key):
        viber = handle.by(name=AccessRightsPage.viber[title_key]).find().window_text()
        check.equal(viber, AccessRightsPage.viber[title_key])

    def test_telegram(self, handle, title_key):
        telegram = handle.by(name=AccessRightsPage.telegram[title_key]).find().window_text()
        check.equal(telegram, AccessRightsPage.telegram[title_key])

    def test_whatsapp(self, handle, title_key):
        whatsapp = handle.by(name=AccessRightsPage.whatsapp[title_key]).find().window_text()
        check.equal(whatsapp, AccessRightsPage.whatsapp[title_key])

    def test_skype(self, handle, title_key):
        skype = handle.by(name=AccessRightsPage.skype[title_key]).find().window_text()
        check.equal(skype, AccessRightsPage.skype[title_key])

    def test_device(self, handle, title_key):
        device = handle.by(name=AccessRightsPage.device[title_key]).find().window_text()
        check.equal(device, AccessRightsPage.device[title_key])

    def test_ftp(self, handle, title_key):
        ftp = handle.by(name=AccessRightsPage.ftp[title_key]).find().window_text()
        check.equal(ftp, AccessRightsPage.ftp[title_key])

    def test_print(self, handle, title_key):
        print = handle.by(name=AccessRightsPage.print[title_key]).find().window_text()
        check.equal(print, AccessRightsPage.print[title_key])

    def test_cloud(self, handle, title_key):
        cloud = handle.by(name=AccessRightsPage.cloud[title_key]).find().window_text()
        check.equal(cloud, AccessRightsPage.cloud[title_key])

    def test_http(self, handle, title_key):
        http = handle.by(name=AccessRightsPage.http[title_key]).find().window_text()
        check.equal(http, AccessRightsPage.http[title_key])

    def test_microphone_index(self, handle, title_key):
        microphone_index = handle.by(name=AccessRightsPage.microphone_index[title_key]).find().window_text()
        check.equal(microphone_index, AccessRightsPage.microphone_index[title_key])

    def test_keylogger_index(self, handle, title_key):
        keylogger_index = handle.by(name=AccessRightsPage.keylogger_index[title_key]).find().window_text()
        check.equal(keylogger_index, AccessRightsPage.keylogger_index[title_key])

    def test_actionslog(self, handle, title_key):
        actionslog = handle.by(name=AccessRightsPage.actionslog[title_key]).find().window_text()
        check.equal(actionslog, AccessRightsPage.actionslog[title_key])

    def test_microphone(self, handle, title_key):
        microphone = handle.by(name=AccessRightsPage.microphone[title_key]).find().window_text()
        check.equal(microphone, AccessRightsPage.microphone[title_key])

    def test_keyLogger(self, handle, title_key):
        keyLogger = handle.by(name=AccessRightsPage.keyLogger[title_key]).find().window_text()
        check.equal(keyLogger, AccessRightsPage.keyLogger[title_key])

    def test_monitor(self, handle, title_key):
        monitor = handle.by(name=AccessRightsPage.monitor[title_key]).find().window_text()
        check.equal(monitor, AccessRightsPage.monitor[title_key])

    def test_webcam(self, handle, title_key):
        webcam = handle.by(name=AccessRightsPage.webcam[title_key]).find().window_text()
        check.equal(webcam, AccessRightsPage.webcam[title_key])

    def test_deviceaudit(self, handle, title_key):
        deviceaudit = handle.by(name=AccessRightsPage.deviceaudit[title_key]).find().window_text()
        check.equal(deviceaudit, AccessRightsPage.deviceaudit[title_key])

    def test_files(self, handle, title_key):
        files = handle.by(name=AccessRightsPage.files[title_key]).find().window_text()
        check.equal(files, AccessRightsPage.files[title_key])

    def test_program(self, handle, title_key):
        program = handle.by(name=AccessRightsPage.program[title_key]).find().window_text()
        check.equal(program, AccessRightsPage.program[title_key])

    def test_database_monitor(self, handle, title_key):
        database_monitor = handle.by(name=AccessRightsPage.database_monitor[title_key]).find().window_text()
        check.equal(database_monitor, AccessRightsPage.database_monitor[title_key])

    def test_profilecenter(self, handle, title_key):
        profilecenter = handle.by(name=AccessRightsPage.profilecenter[title_key]).find().window_text()
        check.equal(profilecenter, AccessRightsPage.profilecenter[title_key])
