from django.db import models
from core import models as core_models


class Portfolio_note(core_models.TimeStampedModel):

    category = models.ForeignKey(
        "categorys.Category", related_name="Portfolio_note", on_delete=models.PROTECT
    )
    title = models.TextField()

    def __str__(self):
        return self.title


class Portfolio_notes_text(core_models.TimeStampedModel):

    title_text = models.ForeignKey(
        "Portfolio_note", related_name="Portfolio_notes_text", on_delete=models.CASCADE
    )

    image = models.ImageField(blank=True)
    text = models.TextField()
