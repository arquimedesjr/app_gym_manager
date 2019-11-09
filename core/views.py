
uts import render_to_response, render
from django.http import HttpResponseRedirect


import dashboard


def dashboard(request):
    """-------------------------------------------------------------------------
    View index principal do projeto.
    -------------------------------------------------------------------------"""
    return render_to_response("dashboard.html")

