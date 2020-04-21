from django.db import models
from core import models as core_models


class Language(core_models.TimeStampedModel):

    category = models.ForeignKey(
        "categorys.Category", related_name="language", on_delete=models.PROTECT
    )
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.language


class Language_note(core_models.TimeStampedModel):

    language_note = models.ForeignKey(
        "Language", related_name="language_note", on_delete=models.PROTECT
    )
    title = models.TextField()

    def __str__(self):
        return self.title


class Language_notes_text(core_models.TimeStampedModel):

    title_text = models.ForeignKey(
        "Language_note", related_name="Language_notes_text", on_delete=models.CASCADE
    )

    image = models.ImageField(blank=True)
    text = models.TextField()
