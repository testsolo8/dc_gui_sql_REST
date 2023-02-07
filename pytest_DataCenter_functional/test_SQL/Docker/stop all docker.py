# My packages
from pytest_DataCenter_functional.test_SQL.sql_tools import Docker

Docker().stop_mssql()
Docker().stop_postgresql()
Docker().stop_mssql_spec()
Docker().stop_postgresql_spec()
