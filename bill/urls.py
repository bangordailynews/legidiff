from django.conf.urls import patterns, url

from bill.views import diff
from bill.views import edit

urlpatterns = patterns('',
    url(r'^diff$', diff.diff, name="diff"),
    url(r'^edit$', edit.edit, name="edit")
)
