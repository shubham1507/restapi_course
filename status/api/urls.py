from django.conf.urls import url
from .views import StatusAPIView

urlpatterns = [
    url(r'^$',
        StatusAPIView().as_view()),
    #/api/status/ -> list
    # url(r'^create/$',
    #     StatusAPICreateView().as_view()),
    # #/api/status/create -> create
    # url(r'^(?<id>.*)/$',
    #     StatusAPIDetailView().as_view()),
    # #/api/status/12/ -> detail
    # url(r'^(?<id>.*)/update/$',
    #     StatusAPIUpdateView().as_view()),
    # #/api/status/12/update/ -> update
    # url(r'^(?<id>.*)/delete/$',
    #     StatusAPIDeleteView().as_view()),
    # #/api/status/12/delete/ -> delete
]
