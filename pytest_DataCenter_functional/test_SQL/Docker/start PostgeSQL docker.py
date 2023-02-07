# My packages
from pytest_DataCenter_functional.test_SQL.sql_tools import Docker

Docker().start_postgresql()
Docker().start_postgresql_spec()
