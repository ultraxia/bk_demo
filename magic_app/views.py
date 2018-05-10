from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from account.decorators import login_exempt
from common.mymako import render_mako_context, render_json


def home(requests):
    return render_mako_context(requests,'magic_app/home.html', {})

@login_exempt
def get_app_info(requests):
    return render_json(
        {"result":'123',
         "demo":"324"}

    )

