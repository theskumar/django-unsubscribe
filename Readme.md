Django Unsubscribe
==================

Django Unsubscribe make it menial to attach the proper unsubscribe methods to 
newsletter-type e-mails.

## Quickstart

Install Django Unsubcribe:

    pip install django-unsubcribe

Then use it in a project:

    from unsubscribe import UnsubscribableEmailMessage
    # rest of your code

## Features

* Adds `List-Unsubscribe` header to the email.
* Adds a context variable `unsubscribe_url` which can be used to render emails.
* Provides signals to implement the actual unsubscribe logic.

## Overview

This application is supposed to help at improving the overall quality of the 
mass e-mails your site sends out by:

1. Creating a simple subclass of `django.core.mail.EmailMultiAlternatives`, which adds a List-Unsubscribe header to the email message and a `render_message` function that is a wrapper to `render_to_string` to add `unsubscribe_url` to the context.

2. Providing a replaceable urlconf and view, which provides a unique url for each user wishing to unsubscribe.

This application does not:

1. Compose, create or mail newsletter e-mails for you. That is up to you.

2. Actually unsubscribe members from your mailing lists. It provides a signal, `unsubscribe.signals.user_unsubscribe`, which you must hook on to to unsubscribe your users.

## Contributing

Please send pull request or open a issue.

## License

MIT
