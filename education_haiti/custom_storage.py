# Class Configuration for the storage of Media files, right now.
# Storage of static files is being considered for the future

class MediaStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION
