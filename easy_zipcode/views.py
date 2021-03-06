# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse

from main import EasyZipCode


def zipcode_view(request):
    return HttpResponse(EasyZipCode.get_zipcode_info(
        zip_code=request.GET.get('zip_code'),
        token=settings.EASY_ZIPCODE_TOKEN,
        plain_text=True,
    ))
