"""Mock responses for alert queries."""

GET_ALERT_RESP = {
    "org_key": "ABCD1234",
    "alert_url": "https://defense.conferdeploy.net/alerts?s[c][query_string]=id:52fa009d-e2d1-4118-8a8d-04f521ae66aa&orgKey=ABCD1234",
    "id": "12ab345cd6-e2d1-4118-8a8d-04f521ae66aa",
    "type": "WATCHLIST",
    "backend_timestamp": "2023-04-14T21:30:40.570Z",
    "user_update_timestamp": None,
    "backend_update_timestamp": "2023-04-14T21:30:40.570Z",
    "detection_timestamp": "2023-04-14T21:27:14.719Z",
    "first_event_timestamp": "2023-04-14T21:21:42.193Z",
    "last_event_timestamp": "2023-04-14T21:21:42.193Z",
    "severity": 8,
    "reason": "Process infdefaultinstall.exe was detected by the report \"Defense Evasion - Signed Binary Proxy Execution - InfDefaultInstall\" in 6 watchlists",
    "reason_code": "05696200-88e6-3691-a1e3-8d9a64dbc24e:7828aec8-8502-3a43-ae68-41b5050dab5b",
    "threat_id": "0569620088E6669121E38D9A64DBC24E",
    "primary_event_id": "-7RlZFHcSGWKSrF55B_4Ig-0",
    "policy_applied": "NOT_APPLIED",
    "run_state": "RAN",
    "sensor_action": "ALLOW",
    "workflow": {
        "change_timestamp": "2023-04-14T21:30:40.570Z",
        "changed_by_type": "SYSTEM",
        "changed_by": "ALERT_CREATION",
        "closure_reason": "NO_REASON",
        "status": "OPEN"
    },
    "determination": None,
    "tags": [
        "tag1",
        "tag2"
    ],
    "alert_notes_present": False,
    "threat_notes_present": False,
    "is_updated": False,
    "device_id": 18118174,
    "device_name": "pscr-test-01-1677785028.620244-9",
    "device_uem_id": "",
    "device_target_value": "LOW",
    "device_policy": "123abcde-c21b-4d64-9e3e-53595ef9c7af",
    "device_policy_id": 1234567,
    "device_os": "WINDOWS",
    "device_os_version": "Windows 10 x64 SP: 1",
    "device_username": "demouser@demoorg.com",
    "device_location": "UNKNOWN",
    "device_external_ip": "1.2.3.4",
    "mdr_alert": False,
    "report_id": "oJFtoawGS92fVMXlELC1Ow-b4ee93fc-ec58-436a-a940-b4d33a613513",
    "report_name": "Defense Evasion - Signed Binary Proxy Execution - InfDefaultInstall",
    "report_description": "\n\nThreat:\nThis behavior may be abused by adversaries to execute malicious files that could bypass application whitelisting and signature validation on systems.\n\nFalse Positives:\nSome environments may legitimate use this, but should be rare.\n\nScore:\n85",
    "report_tags": [
        "attack",
        "attackframework",
        "threathunting"
    ],
    "report_link": "https://attack.mitre.org/wiki/Technique/T1218",
    "ioc_id": "b4ee93fc-ec58-436a-a940-b4d33a613513-0",
    "ioc_hit": "((process_name:InfDefaultInstall.exe)) -enriched:true",
    "watchlists": [
        {
            "id": "9x0timurQkqP7FBKX4XrUw",
            "name": "Carbon Black Advanced Threats"
        }
    ],
    "process_guid": "ABCD1234-0114761e-00002ae4-00000000-19db1ded53e8000",
    "process_pid": 10980,
    "process_name": "infdefaultinstall.exe",
    "process_sha256": "1a2345cd88666a458f804e5d0fe925a9f55cf016733458c58c1980addc44cd774",
    "process_md5": "12c34567894a49f13193513b0138f72a9",
    "process_effective_reputation": "LOCAL_WHITE",
    "process_reputation": "NOT_LISTED",
    "process_cmdline": "InfDefaultInstall.exe C:\\Users\\username\\userdir\\Infdefaultinstall.inf",
    "process_username": "DEMO\\DEMOUSER",
    "process_issuer": "Demo Code Signing CA - G2",
    "process_publisher": "Demo Test Authority",
    "childproc_guid": "",
    "childproc_username": "",
    "childproc_cmdline": "",
    "ml_classification_final_verdict": "NOT_ANOMALOUS",
    "ml_classification_global_prevalence": "LOW",
    "ml_classification_org_prevalence": "LOW"
}

