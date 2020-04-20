from django.contrib import admin
from . import models


@admin.register(models.Categorycode)
class Categorycode(admin.ModelAdmin):

    list_display = (
        "updated",
        "category",
    )

