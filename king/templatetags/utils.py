# -*- coding: utf-8 -*-
from django import template
register = template.Library()
 
@register.filter
def strip_url(url, final_index):
    parts = url[1:len(url)-1].split('/')
    
    path = '/'.join(parts[:final_index])
    
    if path:
        path = '/' + path + '/'
    else:
        path = '/'
        
    return path
    