GET_ALERT_RESP_INVALID_ALERT_ID = {
    "type": "CB_ANALYTICS",
    "id": "86123310980efd0b38111eba4bfa5e98aa30b19",
    "legacy_alert_id": None,
    "org_key": "4JDT3MX9Q",
    "create_time": "2021-05-13T00:20:46.474Z",
    "last_update_time": "2021-05-13T00:27:22.846Z",
    "first_event_time": "2021-05-13T00:20:13.043Z",
    "last_event_time": "2021-05-13T00:20:13.044Z",
    "threat_id": "a26842be6b54ea2f58848b23a3461a16",
    "severity": 1,
    "category": "MONITORED",
    "device_id": 8612331,
    "device_os": "WINDOWS",
    "device_os_version": "Windows Server 2019 x64",
    "device_name": "win-2016-devrel",
    "device_username": "Administrator",
    "policy_id": 7113786,
    "policy_name": "Standard",
    "target_value": "MEDIUM",
    "workflow": {
        "state": "OPEN",
        "remediation": "None",
        "last_update_time": "2021-05-13T00:20:46.474Z",
        "comment": "None",
        "changed_by": "Carbon Black",
    },
    "notes_present": False,
    "tags": "None",
    "reason": "A port scan was detected from 10.169.255.100 on an external network (off-prem).",
    "reason_code": "R_SCAN_OFF",
    "process_name": "svchost.exe",
    "device_location": "OFFSITE",
    "created_by_event_id": "0980efd0b38111eba4bfa5e98aa30b19",
    "threat_indicators": [
        {
            "process_name": "svchost.exe",
            "sha256": "7fd065bac18c5278777ae44908101cdfed72d26fa741367f0ad4d02020787ab6",
            "ttps": [
                "ACTIVE_SERVER",
                "MITRE_T1046_NETWORK_SERVICE_SCANNING",
                "NETWORK_ACCESS",
                "PORTSCAN",
            ],
        }
    ],
}

GET_ALERT_TYPE_WATCHLIST = {
    "type": "WATCHLIST",
    "id": "6b2348cb-87c1-4076-bc8e-7c717e8af608",
    "legacy_alert_id": "6b2348cb-89b1-4076-bc8e-7c719e8af608",
    "org_key": "4JDT3MX9Q",
    "create_time": "2021-10-07T10:46:56.516Z",
    "last_update_time": "2021-10-07T10:46:56.516Z",
    "first_event_time": "2021-10-07T10:43:15.082Z",
    "last_event_time": "2021-10-07T10:43:15.082Z",
    "threat_id": "684285332DE159CA7BF925894E1FC953",
    "severity": 4,
    "category": "THREAT",
    "device_id": 11545912,
    "device_os": "WINDOWS",
    "device_os_version": None,
    "device_name": "TEST",
    "device_username": "Administrator",
    "policy_id": 7113786,
    "policy_name": "Standard",
    "target_value": "MEDIUM",
    "workflow": {
        "state": "OPEN",
        "remediation": None,
        "last_update_time": "2021-10-07T10:45:53.423Z",
        "comment": None,
        "changed_by": "Carbon Black",
    },
    "notes_present": False,
    "tags": None,
    "reason": 'Process msedge.exe was detected by the report.',
    "count": 0,
    "report_id": "QFFFabSGRrub94aetqjouQ",
    "report_name": "edge",
    "ioc_id": "66331b78-0259-4f57-857d-999d804c569e",
    "ioc_field": None,
    "ioc_hit": "(process_name:msedge.exe)",
    "watchlists": [{"id": "zDCzWnQL2YmGh5OlbF6Q", "name": "edge"}],
    "process_guid": "WNEXFKQ7-000309c2-00000478-00000000-1d6a1c1f2b02805",
    "process_name": "msedge.exe",
    "run_state": "RAN",
    "threat_indicators": [
        {
            "process_name": "msedge.exe",
            "sha256": "51470c146291697e5ee80b5409b013b414ea88da4c44fd0884723878f7e803ab",
            "ttps": ["66331b78-0259-4f57-857d-999d804c569e"],
        }
    ],
    "threat_cause_actor_sha256": "51470c146291697e5ee80b5409b013b414ea88da4c44fd0884723878f7e803ab",
    "threat_cause_actor_md5": "16c4c388f84eadd55634c2147e36ce64",
    "threat_cause_actor_name": "c:\\program files (x86)\\microsoft\\edge\\application\\msedge.exe",
    "threat_cause_reputation": "ADAPTIVE_WHITE_LIST",
    "threat_cause_threat_category": "UNKNOWN",
    "threat_cause_vector": "UNKNOWN",
    "document_guid": "TYPjsqedQmqRddFHjjhQpQ",
}

