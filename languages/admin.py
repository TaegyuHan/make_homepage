from django.contrib import admin
from django.db.models import Count
from . import models


@admin.register(models.Language)
class Language(admin.ModelAdmin):

    list_display = (
        "category",
        "language",
    )


class Language_notes_textInline(admin.TabularInline):

    model = models.Language_notes_text


@admin.register(models.Language_note)
class Language_note(admin.ModelAdmin):

    inlines = (Language_notes_textInline,)

    list_display = (
        "created",
        "language_note",
        "title",
        "category",
    )


@admin.register(models.Language_notes_text)
class Language_notes_text(admin.ModelAdmin):

    list_display = (
        "created",
        "title_text",
        "image",
        "text",
    )
