import boto3
import click

session = boto3.Session(profile_name = "pythonAutomation")
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-buckets')
def list_bucket():
    "List all s3 buckets"
    for bucket in s3.bucket.all():
        print(bucket)

@cli.command('list-bucket-objects')
def list_bucket_objects():
    "List objects in an s3 bucket"
    for obj in s3.Bucket('automatinguri-commandline').objects.all():
        print(obj)

if __name__ == '_main_':
    cli()
