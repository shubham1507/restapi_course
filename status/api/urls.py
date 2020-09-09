from django.conf.urls import url
from .views import (StatusAPIView, StatusCreateAPIView, StatusDetailAPIView)

urlpatterns = [
    url(r'^$',
        StatusAPIView().as_view()),
    #/api/status/ -> list
    url(r'^create/$', StatusCreateAPIView.as_view()),
    # #/api/status/create -> create
    url(r'^(?P<pk>.*)/$', StatusDetailAPIView.as_view()),
    # #/api/status/12/ -> detail
    # url(r'^(?<id>.*)/update/$',
    #     StatusAPIUpdateView().as_view()),
    # #/api/status/12/update/ -> update
    # url(r'^(?<id>.*)/delete/$',
    #     StatusAPIDeleteView().as_view()),
    # #/api/status/12/delete/ -> delete
]
