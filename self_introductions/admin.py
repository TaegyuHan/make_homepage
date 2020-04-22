from django.contrib import admin
from . import models


class Self_introductions_noteInline(admin.TabularInline):

    model = models.Self_introductions_notes_text


@admin.register(models.Self_introductions_note)
class Self_introductions_note(admin.ModelAdmin):

    inlines = (Self_introductions_noteInline,)

    list_display = (
        "created",
        "title",
    )


@admin.register(models.Self_introductions_notes_text)
class Self_introductions_notes_text(admin.ModelAdmin):

    list_display = (
        "title_text",
        "image",
        "text",
        "category",
    )
