# Third party packages
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SchemaModelsRESTAPIV2:
    class APIVersion(BaseModel):
        MinSupported: StrictInt
        MaxSupported: StrictInt

    class AuditorList(BaseModel):
        UPN: StrictStr
        SID: StrictStr
        mails: list[StrictStr]
        Enabled: StrictBool
        DisplayName: StrictStr
        GUID: StrictStr

    class DCServerVersion(BaseModel):
        Version: StrictStr

    class DefaultDatabaseInfo(BaseModel):
        DefaultPG: list[StrictStr]
        DefaultMSSQL: list[StrictStr]

    class DomainList(BaseModel):
        LastSync: StrictInt
        Domain: StrictStr
        GUID: StrictStr

    class ConnectionParametersToDCserver(BaseModel):
        class ConnectionPorts(BaseModel):
            APIv3: StrictInt
            SIProxyDC: StrictInt
            UserCardDS: StrictInt

        Ports: ConnectionPorts
        UID: StrictStr
        DBParams: StrictStr = None
        HostName: StrictStr
        Version: StrictStr

    class ConnectionParametersTo_RC_OR_WA_server(BaseModel):
        UID: StrictStr
        DNSHostName: StrictStr
        DBParams: StrictStr = None
        HostName: StrictStr
        Port: StrictInt
        Version: StrictStr

    class ObjectsList(BaseModel):
        UPN: StrictStr = None
        SID: StrictStr
        DisplayName: StrictStr
        Name: StrictStr = None
        GUID: StrictStr
        ObjectType: StrictStr

    class ProxyStatus(BaseModel):
        Enabled: StrictBool

    class GlobalRightsSettings(BaseModel):
        AccessRightsEnabled: StrictBool
        PasswordControllerEnabled: StrictBool = None

    class LogoForReports(BaseModel):
        CompanyName: StrictStr
        ViewLogo: StrictBool
        ViewIcon: StrictBool

    class ESNSLicensingSettings(BaseModel):
        class PasswordLicense(BaseModel):
            Expire_Date: StrictInt
            UniqueID: StrictStr
            LicensesCount: StrictInt

        class MicrophoneToText(BaseModel):
            Expire_Date: StrictInt
            UniqueID: StrictStr
            LicensesCount: StrictInt

        class ExternalAPILicense(BaseModel):
            Expire_Date: StrictInt
            UniqueID: StrictStr
            LicensesCount: StrictInt

        SearchInform_Licence: list
        PasswordLicense: PasswordLicense
        MicrophoneToText: MicrophoneToText
        SupportTo: StrictInt
        Contact_Person_EMail: StrictStr
        Licence_Groups: list
        ExternalAPILicense: ExternalAPILicense
        HardwareID: str

    class ListProfilingLicenses(BaseModel):
        class License(BaseModel):
            FreeCount: StrictInt
            ExpireDate: StrictInt
            Count: StrictInt

        License: License
        Accounts: list

    class MailNotificationSettings(BaseModel):
        class SearchServer(BaseModel):
            Enabled: StrictBool

        class Endpoint(BaseModel):
            Enabled: StrictBool

        class IntegrationSMTP(BaseModel):
            Enabled: StrictBool

        class IntegrationMail(BaseModel):
            Enabled: StrictBool

        class Network(BaseModel):
            Enabled: StrictBool

        SearchServer: SearchServer
        Endpoint: Endpoint
        IntegrationSMTP: IntegrationSMTP
        IntegrationMail: IntegrationMail
        Network: Network
        Enabled: StrictBool
        AddressTo: StrictStr
        LanguageID: StrictStr

    class RightsUserDiffParam(BaseModel):
        class FeatureRights(BaseModel):
            SS: dict
            NS: dict
            ES: dict
            DC: dict
            CA: dict
            AC: dict
            SIEM: dict

        class ProductRights(BaseModel):
            AllowedProducts: StrictInt

        class DataRights(BaseModel):
            ComputersList: list
            UsersList: list
            AccessMode: StrictInt

        featurerights: FeatureRights
        serverrights: list
        productrights: ProductRights
        datarights: DataRights

    class UsersList(BaseModel):
        UPN: StrictStr
        SID: StrictStr
        UserState: StrictInt
        DisplayName: StrictStr
        Name: StrictStr
        GUID: StrictStr


