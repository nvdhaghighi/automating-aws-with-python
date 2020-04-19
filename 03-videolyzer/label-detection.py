# coding: utf-8
import boto3
session=boto3.Session()
get_ipython().run_line_magic('clear', '')
s3=session.resource('s3')
bucket=s3.create_bucket('videolyzer-navid')
bucket=s3.create_bucket(Bucket='videolyzer-navid')
bucket
get_ipython().run_line_magic('ls', '/Users/navidhaghighi/Downloads/*.mp4')
pathname='/Users/navidhaghighi/Downloads/Pexels Videos 1466210.mp4'
from pathlib import Path
path=Path(pathname).expanduser().resolve()
print(path)
path.name
bucket.upload_file(str(path), str(path.name))
rekognition_client=session.client('rekognition')
response = client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name,'Name': path.name}})
response = rekognition_client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name,'Name': path.name}})
response
job_id=response['JobId']
result=response = client.get_label_detection(
    JobId=job_id
)
result=rekognition_client.get_label_detection(
    JobId=job_id
)
result
result.keys()
result['Labels']
len(result['Labels'])
get_ipython().run_line_magic('save', 'label-detection.py 1-30')
