# -*- coding: utf-8 -*-
from django import template
import locale
register = template.Library()
 
@register.filter()
def money(value):
    return "%s %s" % (locale.localeconv()['currency_symbol'], 
                      locale.currency(value, grouping=True, symbol=False))