from django.contrib import admin
from . import models


class Portfolio_notes_textInline(admin.TabularInline):

    model = models.Portfolio_notes_text


@admin.register(models.Portfolio_note)
class Portfolio_note(admin.ModelAdmin):

    inlines = (Portfolio_notes_textInline,)

    list_display = (
        "created",
        "title",
    )


@admin.register(models.Portfolio_notes_text)
class Portfolio_notes_text(admin.ModelAdmin):

    list_display = (
        "title_text",
        "image",
        "text",
        "category",
    )
