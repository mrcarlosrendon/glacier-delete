"""
Delete's AWS Glacier archives given a Vault's inventory JSON
Handles step 5 of:
https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-an-archive-using-cli.html

Usage: delete_archives.py [vault_name] [archive_json_file]
"""

import os
import json
import boto3
import argparse

from joblib import Parallel, delayed

argparser = argparse.ArgumentParser()
argparser.add_argument("vault", help="Vault Name")
help = "JSON of Archive Inventory. See step 4 of " \
       "https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-an-archive-using-cli.html"
argparser.add_argument("archive_json_file",
                       help=help)
args = argparser.parse_args()

with open(args.archive_json_file) as f:
    j = json.load(f)

archives = j.get('ArchiveList')
print("Deleting " + str(len(archives)) + " archives.")


def delete_boto(archive):
    client = boto3.client("glacier")
    archive_id = archive.get("ArchiveId")
    try:
        resp = client.delete_archive(vaultName=args.vault,
                                     archiveId=archive_id)
    except Exception as e:
        print(resp)
        print(e)


Parallel(n_jobs=os.cpu_count(),
         prefer="threads",
         verbose=1)(delayed(delete_boto)(archive) for archive in archives)
