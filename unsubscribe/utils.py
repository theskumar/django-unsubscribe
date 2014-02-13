import hashlib
from django.conf import settings

def get_token_for_user(user):
    m = hashlib.md5(user.email + settings.SECRET_KEY).hexdigest()
    return m