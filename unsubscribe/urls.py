# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .compat import patterns, url

urlpatterns = patterns('unsubscribe.views',
    url(r'^(?P<user_id>\d*)-(?P<token>.*)/$', 'unsubscribe',\
                                                name="unsubscribe_unsubscribe"),
)
