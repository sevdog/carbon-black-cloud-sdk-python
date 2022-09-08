"""Mock responses for Workloads Search API."""

FETCH_COMPUTE_RESOURCE_BY_ID_RESP = {
    "id": "15396109",
    "appliance_uuid": "f6660a01-b0e5-46a7-aed0-45bf988ea78c",
    "cluster_name": "cwp-bucket-1-cluster",
    "datacenter_name": "cwp-bucket-1-datacenter",
    "esx_host_name": "10.105.17.113",
    "esx_host_uuid": "a2311b42-3e53-8f21-97d7-66680007185f",
    "vcenter_name": "VMware vCenter Server 6.7.0 build-14368073",
    "vcenter_host_url": "10.105.17.114",
    "vcenter_uuid": "9a8a0be5-ae1e-49ce-b2aa-34bc7dc445e3",
    "name": "cwp-bucket-1-centos_74",
    "host_name": "localhost.localdomain",
    "created_at": "2020-11-30T07:52:10.401Z",
    "ip_address": "10.105.17.107",
    "eligibility": "ELIGIBLE",
    "eligibility_code": ["Unsupported OS"],
    "installation_status": "SUCCESS",
    "installation_status_code": "SENSOR_INSTALLATION_SUCCESS",
    "uuid": "500e6a3f-ebf0-f2cb-3c23-182a1432563c",
    "os_description": "CentOS 7 (64-bit)",
    "os_type": "CENTOS",
    "os_architecture": "64",
    "vmwaretools_version": "2147483647"
}

FETCH_AWS_RESOURCE_BY_ID_RESP = {
    "auto_scaling_group_name": "GammaGroup",
    "availability_zone": "us-west-1c",
    "cloud_provider_account_id": "0112249969",
    "cloud_provider_resource_id": "XAW11",
    "cloud_provider_tags": [
        "Name##Demo-ASG",
    ],
    "create_time": "2022-06-02T05:23:27Z",
    "deployment_type": "AWS",
    "external_ip": "192.168.1.1",
    "id": "7001",
    "image_description": "Amazon Linux 2 Kernel 5.10 AMI 2.0.20220426.0 x86_64",
    "image_id": "ami-abcd123443",
    "image_name": "amzn2-ami-kernel-5.10-hvm-2.0.20220426.0-x86_64-gp2",
    "installation_status": "NOT_INSTALLED",
    "instance_state": "running",
    "instance_type": "t2.micro",
    "internal_ip": "192.168.2.2",
    "name": "Demo-ASG",
    "org_key": "test",
    "platform": "Unix/Linux",
    "platform_details": "Linux/UNIX",
    "region": "us-west-1",
    "security_group_id": [
        "kappa-group"
    ],
    "subnet_id": "3303",
    "virtual_private_cloud_id": "90210"
}

SEARCH_COMPUTE_RESOURCES = {
    "num_found": 1,
    "results": [
        {
            "id": "15054477",
            "appliance_uuid": "c89f183b-f201-4bca-bacc-80184b5b8823",
            "cluster_name": "launcher-cluster",
            "datacenter_name": "launcher-dc",
            "esx_host_name": "10.105.5.70",
            "esx_host_uuid": "d5304d56-5004-a871-1ad1-bd4b4af9977d",
            "vcenter_name": "VMware vCenter Server 7.0.0 build-15952599",
            "vcenter_host_url": "10.105.5.63",
            "vcenter_uuid": "4a6b1382-f917-4e1a-8564-374cb7274bd7",
            "name": "vsvv-2k8r2",
            "host_name": "QUIMBY",
            "created_at": "2020-11-18T07:41:18.218Z",
            "ip_address": "192.168.1.1",
            "device_guid": "a12e0d99-2114-459c-abf8-1af5f719f121",
            "registration_id": "20-112233999",
            "eligibility": "NOT_ELIGIBLE",
            "eligibility_code": [
                "VMware Tools install required",
                "Launcher not found",
                "VM is offline"
            ],
            "installation_status": "NOT_INSTALLED",
            "installation_status_code": "",
            "installation_type": "A",
            "uuid": "502277cc-0aa9-80b0-9ac8-6f540c11edaf",
            "os_description": "Windows 10 32-bit",
            "os_type": "WINDOWS",
            "os_architecture": "32",
            "vmwaretools_version": "0"
        }
    ]
}

SEARCH_AWS_RESOURCES = {
    "num_found": 1,
    "results": [
        {
            "auto_scaling_group_name": "GammaGroup",
            "availability_zone": "us-west-1c",
            "cloud_provider_account_id": "0112249969",
            "cloud_provider_resource_id": "XAW11",
            "cloud_provider_tags": [
                "Name##Demo-ASG",
            ],
            "create_time": "2022-06-02T05:23:27Z",
            "deployment_type": "AWS",
            "external_ip": "192.168.1.1",
            "id": "7001",
            "image_description": "Amazon Linux 2 Kernel 5.10 AMI 2.0.20220426.0 x86_64",
            "image_id": "ami-abcd123443",
            "image_name": "amzn2-ami-kernel-5.10-hvm-2.0.20220426.0-x86_64-gp2",
            "installation_status": "NOT_INSTALLED",
            "instance_state": "running",
            "instance_type": "t2.micro",
            "internal_ip": "192.168.2.2",
            "name": "Demo-ASG",
            "org_key": "test",
            "platform": "Unix/Linux",
            "platform_details": "Linux/UNIX",
            "region": "us-west-1",
            "security_group_id": [
                "kappa-group"
            ],
            "subnet_id": "3303",
            "virtual_private_cloud_id": "90210"
        }
    ]
}
