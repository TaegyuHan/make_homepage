from django.contrib import admin
from . import models


@admin.register(models.Portfolio)
class Portfolio(admin.ModelAdmin):

    list_display = (
        "updated",
        "title",
    )
