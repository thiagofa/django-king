# -*- coding: utf-8 -*-
#from django.forms.util import ErrorList

def get_last_error_message(form):
    for f in form:
        if f.errors:
            message = f.errors[0]
            break
    
    return message

#def at_least_one_required(form, field1, field2, message):
#    cleaned_data = form.cleaned_data
#
#    if not bool(cleaned_data.get(field1)) and not bool(cleaned_data.get(field2)):
#        form._errors['phone'] = ErrorList([message])
        
def r(message):
    return {'required': message}

def i(message):
    return {'invalid': message}

def r_i(message_r, message_i):
    messages = r(message_r);
    messages.update(i(message_i))
    return messages