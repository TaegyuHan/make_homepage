from django.contrib import admin
from django.db.models import Count
from . import models


@admin.register(models.Language)
class Language(admin.ModelAdmin):

    list_display = (
        "category",
        "language",
    )


@admin.register(models.Language_note)
class Language_note(admin.ModelAdmin):

    list_display = (
        "created",
        "language_note",
        "title",
    )


@admin.register(models.Language_notes_text)
class Language_notes_text(admin.ModelAdmin):

    list_display = (
        "created",
        "title_text",
        "image",
        "text",
    )
