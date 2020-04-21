from django.contrib import admin
from . import models


@admin.register(models.Self_introductions_note)
class Portfolio_note(admin.ModelAdmin):

    list_display = (
        "created",
        "title",
    )


@admin.register(models.Self_introductions_notes_text)
class Language_note(admin.ModelAdmin):

    list_display = (
        "title_text",
        "image",
        "text",
    )
