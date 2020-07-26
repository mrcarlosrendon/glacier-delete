# glacier-delete
Given a JSON inventory of an Amazon Glacier vault, this will delete all archives. Uses `boto3` and `joblib` libraries for speed.

### How do I create the archive JSON file? 
See Glacier's docs: [Deleting an archive using the CLI](https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-an-archive-using-cli.html)

### How to install required libraries
`pip3 install -r requirements.txt`

### How to run
`python delete_archives.py [backup] [archivejson]`

### How to get help
`python delete_archives.py -h`

### How long will this take?
On my 16 CPU machine a vault of ~135,000 archives took ~30 minutes to delete.

### Why can't I delete the vault afterwards?
After deleting all of the archives, you need to recompute the inventory again :(

After that you should have an empty inventory and should be able to delete the vault.

See https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-vaults-cli.html
