from django.shortcuts import render_to_response

# No Models in use yet.

def diff(request):
    diff = ""
    data = {"title": "diff of a bill",
            "bill": { "id": "HP 0718",
                "description": "An Act Regarding the Swans Island Lobster Fishing Zone"},
            "before": { "version": "original"},
            "after": {"version": "first revision"},
            "diff": diff
            }
    return render_to_response('diff.jinja', data)
