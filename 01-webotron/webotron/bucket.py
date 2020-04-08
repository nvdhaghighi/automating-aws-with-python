"""Classes for S3 buckets"""

class BucketManager:
    def __init__(self, session):
        self.s3=session.resource('s3')
