import boto3
import click

session=boto3.Session()
s3=session.resource('s3')

@click.group()
def cli():
    'Webetron deploys website to aws'
    pass

@cli.command('list-buckets')
def list_buckets():
    'Lists all the buckets'
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def lis_bucket_objects(bucket):
    'List all the objects within the bucket'
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

if __name__=='__main__':
    cli()
