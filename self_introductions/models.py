from django.db import models
from core import models as core_models


class Self_introductions_note(core_models.TimeStampedModel):

    category = models.ForeignKey(
        "categorys.Category",
        related_name="Self_introductions_note",
        on_delete=models.PROTECT,
    )
    title = models.TextField()

    def __str__(self):
        return self.title


class Self_introductions_notes_text(core_models.TimeStampedModel):

    title_text = models.ForeignKey(
        "Self_introductions_note",
        related_name="Self_introductions_notes_text",
        on_delete=models.CASCADE,
    )

    image = models.ImageField(blank=True)
    text = models.TextField()