GET_ALERT_TYPE_WATCHLIST_INVALID = {
    "type": "WATCHLIST",
    "id": "6b2348cb-87c1-4076-bc8e-7c717e8af608",
    "legacy_alert_id": "6b2348cb-89b1-4076-bc8e-7c719e8af608",
    "org_key": "4JDT3MX9Q",
    "create_time": "2021-10-07T10:46:56.516Z",
    "last_update_time": "2021-10-07T10:46:56.516Z",
    "first_event_time": "2021-10-07T10:43:15.082Z",
    "last_event_time": "2021-10-07T10:43:15.082Z",
    "threat_id": "684285332DE159CA7BF925894E1FC953",
    "severity": 4,
    "category": "THREAT",
    "device_id": 11545912,
    "device_os": "WINDOWS",
    "device_os_version": None,
    "device_name": "TEST",
    "device_username": "Administrator",
    "policy_id": 7113786,
    "policy_name": "Standard",
    "target_value": "MEDIUM",
    "workflow": {
        "state": "OPEN",
        "remediation": None,
        "last_update_time": "2021-10-07T10:45:53.423Z",
        "comment": None,
        "changed_by": "Carbon Black",
    },
    "notes_present": False,
    "tags": None,
    "reason": 'Process msedge.exe was detected by the report.',
    "count": 0,
    "report_id": "QFFFabSGRrub94aetqjouQ",
    "report_name": "edge",
    "ioc_id": "66331b78-0259-4f57-857d-999d804c569e",
    "ioc_field": None,
    "ioc_hit": "(process_name:msedge.exe)",
    "watchlists": [{"id": "zDCzWnQL2YmGh5OlbF6Q", "name": "edge"}],
    "process_guid": "",
    "process_name": "msedge.exe",
    "run_state": "RAN",
    "threat_indicators": [
        {
            "process_name": "msedge.exe",
            "sha256": "51470c146291697e5ee80b5409b013b414ea88da4c44fd0884723878f7e803ab",
            "ttps": ["66331b78-0259-4f57-857d-999d804c569e"],
        }
    ],
    "threat_cause_actor_sha256": "51470c146291697e5ee80b5409b013b414ea88da4c44fd0884723878f7e803ab",
    "threat_cause_actor_md5": "16c4c388f84eadd55634c2147e36ce64",
    "threat_cause_actor_name": "c:\\program files (x86)\\microsoft\\edge\\application\\msedge.exe",
    "threat_cause_reputation": "ADAPTIVE_WHITE_LIST",
    "threat_cause_threat_category": "UNKNOWN",
    "threat_cause_vector": "UNKNOWN",
    "document_guid": "TYPjsqedQmqRddFHjjhQpQ",
}

