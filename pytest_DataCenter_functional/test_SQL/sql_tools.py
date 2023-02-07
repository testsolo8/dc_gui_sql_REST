# Standart libraries
import logging
import subprocess
import time
import traceback
from pathlib import Path

# Third party packages
import psycopg2
import pyautogui
import pyodbc
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from pywinauto import Application

# My packages
from DataCenter.buttons import ActiveDirectoryPage
from DataCenter.tools.get_project_root import get_project_root


class Docker:
    def start_mssql(self):
        subprocess.call(
            r"docker-compose --context sql -f "
            + str(
                Path(
                    get_project_root(),
                    "pytest_DataCenter_functional",
                    "test_SQL",
                    "MSSQL",
                    "mssql-docker-compose.yml",
                )
            )
            + " up -d"
        )

    def stop_mssql(self):
        subprocess.call(
            r"docker-compose --context sql -f "
            + str(
                Path(
                    get_project_root(),
                    "pytest_DataCenter_functional",
                    "test_SQL",
                    "MSSQL",
                    "mssql-docker-compose.yml",
                )
            )
            + " rm -s -f"
        )

    def start_mssql_spec(self):
        subprocess.call(
            r"docker-compose --context sql -f "
            + str(
                Path(
                    get_project_root(),
                    "pytest_DataCenter_functional",
                    "test_SQL",
                    "MSSQL",
                    "mssql-docker-compose-spec-symbol.yml",
                )
            )
            + " up -d"
        )

    def stop_mssql_spec(self):
        subprocess.call(
            r"docker-compose --context sql -f "
            + str(
                Path(
                    get_project_root(),
                    "pytest_DataCenter_functional",
                    "test_SQL",
                    "MSSQL",
                    "mssql-docker-compose-spec-symbol.yml",
                )
            )
            + " rm -s -f"
        )

    def start_postgresql(self):
        subprocess.call(
            r"docker-compose --context sql -f "
            + str(
                Path(
                    get_project_root(),
                    "pytest_DataCenter_functional",
                    "test_SQL",
                    "PostgreSQL",
                    "postgresql-docker-compose.yml",
                )
            )
            + " up -d"
        )

    def stop_postgresql(self):
        subprocess.call(
            r"docker-compose --context sql -f "
            + str(
                Path(
                    get_project_root(),
                    "pytest_DataCenter_functional",
                    "test_SQL",
                    "PostgreSQL",
                    "postgresql-docker-compose.yml",
                )
            )
            + " rm -s -f"
        )

    def start_postgresql_spec(self):
        subprocess.call(
            r"docker-compose --context sql -f "
            + str(
                Path(
                    get_project_root(),
                    "pytest_DataCenter_functional",
                    "test_SQL",
                    "PostgreSQL",
                    "postgresql-docker-compose-spec-symbol.yml",
                )
            )
            + " up -d"
        )

    def stop_postgresql_spec(self):
        subprocess.call(
            r"docker-compose --context sql -f "
            + str(
                Path(
                    get_project_root(),
                    "pytest_DataCenter_functional",
                    "test_SQL",
                    "PostgreSQL",
                    "postgresql-docker-compose-spec-symbol.yml",
                )
            )
            + " rm -s -f"
        )


def delete_mssql_DB(sqlAddr, sqlUser, sqlPass, dbName):
    connectionStr = (
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER=%s;DATABASE=master;UID=%s;PWD=%s"
        % (sqlAddr, sqlUser, sqlPass)
    )
    try:
        with pyodbc.connect(connectionStr, autocommit=True) as conn:
            if (
                dbName.find("%") != -1
            ):  # если в имени БД встречается %, то удалим БД по маске
                sqlMask = (
                    f"SELECT NAME FROM sys.sysdatabases WHERE name LIKE '{dbName}'"
                )
                cursor = conn.cursor().execute(sqlMask)
                dbToDelete = [row.NAME for row in cursor.fetchall()]
            else:
                dbToDelete = [dbName]
            for dbName in dbToDelete:
                sql = f"""
                        WHILE EXISTS(select NULL from sys.databases where name='{dbName}')
                        BEGIN
                            DECLARE @SQL varchar(max)
                            SELECT @SQL = COALESCE(@SQL,'') + 'Kill ' + Convert(varchar, SPId) + ';'
                            FROM MASTER..SysProcesses
                            WHERE DBId = DB_ID(N'{dbName}') AND SPId <> @@SPId
                            EXEC(@SQL)
                            DROP DATABASE [{dbName}]
                        END
                    """
                conn.cursor().execute(sql)
                cursor.close()
        return True
    except Exception as ex:
        logging.error(f"Exception on deleteDB: {ex}")
        logging.debug(traceback.format_exc())
        return False


