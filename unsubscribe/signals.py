# -*- coding: utf-8 -*-
from django.dispatch import Signal

user_unsubscribed = Signal(providing_args=['user'])
