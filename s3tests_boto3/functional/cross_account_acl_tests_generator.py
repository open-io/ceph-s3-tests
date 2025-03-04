# This script generates cross account tests
from datetime import date

# The folllowing list contains dictionaries that describes tests of one function
# that will be tested with alt_client for each acl on the resource (bucket or
# object)
test_list = [
    {
        "resource": "bucket",
        "method": "get",
        "function": "list_objects_v2",
        "args": ["Bucket=bucket_name"],
        "result": {
            "READ": True,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": True,
        },
    },
    {
        "resource": "bucket",
        "method": "get",
        "function": "list_object_versions",
        "args": ["Bucket=bucket_name"],
        "result": {
            "READ": True,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": True,
        },
    },
    {
        "resource": "bucket",
        "method": "get",
        "function": "list_multipart_uploads",
        "args": ["Bucket=bucket_name"],
        "result": {
            "READ": True,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": True,
        },
    },
    {
        "resource": "bucket",
        "method": "put",
        "function": "put_object",
        "args": ["Bucket=bucket_name", 'Key="foo"'],
        "result": {
            "READ": False,
            "WRITE": True,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": True,
        },
    },
    {
        "resource": "bucket",
        "method": "get",
        "function": "get_bucket_acl",
        "args": ["Bucket=bucket_name"],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": True,
            "WRITE_ACP": False,
            "FULL_CONTROL": True,
        },
    },
    {
        "resource": "bucket",
        "method": "put",
        "function": "put_bucket_acl",
        "args": ["Bucket=bucket_name", 'GrantFullControl="id=" + alt_user_id'],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": True,
            "FULL_CONTROL": True,
        },
    },
    {
        "resource": "bucket",
        "method": "get",
        "function": "get_bucket_cors",
        "args": ["Bucket=bucket_name"],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": False,
        },
    },
    {
        "resource": "bucket",
        "method": "put",
        "function": "put_bucket_cors",
        "args": ["Bucket=bucket_name", "CORSConfiguration=config"],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": False,
        },
        "prerequisite": """    config = {"CORSRules": [{"AllowedMethods": ["GET"], "AllowedOrigins": ["*"]}]}
""",
    },
    {
        "resource": "bucket",
        "method": "get",
        "function": "get_bucket_tagging",
        "args": ["Bucket=bucket_name"],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": False,
        },
    },
    {
        "resource": "bucket",
        "method": "put",
        "function": "put_bucket_tagging",
        "args": ["Bucket=bucket_name", "Tagging=tags"],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": False,
        },
        "prerequisite": """    tags = {"TagSet": [{"Key": "test", "Value": "test"}]}
""",
    },
    {
        "resource": "bucket",
        "method": "get",
        "function": "get_bucket_lifecycle",
        "args": ["Bucket=bucket_name"],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": False,
        },
    },
    {
        "resource": "bucket",
        "method": "put",
        "function": "put_bucket_lifecycle_configuration",
        "args": [
            "Bucket=bucket_name",
            "LifecycleConfiguration=lifecycle_configuration",
        ],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": False,
        },
        "prerequisite": """    lifecycle_configuration = {
        "Rules": [
            {
                "Expiration": {
                    "Days": 7,
                },
                "ID": "myfirstrule",
                "Filter": {"Prefix": "garbage/"},
                "Status": "Enabled",
            }
        ]
    }
""",
    },
    {
        "resource": "bucket",
        "method": "delete",
        "function": "delete_bucket_lifecycle",
        "args": ["Bucket=bucket_name"],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": False,
        },
    },
    {
        "resource": "bucket",
        "method": "get",
        "function": "get_bucket_versioning",
        "args": ["Bucket=bucket_name"],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": False,
        },
    },
    {
        "resource": "bucket",
        "method": "put",
        "function": "put_bucket_versioning",
        "args": [
            "Bucket=bucket_name",
            "VersioningConfiguration=versioning_configuration",
        ],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": False,
        },
        "prerequisite": """    versioning_configuration = {"Status": "Enabled"}
""",
    },
    {
        "resource": "bucket",
        "method": "get",
        "function": "get_object_lock_configuration",
        "args": ["Bucket=bucket_name"],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": False,
        },
    },
    {
        "resource": "bucket",
        "method": "put",
        "function": "put_object_lock_configuration",
        "args": [
            "Bucket=bucket_name",
            "ObjectLockConfiguration=object_lock_configuration",
        ],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": False,
        },
        "prerequisite": """    object_lock_configuration = {
        'ObjectLockEnabled':'Enabled',
        'Rule': {
            'DefaultRetention': {
                'Mode':'GOVERNANCE',
                'Days':1
            }
        }
    }
""",
    },
    {
        "resource": "bucket",
        "method": "get",
        "function": "get_bucket_website",
        "args": ["Bucket=bucket_name"],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": False,
        },
    },
    {
        "resource": "bucket",
        "method": "put",
        "function": "put_bucket_website",
        "args": ["Bucket=bucket_name", "WebsiteConfiguration=website_config"],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": False,
        },
        "prerequisite": """    website_config = {
        'IndexDocument': {
            'Suffix': 'foo'
        }
    }
""",
    },
    {
        "resource": "bucket",
        "method": "delete",
        "function": "delete_bucket_website",
        "args": ["Bucket=bucket_name"],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": False,
        },
    },
    {
        "resource": "bucket",
        "method": "get",
        "function": "get_bucket_encryption",
        "args": ["Bucket=bucket_name"],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": False,
        },
    },
    {
        "resource": "bucket",
        "method": "put",
        "function": "put_bucket_encryption",
        "args": [
            "Bucket=bucket_name",
            "ServerSideEncryptionConfiguration=server_side_encryption_conf",
        ],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": False,
        },
        "prerequisite": """    server_side_encryption_conf = {
        'Rules': [
            {
                'ApplyServerSideEncryptionByDefault': {
                    'SSEAlgorithm': 'AES256'
                }
            },
        ]
    }
""",
    },
    {
        "resource": "bucket",
        "method": "get",
        "function": "get_bucket_location",
        "args": ["Bucket=bucket_name"],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": False,
        },
    },
    {
        "resource": "object",
        "method": "get",
        "function": "get_object",
        "args": ["Bucket=bucket_name", "Key=object_name"],
        "result": {
            "READ": True,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": True,
        },
    },
    {
        "resource": "object",
        "method": "get",
        "function": "get_object",
        "args": [
            "Bucket=bucket_name",
            "Key=object_name",
            "VersionId=version_id",
        ],
        "result": {
            "READ": True,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": False,
            "FULL_CONTROL": True,
        },
        "name": "get_object_version",
        "prerequisite": """    main_client.put_bucket_versioning(
        Bucket=bucket_name, VersioningConfiguration={"Status": "Enabled"}
    )
    response = main_client.put_object(Bucket=bucket_name, Key=object_name)
    version_id = response["VersionId"]
""",
    },
    {
        "resource": "object",
        "method": "get",
        "function": "get_object_acl",
        "args": ["Bucket=bucket_name", "Key=object_name"],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": True,
            "WRITE_ACP": False,
            "FULL_CONTROL": True,
        },
    },
    {
        "resource": "object",
        "method": "put",
        "function": "put_object_acl",
        "args": [
            "Bucket=bucket_name",
            "Key=object_name",
            'GrantFullControl="id=" + alt_user_id',
        ],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": True,
            "FULL_CONTROL": True,
        },
    },
    {
        "resource": "object",
        "method": "get",
        "function": "get_object_acl",
        "args": [
            "Bucket=bucket_name",
            "Key=object_name",
            "VersionId=version_id",
        ],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": True,
            "WRITE_ACP": False,
            "FULL_CONTROL": True,
        },
        "name": "get_object_version_acl",
        "prerequisite": """    main_client.put_bucket_versioning(
        Bucket=bucket_name, VersioningConfiguration={"Status": "Enabled"}
    )
    response = main_client.put_object(Bucket=bucket_name, Key=object_name)
    version_id = response["VersionId"]
""",
    },
    {
        "resource": "object",
        "method": "put",
        "function": "put_object_acl",
        "args": [
            "Bucket=bucket_name",
            "Key=object_name",
            "VersionId=version_id",
            'GrantFullControl="id=" + alt_user_id',
        ],
        "result": {
            "READ": False,
            "WRITE": False,
            "READ_ACP": False,
            "WRITE_ACP": True,
            "FULL_CONTROL": True,
        },
        "name": "put_object_version_acl",
        "prerequisite": """    main_client.put_bucket_versioning(
        Bucket=bucket_name, VersioningConfiguration={"Status": "Enabled"}
    )
    response = main_client.put_object(Bucket=bucket_name, Key=object_name)
    version_id = response["VersionId"]
""",
    },
]


