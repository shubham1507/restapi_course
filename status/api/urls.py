from django.conf.urls import url
from .views import (
    StatusAPIView,
    #  StatusCreateAPIView,
    StatusDetailAPIView,
    #  StatusUpdateAPIView,
    #  StatusDeleteAPIView
)

urlpatterns = [
    url(r'^$',
        StatusAPIView().as_view()),
    #/api/status/ -> list
    # url(r'^create/$', StatusCreateAPIView.as_view()),
    # #/api/status/create -> create
    url(r'^(?P<pk>\d+)/$', StatusDetailAPIView.as_view()),
    # #/api/status/12/ -> detail
    #  url(r'^(?P<pk>\d+)/update/$', StatusUpdateAPIView.as_view()),
    #/api/status/12/update/ -> update
    #  url(r'^(?P<pk>\d+)/delete/$', StatusDeleteAPIView.as_view()),
    # #/api/status/12/delete/ -> delete
]
