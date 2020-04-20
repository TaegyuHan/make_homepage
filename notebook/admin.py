from django.contrib import admin
from . import models


@admin.register(models.Notebook)
class Notebook(admin.ModelAdmin):

    list_display = (
        "updated",
        "category",
        "title",
    )
