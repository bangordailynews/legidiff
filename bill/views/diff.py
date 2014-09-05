import logging

from django.conf import settings
from django.shortcuts import render_to_response
#from django.utils.encoding import smart_str

import ghdiff
import html2text
log = logging.getLogger('legidiff')

# No Models in use yet.

def _get_bill(location, name, version="", extension=".html"):
    path = "".join([location, name, version, extension])
    archived_bill = open(path, 'r')
    original_bill = archived_bill.read()
    unicode_bill = unicode(original_bill, 'utf-8')
    plain_bill = html2text.html2text(unicode_bill)
    return plain_bill


def diff(request):

    # Canned example read from local disk.
    data_dir = settings.BASE_DIR + "/tests/data/"
    bill_name = "HP_0718_LD_1020"

    before_text = _get_bill(data_dir, bill_name)
    after_text = _get_bill(data_dir, bill_name, "_v001")

    diff = ghdiff.diff(before_text, after_text, css=False)

    # Jinja requires unicode
#    uni_diff = unicode(diff, 'utf-8')
    uni_diff = diff

    # Send data off to be rendered.
    data = {"title": "diff of a bill",
            "bill": { "id": "HP 0718",
                "description": "An Act Regarding the Swans Island Lobster Fishing Zone"},
            "before": { "version": "original"},
            "after": {"version": "first revision"},
            "diff": uni_diff
            }
    return render_to_response('diff.jinja', data)
