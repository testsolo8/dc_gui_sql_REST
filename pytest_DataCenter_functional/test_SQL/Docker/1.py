# Standart libraries
import logging
import time

# Third party packages
import allure
import pyodbc
import pytest
import pytest_check as check
import sqlalchemy_utils
from pywinauto import Application
from pywinauto.keyboard import send_keys
from sqlalchemy import create_engine, inspect

# My packages
from DataCenter.buttons import ActiveDirectoryPage
from pytest_DataCenter_functional.test_SQL.sql_tools import Docker, delete_mssql_DB
from pytest_DataCenter_functional.test_SQL.tables_templates import (
    dc_active_directory_mssql,
)

testdata = [
    ("192.168.1.12,1422", "sa", "Passw0rd", "DataCenter"),
    ("192.168.1.12,1419", "sa", "Passw0rd", "DataCenter"),
    ("192.168.1.12,1417", "sa", "Passw0rd", "DataCenter"),
]


# engine = create_engine(
#     f"mssql+pyodbc://sa:Passw0rd@192.168.166.44,1419/ActionsLog?driver=ODBC+Driver+17+for+SQL+Server"
# )
connectionStr = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    + f"SERVER=192.168.166.44,1422;DATABASE=master;UID=sa;PWD=Passw0rd"
)
with pyodbc.connect(connectionStr, autocommit=True) as cursor:
    sqlMask = f"SELECT NAME FROM sys.sysdatabases WHERE name LIKE 'ActionsLog'"
    rows = [row.NAME for row in cursor.execute(sqlMask).fetchall()]
