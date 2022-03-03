#!/usr/bin/python3

import sys

import boto3
from botocore.exceptions import ClientError


def create_client(endpoint, profile="s3-tests-admin"):
    session = boto3.Session(profile_name=profile)
    s3_client = session.client('s3', endpoint_url=endpoint)
    return s3_client


def clean_bucket(client, bucket):
    loops = 0
    truncated = True
    while truncated:
        resp = client.list_object_versions(Bucket=bucket)
        truncated = resp.get('IsTruncated', False)
        versions = [{'Key': ver['Key'], 'VersionId': ver['VersionId']}
                    for ver in resp.get('Versions', [])]
        if not versions or loops > 2000:
            break
        try:
            print(
                f"Deleting {len(versions)} object versions from {bucket}... ",
                end=''
            )
            client.delete_objects(Bucket=bucket,
                                  Delete={'Objects': versions})
            # TODO(FVE): check response, deletion may have failed
            print("OK")
        except ClientError as exc:
            print(f"{exc}")
        loops += 1


def clean_all_buckets(client):
    all_buckets = client.list_buckets()
    for bucket in all_buckets['Buckets']:
        try:
            print(f"Cleaning bucket {bucket['Name']}")
            clean_bucket(client, bucket['Name'])
            client.delete_bucket(Bucket=bucket['Name'])
        except ClientError as exc:
            print(f"Failed to clean {bucket['Name']}: {exc}")


if __name__ == "__main__":
    PROFILE = sys.argv[1]
    ENDPOINT = sys.argv[2]
    CLIENT = create_client(ENDPOINT, PROFILE)
    clean_all_buckets(CLIENT)
