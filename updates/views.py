from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def update_model_detail_view(request):

    data = {"count": 1000, "content": "adsf"}

    return JsonResponse(data)
