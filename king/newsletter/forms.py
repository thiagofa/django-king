# -*- coding: utf-8 -*-
from django import forms
from king.utils.forms import r_i

class SubscriptionForm(forms.Form):
    email = forms.EmailField(error_messages=r_i('Por favor, informe o seu e-mail.',
                                                'O e-mail informado não é válido.'))