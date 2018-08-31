from django.conf.urls import patterns, url

from account_captcha.views import SignupViewCaptcha

urlpatterns = patterns('',
    url(r'^$', SignupViewCaptcha.as_view(), name='account_signup'),
)