HEADER = """# Generated by cross_account_acl_tests_generator.py
# Date of creation: {creation_date}

from botocore.exceptions import ClientError
from .utils import assert_raises
from .utils import _get_status
from . import (
    configfile,
    setup_teardown,
    get_client,
    get_alt_client,
    get_new_bucket_name,
    get_alt_user_id,
)

"""


def _generate_prerequisite(name, resource, prerequisite, acl):
    PREREQUISITE_TMPL = """def test_{name}_cross_account_with_{acl}_acl():
    bucket_name = get_new_bucket_name()
    main_client = get_client()
    main_client.create_bucket(Bucket=bucket_name)
{create_object}{prerequisite}    alt_client = get_alt_client()
    alt_user_id = get_alt_user_id()
    # put bucket acl {acl} for alt user
"""
    create_object = ""
    if resource == "object":
        create_object = """    object_name = "foo"
    main_client.put_object(Bucket=bucket_name, Key=object_name)
"""
    if prerequisite is None:
        prerequisite = ""
    return PREREQUISITE_TMPL.format(
        name=name,
        acl=acl,
        create_object=create_object,
        prerequisite=prerequisite,
    )


def _generate_put_acl(resource, acl):
    PUT_ACL_TMPL = """    main_client.{method}(
        Bucket=bucket_name{object}, {grant_acl}="id=" + alt_user_id
    )
"""
    if resource == "bucket":
        method = "put_bucket_acl"
        object = ""
    else:
        method = "put_object_acl"
        object = ", Key=object_name"
    if acl == "READ":
        grant_acl = "GrantRead"
    elif acl == "WRITE":
        grant_acl = "GrantWrite"
    elif acl == "READ_ACP":
        grant_acl = "GrantReadACP"
    elif acl == "WRITE_ACP":
        grant_acl = "GrantWriteACP"
    else:
        grant_acl = "GrantFullControl"
    return PUT_ACL_TMPL.format(
        method=method, object=object, grant_acl=grant_acl
    )


def _generate_test_function(function, args, result):
    TEST_FUNCTION_FAIL_TMPL = """    e = assert_raises(
        ClientError, alt_client.{fucntion}
    )
    status = _get_status(e.response)
    assert status == 403
"""
    if result:
        return "    alt_client." + function + "(" + ", ".join(args) + ")\n"
    else:
        return TEST_FUNCTION_FAIL_TMPL.format(
            fucntion=function + ", " + ", ".join(args)
        )


def _generate_test(
    resource, method, function, args, acl, result, name, prerequisite
):
    if name is None:
        name = function
    output = "\n\n"
    output += _generate_prerequisite(name, resource, prerequisite, acl)
    output += _generate_put_acl(resource, acl)
    output += _generate_test_function(function, args, result)
    return output


def generate_all():
    current_date = date.today()
    output = HEADER.format(creation_date=current_date.isoformat())

    for test in test_list:
        results = test["result"]
        for acl, result in results.items():
            output += _generate_test(
                test["resource"],
                test["method"],
                test["function"],
                test["args"],
                acl,
                result,
                test.get("name"),
                test.get("prerequisite"),
            )
    with open("test_s3_cross_account_acl.py", "w") as fd:
        fd.write(output)


if __name__ == "__main__":
    generate_all()
