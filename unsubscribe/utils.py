# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import hashlib
from django.conf import settings

def get_token_for_user(user):
    # TODO: use USERNAME_FIELD instead
    token = str(user.email + settings.SECRET_KEY).encode('utf-8')
    return hashlib.md5(token).hexdigest()