def delete_postgres_DB(pgAddr, pgPort, pgUser, pgPass, dbName):
    try:
        conn = psycopg2.connect(
            host=pgAddr, port=pgPort, user=pgUser, password=pgPass, dbname="postgres"
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        pgMask = f"""
                        SELECT datname
                        FROM pg_database
                        WHERE datistemplate = false AND datname ILIKE '{dbName}';
                    """
        closeDBConn = f"""
                        SELECT pg_terminate_backend(pid)
                        FROM pg_stat_activity
                        WHERE datname ILIKE '{dbName}';
                """
        with conn.cursor() as cursor:
            cursor.execute(pgMask)
            dbToDelete = cursor.fetchall()
            dbToDelete = "".join(map(str, dbToDelete[0]))
            print(f"Бд для удаления: {dbToDelete}")
            if dbToDelete.islower():
                sql = f"DROP database {dbName};"
                conn.cursor().execute(closeDBConn)
                conn.cursor().execute(sql)
                print("удалило БД на PostgreSQL с именем в низком регистре")
            else:
                sql = f'DROP database "{dbName}";'
                conn.cursor().execute(closeDBConn)
                conn.cursor().execute(sql)
                print("удалило БД на PostgreSQL с именем в разном регистре")
        cursor.close()
        conn.close()
        return True
    except Exception as ex:
        logging.error(f"Exception on deleteDB: {ex}")
        logging.debug(traceback.format_exc())
        return False


def save_start_db_name(handle):
    handle.by(name=ActiveDirectoryPage.setup_connection_db["title_ru"]).click()
    app_win32 = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    handle_win32 = app_win32.window(name_re="Параметры подключения к SQL*")
    time.sleep(2)
    start_db_name = handle_win32.__getattribute__(
        "Использовать внутреннюю аутентификацию SQL ServerComboBox2"
    ).texts()
    handle_win32.close()
    return handle_win32, start_db_name


def return_start_db_data(uia_handle_type, win32_handle_type, start_db_name):
    uia_handle_type.by(name=ActiveDirectoryPage.setup_connection_db["title_ru"]).click()
    win32_handle_type.__getattribute__("ComboBox3").type_keys("m")
    time.sleep(2)
    win32_handle_type.__getattribute__("ComboBox2").type_keys("192.168.1.9")
    time.sleep(2)
    win32_handle_type.__getattribute__("Edit3").type_keys("sa")
    time.sleep(2)
    win32_handle_type.__getattribute__("Edit0").type_keys(
        "{VK_SHIFT down}" "p" "{VK_SHIFT up}" "assword1"
    )
    time.sleep(2)
    win32_handle_type.__getattribute__(
        "Использовать внутреннюю аутентификацию SQL ServerComboBox2"
    ).type_keys(start_db_name)
    time.sleep(2)
    win32_handle_type.__getattribute__("OKButton").click()
    time.sleep(10)
    uia_handle_type.by(name=ActiveDirectoryPage.apply_button["title_ru"]).click()


def add_domain(handle):
    app_win32 = Application(backend="win32").connect(
        path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
    )
    add_domain_button = pyautogui.locateOnScreen(
        str(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "ScreensForTest",
                "add_domain",
                "AddDomainButton.png",
            )
        )
    )
    add_domain_button_center = pyautogui.center(add_domain_button)
    pyautogui.click(add_domain_button_center)
    time.sleep(1)
    handle_for_create_domain_win32 = app_win32.window(name="Добавить домен")
    handle_for_create_domain_win32.__getattribute__("ComboBox2").type_keys(
        "autotest.lan"
    )  # имя домена
    handle_for_create_domain_win32.__getattribute__("Edit6").type_keys(
        "администратор"
    )  # логин к домену
    handle_for_create_domain_win32.__getattribute__("Edit5").type_keys(
        "{VK_SHIFT down}" "p" "{VK_SHIFT up}" "assword1"
    )  # пароль к домену
    time.sleep(2)
    handle_for_create_domain_win32.__getattribute__("OK").click()
    time.sleep(2)
    handle.by(name=ActiveDirectoryPage.apply_button["title_ru"]).click()
    return app_win32


def delete_domain(app_win32, handle):
    handle.by(name="autotest.lan=-1").click_input()
    time.sleep(1)
    delete_domain_button = pyautogui.locateOnScreen(
        str(
            Path(
                get_project_root(),
                "pytest_DataCenter_functional",
                "test_SQL",
                "ScreensForTest",
                "add_domain",
                "DeleteDomainButton.png",
            )
        )
    )
    delete_domain_button_center = pyautogui.center(delete_domain_button)
    pyautogui.click(delete_domain_button_center)
    time.sleep(3)
    handle_win32 = app_win32.window(name="Подтверждение")
    time.sleep(1)
    handle_win32.__getattribute__("Да").click()
    time.sleep(1)
    handle.by(name=ActiveDirectoryPage.apply_button["title_ru"]).click()
