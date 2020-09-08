from django.contrib import admin

from .models import Status

from .forms import StatusForm


class StatusAdmin(admin.ModelAdmin):

    list_display = ['user', '__str__', 'image']

    # class Meta:
    #     model = Status

    form = StatusForm


# Register your models here.

admin.site.register(Status, StatusAdmin)