class SchemaModelsRESTAPIV3:
    class InformationPasswordExtAPILicense(BaseModel):
        Expire_Date: StrictInt
        Start_Date: StrictInt
        UniqueID: StrictStr
        LicensesCount: StrictInt

    class InformationAboutLocationSeaweedMaster(BaseModel):
        master: StrictStr

    class GetOperatingModeSelectedServerGroup(BaseModel):
        Mode: StrictInt


class SchemaModelsDataServiceAPIv2:
    class ResumeForUser(BaseModel):
        class jsonData(BaseModel):
            jsonData: StrictStr

        data: list[jsonData]

    class AccountListMessengersAndSocialNetworksForUser(BaseModel):
        accountID: StrictInt
        accountName: StrictStr
        accountTypeID: StrictInt
        contactTypeID: StrictInt
        displayName: StrictStr
        docID: StrictStr = None
        inHeader: StrictBool = None
        lastLogon: StrictInt = None
        signID: StrictStr = None

    class EmailListForUser(BaseModel):
        docID: StrictStr = None
        inHeader: StrictBool = None
        mailAddress: StrictStr
        mailID: StrictInt
        mailType: StrictInt
        signID: StrictStr = None

    class FileListForUser(BaseModel):
        createDate: StrictInt
        description: StrictStr
        fileID: StrictInt
        fileName: StrictStr

    class FullDataForUser(BaseModel):
        bigPhoto: StrictStr
        calendarID: StrictInt
        changedFields: StrictInt
        citizenship: StrictStr
        city: StrictStr
        color: StrictInt
        company: StrictStr
        concatList: StrictStr = None
        country: StrictStr
        countryCode: StrictInt
        customFields: StrictStr = None
        dateOfBirth: StrictInt
        department: StrictStr
        description: StrictStr
        displayName: StrictStr
        domainID: StrictInt
        endDate: StrictInt
        guid: StrictStr
        hasIntercept: StrictBool
        id: StrictInt
        isChangedPhoto: StrictBool
        maritalStatus: StrictInt
        numberOfChildren: StrictInt
        parentID: StrictInt = None
        personnelNumber: StrictStr
        position: StrictStr
        principalName: StrictStr
        region: StrictStr
        rowNum: StrictInt
        sex: StrictInt
        sid: StrictStr
        smallPhoto: StrictStr = None
        startDate: StrictInt
        state: StrictInt
        streetAddress: StrictStr
        type: StrictInt
        userType: StrictInt
        zipCode: StrictStr

    class ListUsersGroupsForWorkCalendarRules(BaseModel):
        calendarID: StrictInt
        childCount: StrictInt
        color: StrictInt
        concatList: StrictStr = None
        displayName: StrictStr
        exclude: StrictBool
        guid: StrictStr
        id: StrictInt
        isGroup: StrictInt
        principalName: StrictStr = None
        rowNum: StrictInt
        state: StrictInt
        type: StrictInt
        userType: StrictInt = None

    class ListWorkCalendarRules(BaseModel):
        calendarID: StrictInt
        checked: StrictBool
        jsonData: StrictStr
        name: StrictStr
        orderID: StrictInt

    class PhonesListForUser(BaseModel):
        docID: StrictStr
        inHeader: StrictBool = None
        phoneID: StrictInt
        phoneNumber: StrictStr
        phoneType: StrictInt
        signID: StrictStr

    class ProcedureForObtainingListContactsForMergedUsers(BaseModel):
        accountTypeID: StrictInt
        contactTypeID: StrictInt
        displayName: StrictStr
        userID: StrictInt

    class ListOfUserGroups(BaseModel):
        branch: StrictInt
        color: StrictInt
        displayName: StrictStr
        groupID: StrictInt
        inGroup: StrictBool
        parentID: StrictInt
        type: StrictInt

    class ResolveSIDForUser(BaseModel):
        inputName: StrictStr
        objectID: StrictInt
        sID: StrictStr
        isGroup: StrictInt

    class ProcedureForObtainingUPNByContact(BaseModel):
        childCount: StrictInt = None
        color: StrictInt
        concatList: StrictStr = None
        displayName: StrictStr
        guid: StrictStr
        id: StrictInt
        isGroup: StrictInt
        principalName: StrictStr
        state: StrictInt
        type: StrictInt
        userType: StrictInt

    class ListOfTasks(BaseModel):
        class Data(BaseModel):
            changeDateTime: StrictInt
            changeStateDateTime: StrictInt
            cntChildTasks: StrictInt
            cntEndChildTasks: StrictInt
            completeDateTime: StrictInt = None
            createDateTime: StrictInt
            createUserID: StrictInt
            description: StrictStr
            execUserID: StrictInt
            gossopkaID: StrictStr = None
            notes: StrictStr = None
            parentTaskID: StrictInt
            parentTaskNumber: StrictStr = None
            prefix: StrictStr
            priorityID: StrictInt
            rowNum: StrictInt
            rvisionID: StrictStr = None
            tagColor: StrictInt
            tagID: StrictInt
            tagName: StrictStr
            taskID: StrictInt
            taskName: StrictStr
            taskNumber: StrictStr
            taskStateID: StrictInt
            taskTypeID: StrictInt
            typeIconID: StrictInt
            typeName: StrictStr

        data: Data

        class Header(BaseModel):
            rowsCount: StrictInt

        header: Header

    class ListFilesOrFileContentsByTask(BaseModel):
        createDateTime: StrictInt
        description: StrictStr
        fileID: StrictInt
        fileName: StrictStr
        fileSize: StrictInt

    class AllCommentsOnTask(BaseModel):
        commentID: StrictInt
        createDateTime: StrictInt
        msg: StrictStr
        userID: StrictInt

    class ListOfUsersFilters(BaseModel):
        description: StrictStr
        filterID: StrictInt
        filterName: StrictStr
        value: StrictStr

    class DataFromTaskOnGossopka(BaseModel):
        data: StrictStr

    class ListOfIncidentsOrIncidentBodyByTask(BaseModel):
        class Data(BaseModel):
            attributes: StrictStr
            comment: StrictStr = None
            createDateTime: StrictInt
            incidentID: StrictInt
            incidentUDL: StrictStr
            productID: StrictInt
            rawBody: StrictStr
            rawName: StrictStr
            rowNum: StrictInt
            textBody: StrictStr

        data: Data

        class Header(BaseModel):
            rowsCount: StrictInt

        header: Header

    class ListOfPersonsInvolvedInIncidentOrTask(BaseModel):
        incidentID: StrictInt
        userID: StrictInt

    class ListOfTags(BaseModel):
        tagColor: StrictInt
        tagID: StrictInt
        tagName: StrictStr

    class TaskChangeHistory(BaseModel):
        changeDateTime: StrictInt
        changeStateDateTime: StrictInt = None
        completeDateTime: StrictInt = None
        createDateTime: StrictInt
        createUserID: StrictInt
        deleted: StrictBool
        description: StrictStr
        execUserID: StrictInt
        notes: StrictStr = None
        parentTaskID: StrictInt
        priorityID: StrictInt
        processDate: StrictInt
        tagID: StrictInt = None
        taskName: StrictStr
        taskNumber: StrictInt
        taskStateID: StrictInt
        taskTypeID: StrictInt

    class ListOfTaskTypes(BaseModel):
        description: StrictStr
        enumerator: StrictInt
        prefix: StrictStr
        typeID: StrictInt
        typeIconID: StrictInt
        typeName: StrictStr

    class ListOfWatchersForTask(BaseModel):
        userID: StrictInt


