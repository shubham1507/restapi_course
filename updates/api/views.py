from updates.models import Update as UpdateModel

from django.http import HttpResponse

from django.views.generic import View

from django.core.serializers import serialize

from .mixins import CSRFExemptMixin

import json


class UpdateModelDetailAPIView(View, CSRFExemptMixin):
    '''
    retrieve,update,delete --> Object
    '''
    def get(self, request, id, *args, **kwargs):

        obj = UpdateModel.objects.get(id=id)

        json_data = obj.serialize()

        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):

        return HttpResponse({}, content_type='application/json')

    def put(self, request, *args, **kwargs):

        return HttpResponse({}, content_type='application/json')

    def delete(self, request, *args, **kwargs):

        return HttpResponse({}, content_type='application/json')


class UpdateModelListAPIView(CSRFExemptMixin, View):
    '''
    ListView
    createView
    '''
    def get(self, request, *args, **kwargs):

        qs = UpdateModel.objects.all()

        json_data = serialize("json", qs)

        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):

        data = json.dumps({"message": "unknown data"})

        return HttpResponse(data, content_type='application/json')

    def delete(self, request, *args, **kwargs):

        data = json.dumps({"message": "You can not delete"})

        return HttpResponse(data, content_type='application/json')
