import os
from.main import BASE_DIR

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR + '/media/'

IMAGE_ROOT = os.path.join(MEDIA_ROOT, "image")
IMAGE_URL = os.path.join(MEDIA_URL, "image")



#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# AWS_DEFAULT_ACL = None
#
# # Default Django Storage API behavior - don't overwrite files with same name
# AWS_S3_FILE_OVERWRITE = False
#
# try:
#     AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
#     AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
#     AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
# except KeyError:
#     raise KeyError('Need to define AWS environment variables: '
#                    'AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_STORAGE_BUCKET_NAME')
#
# MEDIA_ROOT = '/media/'
# MEDIA_URL = 'http://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
#
# STATIC_ROOT = '/static/'
# STATIC_URL = 'http://%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME