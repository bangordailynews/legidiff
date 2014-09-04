from django.conf import settings
from django.shortcuts import render_to_response
#from django.utils.encoding import smart_str

import ghdiff
import logging
log = logging.getLogger('legidiff')

# No Models in use yet.

def diff(request):
    data_dir = settings.BASE_DIR + "/tests/data/"
    bill_text = "HP_0718_LD_1020"
    before_path = "".join([data_dir, bill_text, ".html"])
    after_version = "_v001"
    after_path = "".join([data_dir, bill_text, after_version, ".html"])
    before = open(before_path, 'r')
    before_text = before.read()
    after = open(after_path, 'r')
    after_text = after.read()
    diff = ghdiff.diff(before_text, after_text, css=False)
    uni_diff = unicode(diff, 'utf-8')
    data = {"title": "diff of a bill",
            "bill": { "id": "HP 0718",
                "description": "An Act Regarding the Swans Island Lobster Fishing Zone"},
            "before": { "version": "original"},
            "after": {"version": "first revision"},
            "diff": uni_diff
            }
    return render_to_response('diff.jinja', data)