GET_ALERT_RESP_WITH_NOTES = {
    "type": "CB_ANALYTICS",
    "id": "1ba0c35f-9c01-4413-afd8-fe4f01365e35",
    "legacy_alert_id": "62802DCE",
    "org_key": "4JDT3MX9Q",
    "create_time": "2021-05-13T00:20:46.474Z",
    "last_update_time": "2021-05-13T00:27:22.846Z",
    "first_event_time": "2021-05-13T00:20:13.043Z",
    "last_event_time": "2021-05-13T00:20:13.044Z",
    "threat_id": "a26842be6b54ea2f58848b23a3461a16",
    "severity": 1,
    "category": "MONITORED",
    "device_id": 8612331,
    "device_os": "WINDOWS",
    "device_os_version": "Windows Server 2019 x64",
    "device_name": "win-2016-devrel",
    "device_username": "Administrator",
    "policy_id": 7113786,
    "policy_name": "Standard",
    "target_value": "MEDIUM",
    "workflow": {
        "state": "OPEN",
        "remediation": "None",
        "last_update_time": "2021-05-13T00:20:46.474Z",
        "comment": "None",
        "changed_by": "Carbon Black",
    },
    "notes_present": True,
    "tags": "None",
    "reason": "A port scan was detected from 10.169.255.100 on an external network (off-prem).",
    "reason_code": "R_SCAN_OFF",
    "process_name": "svchost.exe",
    "device_location": "OFFSITE",
    "created_by_event_id": "0980efd0b38111eba4bfa5e98aa30b19",
    "threat_indicators": [
        {
            "process_name": "svchost.exe",
            "sha256": "7fd065bac18c5278777ae44908101cdfed72d26fa741367f0ad4d02020787ab6",
            "ttps": [
                "ACTIVE_SERVER",
                "MITRE_T1046_NETWORK_SERVICE_SCANNING",
                "NETWORK_ACCESS",
                "PORTSCAN",
            ],
        }
    ],
    "threat_activity_dlp": "NOT_ATTEMPTED",
    "threat_activity_phish": "NOT_ATTEMPTED",
    "threat_activity_c2": "NOT_ATTEMPTED",
    "threat_cause_actor_sha256": "10.169.255.100",
    "threat_cause_actor_name": "svchost.exe -k RPCSS -p",
    "threat_cause_actor_process_pid": "868-132563418721238249-0",
    "threat_cause_process_guid": "4JDT3MX9Q-008369eb-00000364-00000000-1d6f5ba1b173ce9",
    "threat_cause_parent_guid": "None",
    "threat_cause_reputation": "ADAPTIVE_WHITE_LIST",
    "threat_cause_threat_category": "NEW_MALWARE",
    "threat_cause_vector": "UNKNOWN",
    "threat_cause_cause_event_id": "0980efd1b38111eba4bfa5e98aa30b19",
    "blocked_threat_category": "UNKNOWN",
    "not_blocked_threat_category": "NEW_MALWARE",
    "kill_chain_status": ["RECONNAISSANCE"],
    "sensor_action": "None",
    "run_state": "RAN",
    "policy_applied": "NOT_APPLIED",
}

GET_ALERT_NOTES = {
    "num_found": 2,
    "num_available": 2,
    "results": [
        {
            "author": "Grogu",
            "id": "3gsgsfds",
            "note": "I am Grogu",
            "create_timestamp": "2023-04-18T03:25:44.397Z",
            "last_update_timestamp": "2023-04-18T03:25:44.397Z",
            "source": "CUSTOMER",
            "parent_id": None,
            "read_history": None,
            "thread": None
        },
        {
            "author": "demouser@demoorg.com",
            "create_timestamp": "2023-04-18T03:25:44.397Z",
            "last_update_timestamp": "2023-04-18T03:25:44.397Z",
            "id": "2",
            "source": "CUSTOMER",
            "note": "My first note",
            "parent_id": None,
            "read_history": None,
            "thread": None
        }
    ]
}

CREATE_ALERT_NOTE = {
    "author": "Grogu",
    "id": "3gsgsfds",
    "note": "I am Grogu",
    "create_timestamp": "2023-04-18T03:25:44.397Z",
    "last_update_timestamp": "2023-04-18T03:25:44.397Z",
    "source": "CUSTOMER",
    "parent_id": None,
    "read_history": None,
    "thread": None
}
