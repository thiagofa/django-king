from django.conf.urls import patterns, url

urlpatterns = patterns('king.newsletter.mailchimp',
    
    url(r'^subscribe$', 'json.subscribe', name='mailchimp-subscribe'),
    
)