# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase


class UtilsTests(TestCase):
    """docstring for UtilsTests"""

    def setUp(self):
        self.username = 'theskumar'
        self.email = 'theskumar@example.com'

    def test_foo(self):
        self.assertEqual('foo', "foo")
