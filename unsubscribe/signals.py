from django.dispatch import Signal

user_unsubscribed = Signal(providing_args=['user'])