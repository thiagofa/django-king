# -*- coding: utf-8 -*-
from mailsnake import MailSnake
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from djangoking.newsletter.forms import SubscriptionForm
from djangoking.utils.forms import get_last_error_message
import simplejson
from django.http import HttpResponse
from mailsnake.exceptions import ListAlreadySubscribedException

@csrf_exempt
def subscribe(request):
    ms = MailSnake(settings.MAILCHIMP_KEY)
    form = SubscriptionForm(request.POST)
    
    result = {}
    
    if form.is_valid():
        try:
            subscribed = ms.listSubscribe(id=settings.MAILCHIMP_NEWSLETTER_LIST_ID, 
                                          email_address=form.cleaned_data['email'], 
                                          double_optin=False)
            
            if subscribed:
                result = {'status': 'success', 'message': 'E-mail cadastrado com sucesso! :)'}
            else:
                result = {'status': 'error', 'message': 'Algo de errado aconteceu e seu e-mail não foi cadastrado. :('}
            
        except ListAlreadySubscribedException:
            result = {'status': 'success', 'message': 'O e-mail informado já estava cadastrado em nossa newsletter. ;)'}
    else:
        result = {'status': 'error', 'message': get_last_error_message(form)}
    
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')