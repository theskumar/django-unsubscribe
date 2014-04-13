# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

from .utils import get_token_for_user


class UnsubscribableEmailMessage(EmailMultiAlternatives):
    """
    A simple wrapper around EmailMultiAlternatives that requires a User
    object and appends a `List-Unsubscribe` header to the email message
    """
    def __init__(self, user, subject='', body='', from_email=None, to=None,
                                bcc=None, connection=None, attachments=None,
                                headers=None, alternatives=None):
        unsub_headers = headers or {}
        unsub_url = reverse('unsubscribe_unsubscribe',
            args=[user.pk, get_token_for_user(user)])

        # TODO fix scheme not to be hard coded.
        protocol = 'http'
        site_url = '%s://%s' % (protocol, Site.objects.get_current().domain)
        unsub_headers['List-Unsubscribe'] = '<%s%s>' % (site_url, unsub_url)
        super(UnsubscribableEmailMessage, self).__init__(subject=subject,
                            body=body, from_email=from_email, to=to, bcc=bcc,
                            connection=connection, attachments=attachments,
                            headers=unsub_headers, alternatives=alternatives)

    def _get_unsubscribe_url(self):
        return self.extra_headers['List-Unsubscribe'][1:-1]

    def _set_unsubscribe_url(self, value):
        self.extra_headers['List-Unsubscribe'] = "<%s>" % value

    unsubscribe_url = property(_get_unsubscribe_url, _set_unsubscribe_url)

    def render_message(self, template, context=None):
        """
        A wrapper around render_to_string which feeds the template the
        additional context, `unsubscribe_url` which is the url for the user to
        unsubscribe
        """
        if not context:
            context = {}
        context['unsubscribe_url'] = self.unsubscribe_url
        return render_to_string(template, context)
