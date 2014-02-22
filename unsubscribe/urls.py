# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('unsubscribe.views',
    url(r'^(?P<user_id>\d*)-(?P<token>.*)/$', 'unsubscribe',\
                                                name="unsubscribe_unsubscribe"),
)
