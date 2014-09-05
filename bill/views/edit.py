import logging

from django.conf import settings
from django.shortcuts import render_to_response

import html2text

log = logging.getLogger('legidiff')

# No Models in use yet.

def _get_bill(location, name, version="", extension=".html"):
    path = "".join([location, name, version, extension])
    archived_bill = open(path, 'r')
    original_bill = archived_bill.read()
    log.info("original_bill: {}".format(original_bill))
    unicode_bill = unicode(original_bill, 'utf-8')
    plain_bill = html2text.html2text(unicode_bill)
    return plain_bill


def edit(request):

    # Canned example read from local disk.
    data_dir = settings.BASE_DIR + "/tests/data/"
    bill_name = "HP_0718_LD_1020"

    bill_text = _get_bill(data_dir, bill_name)

    # Jinja requires unicode
    #safe_bill = unicode(bill_text, 'utf-8')
    safe_bill = bill_text

    # Send data off to be rendered.
    data = {"title": "edit this bill",
            "bill": { "id": "HP 0718",
                "description": "An Act Regarding the Swans Island Lobster Fishing Zone"},
            "before": { "version": "original"},
            "after": {"version": "first revision"},
            "bill_text": safe_bill
            }
    return render_to_response('edit.jinja', data)
