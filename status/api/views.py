from rest_framework.views import APIView
from rest_framework import generics, mixins

from rest_framework.response import Response

from status.models import Status

from .serializers import StatusSerializer
# from django.views.generic import View


class StatusListSearchAPIView(APIView):
    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)


class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
            print(qs)

        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class StatusCreateAPIView(generics.CreateAPIView):

#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer


class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Status.objects.all()
    serializer_class = StatusSerializer


# class StatusDetailAPIView(mixins.CreateModelMixin, mixins.UpdateModelMixin,
#                           mixins.DestroyModelMixin, generics.RetrieveAPIView):

#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# lookup_field = 'id'

# def get_object(self, *args, **kwargs):

#     kwargs = self.kwargs
#     kw_id = kwargs.get('abc')
#     return Status.objects.get(id=kw_id)

# class StatusUpdateAPIView(generics.UpdateAPIView):

#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

# class StatusDeleteAPIView(generics.DestroyAPIView):

#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
