from django.conf.urls import patterns, url

from bill.views import diff

urlpatterns = patterns('',
    url(r'^$', diff.diff, name="diff")
)
