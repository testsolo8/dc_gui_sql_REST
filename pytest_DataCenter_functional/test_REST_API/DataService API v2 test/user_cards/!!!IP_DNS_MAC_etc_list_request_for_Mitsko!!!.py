# Standart libraries
import json

# Third party packages
from jsonschema import validate

# My packages
from tools.dc_api_with_token import DcApiWithToken

URL_TAIL = (
    "/api/v2/data_center/user_cards/contacts/network?userID=313&sortFields=LastActive DESC&selectFields="
    "AddressID, DNS, Address, AddressType, LastActive, PrincipalName, DisplayName, Domain, GroupName, _RowsCount,"
    " RowNum"
)


def test_status_code_200(dc_api: DcApiWithToken):
    r = dc_api.req_get(URL_TAIL)
    assert r.status_code == 200


def test_content_type(dc_api: DcApiWithToken):
    con_type = dc_api.req_get(URL_TAIL).headers["content-type"]
    assert con_type == "application/json; charset=utf-8"


def test_response_time(dc_api: DcApiWithToken):
    resp_time = dc_api.req_get(URL_TAIL).elapsed.total_seconds()
    assert resp_time <= 30


def test_sort_by_addressID_DESC(dc_api: DcApiWithToken):
    data_dict = dc_api.req_get(URL_TAIL).json()
    data_str = json.dumps(data_dict)
    data_dict = json.loads(data_str)
    assert data_dict["data"][0]["address"] == 167772795
    assert data_dict["data"][0]["addressID"] == 10804
    assert data_dict["data"][0]["addressType"] == 1
    assert data_dict["data"][0]["dNS"] == "MSQ-PC-293.minsk.searchinform.net"
    assert data_dict["data"][0]["displayName"] == "Митько Максим"
    assert data_dict["data"][0]["domain"] == "minsk.searchinform.net"
    assert data_dict["data"][0]["groupName"] == "Минск"
    assert data_dict["data"][0]["lastActive"] is not None
    assert data_dict["data"][0]["principalName"] == "m.mitsko@minsk.searchinform.net"


def test_schema(dc_api: DcApiWithToken):
    schema = {
        "type": "object",
        "properties": {"data": {"type": "array"}},
        "required": ["data"],
    }
    resp = dc_api.req_get(URL_TAIL).json()
    validate(resp, schema=schema)
