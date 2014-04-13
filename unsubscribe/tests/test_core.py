# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from unsubscribe.mail import UnsubscribableEmailMessage
from unsubscribe.utils import get_token_for_user


class UnsubscribeTest(TestCase):
    def setUp(self):
        self.user = User(username='unsubscribe-testuser', email='testuser@sdaf.com')
        self.user.save()

    def test_list_unsubscribe_headers(self):
        msg = UnsubscribableEmailMessage(self.user, "Test Message", "Body",
            from_email="test@testserver.com", to=["testemail@somewhereelse.com"])
        msg.send()

        from django.core.mail import outbox
        self.assertEquals(len(outbox), 1)
        self.assertTrue('List-Unsubscribe' in outbox[0].extra_headers.keys())
        self.assertEquals(outbox[0].extra_headers['List-Unsubscribe'], '<' + msg.unsubscribe_url + '>')

    def test_list_unsubscribe_view(self):
        closure_test = [0]
        def test_callback(sender, user, **kwargs):
            closure_test[0] = 1

        from unsubscribe.signals import user_unsubscribed
        user_unsubscribed.connect(test_callback)

        from django.test.client import Client
        c = Client()
        c.get(reverse('unsubscribe_unsubscribe',
                            args=(self.user.pk, get_token_for_user(self.user))))

        self.assertTrue(closure_test[0])
