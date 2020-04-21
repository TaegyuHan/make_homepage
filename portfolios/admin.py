from django.contrib import admin
from . import models


@admin.register(models.Portfolio_note)
class Portfolio_note(admin.ModelAdmin):

    list_display = (
        "created",
        "title",
    )


@admin.register(models.Portfolio_notes_text)
class Language_note(admin.ModelAdmin):

    list_display = (
        "title_text",
        "image",
        "text",
    )
