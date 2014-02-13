from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.models import User
from django.http import Http404
from django.template import RequestContext

from .utils import get_token_for_user
from .signals import user_unsubscribed

def unsubscribe(request, user_id, token,\
                template='unsubscribe/unsubscribe.html', extra_context=None):
    """
    Checks the user token and fires `unsubscribe.signals.user_unsubscribed` and
    returns unsubscribe/unsubscribe.html with extra_context, which could include
    callables and `unsubscribe_user`, which is the user that is unsibscribing.
    """
    user = get_object_or_404(User, pk=user_id)
    if not token == get_token_for_user(user):
        raise Http404, "Token did not match"

    context = RequestContext(request)

    if extra_context is None:
        extra_context = {}
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value

    user_unsubscribed.send(sender=User, user=user)

    return render_to_response(template, {'unsubscribe_user' : user}, context_instance=context)
