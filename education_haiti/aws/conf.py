import datetime
import os

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False
AWS_S3_SECURE_URLS = False
DEFAULT_FILE_STORAGE = 'education_haiti.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'education_haiti.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'education-haiti'
S3DIRECT_REGION = 'us-east-2'
S3_URL = '//{}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)
MEDIA_URL = '//{}.s3.amazonaws.com/media/'.format(AWS_STORAGE_BUCKET_NAME)
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}
