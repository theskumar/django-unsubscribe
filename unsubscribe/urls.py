# -*- coding: utf-8 -*-
from unsubscribe.compat import patterns, url

urlpatterns = patterns('unsubscribe.views',
    url(r'^(?P<user_id>\d*)-(?P<token>.*)/$', 'unsubscribe',\
                                                name="unsubscribe_unsubscribe"),
)
