from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/updates/', include('updates.api.urls')),
    # url(r'^json/cbv/$', JsonCBV.as_view()),
    # url(r'^json/cbv2/$', JsonCBV2.as_view()),
    # url(r'^json/example/$', json_example_view),
    # url(r'^json/serialized/list/$', SerializedListView.as_view()),
    # url(r'^json/serialized/detail/$', SerializedDetailView.as_view())
]
