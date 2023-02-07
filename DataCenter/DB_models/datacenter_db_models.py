from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import BOOLEAN, DATETIME, INT, NVARCHAR, SMALLINT

Base = declarative_base()


class AD_ObjectAttributes(Base):
    """Вычитанные доменные атрибуты"""

    __tablename__ = "ad_objectattributes"

    obj_id = Column(INT, primary_key=True, autoincrement="auto")
    objectclass = Column(NVARCHAR(512), nullable=False)
    objectcategory = Column(NVARCHAR(1024), nullable=False)
    objectsid = Column(NVARCHAR(64), nullable=False)
    cn = Column(NVARCHAR(512), nullable=False)
    ou = Column(NVARCHAR(512), nullable=False)
    whencreated = Column(DATETIME, nullable=False)
    whenchanged = Column(DATETIME, nullable=False)
    adspath = Column(NVARCHAR(1024), nullable=False)
    dnshostname = Column(NVARCHAR(256), nullable=False)
    operatingsystem = Column(NVARCHAR(256), nullable=False)
    operatingsystemversion = Column(NVARCHAR(128), nullable=False)
    operatingsystemservicepack = Column(NVARCHAR(256), nullable=False)
    pwdlastset = Column(DATETIME, nullable=False)
    badpwdcount = Column(INT, nullable=False)
    badpasswordtime = Column(DATETIME, nullable=False)
    localpolicyflags = Column(INT, nullable=False)
    accountexpires = Column(DATETIME, nullable=False)
    lastlogoff = Column(DATETIME, nullable=False)
    lastlogon = Column(DATETIME, nullable=False)
    logoncount = Column(INT, nullable=False)
    samaccountname = Column(NVARCHAR(1024), nullable=False)
    userprincipalname = Column(NVARCHAR(1024), nullable=False)
    mail = Column(NVARCHAR(256), nullable=False)
    othermailbox = Column(NVARCHAR(1024), nullable=False)
    proxyaddresses = Column(NVARCHAR(1024), nullable=False)
    grouptype = Column(NVARCHAR(16), nullable=False)


class ADObjectsList(Base):
    """Вычитанные доменные атрибуты"""

    __tablename__ = "adobjectslist"

    obj_id = Column(INT, primary_key=True, autoincrement="auto")
    domain_id = Column(INT, nullable=True)
    obj_guid = Column(NVARCHAR, nullable=True)
    obj_type = Column(SMALLINT, nullable=True)
    obj_name = Column(NVARCHAR(512), nullable=True)
    obj_displayname = Column(NVARCHAR(256), nullable=True)
    obj_enabled = Column(BOOLEAN, nullable=True)
    enableddate = Column(DATETIME, nullable=True)
    disableddate = Column(DATETIME, nullable=False)
    account_enabled = Column(BOOLEAN, nullable=True)
    comment = Column(NVARCHAR(512), nullable=False)
