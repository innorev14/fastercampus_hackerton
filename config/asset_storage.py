# pip install django-storages
# pip install boto3
from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = ''
    bucket_name = 'images.innorev.site'
    custom_domain = 'images.innorev.site'
    file_overwrite = False