# diagram.py
from diagrams.aws.storage import SimpleStorageServiceS3Bucket

def s3_resource(name:str):

    return SimpleStorageServiceS3Bucket(label=name)