class SchemaModelsDCArchivingRESTAPI:
    class GettingListOfStoragesForBackups(BaseModel):
        Settings: StrictStr
        ID: StrictStr
        Path: StrictStr
        User: StrictStr = None
        Password: StrictStr = None
        Server: StrictStr
        AgentVersion: StrictStr
        AgentAPIVersion: StrictInt
        AgentAPIPort: StrictInt
        AgentNeedsUpdate: StrictBool
        Mode: StrictInt
        Limit: StrictInt

    class GettingListOfAllTasks(BaseModel):
        ID: StrictStr
        ShareID: StrictStr
        TypeID: StrictInt
        ActionID: StrictInt
        ErrorCount: StrictInt
        MaxErrorCount: StrictInt
        Server: StrictStr
        Source: StrictStr
        Backup: StrictStr
        BackupSize: StrictInt
        Date: StrictInt
        Protocol: StrictInt
        MinDocDate: StrictInt
        MaxDocDate: StrictInt
        BackupFile: StrictStr
        StiPath: StrictStr
        IndexName: StrictStr
        IndexPath: StrictStr

        class Progress(BaseModel):
            ProgressID: StrictInt
            Status: StrictInt
            Messages: list
            CompletedPercent: StrictInt

        Progress: Progress

    class GettingCurrentServiceConfiguration(BaseModel):
        MailServiceHost: StrictStr
        MailServicePort: StrictInt
        WorkerCount: StrictInt
        RemoteOperationTimeout: StrictInt
        DefaultDBAgentPort: StrictInt
