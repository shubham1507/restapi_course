from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from django.core.serializers import serialize

from django.views.generic import View

from restapi.mixins import JsonResponseMixin

from updates.models import Update

# Create your views here.


def json_example_view(request):
    '''
        GET --> Retrieve
    '''

    data = {"count": 1000, "content": "adsf"}

    json_data = json.dumps(data)
    '''
        Django uses request and response objects to pass state through the system. Each view is responsible for returning an HttpResponse object. Using HttpResponse you need to first serialize your object to JSON.

Whereas,

Since version 1.7, Django counts with the built-in JsonResponse class, which is a subclass of HttpResponse. Its default Content-Type header is set to application/json, which is really convenient. It also comes with a JSON encoder, so you don’t need to serialize the data before returning the response object.
    '''

    # return JsonResponse(data)

    return HttpResponse(json_data, content_type='application/json')


class JsonCBV(View):
    def get(self, request, *args, **kwargs):

        data = {"count": 1000, "content": "sample JSON content"}

        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):

        data = {"count": 1000, "content": "sample JSON content"}

        return self.rendor_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):

        obj = Update.objects.get(id=1)

        # data = serialize("json", [obj], fields=('user', 'content'))

        json_data = obj.serialize()

        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):

        qs = Update.objects.all()

        # data = serialize("json", qs, fields=('user', 'content'))

        data = qs.serialize()

        return HttpResponse(data, content_type='application/json')
