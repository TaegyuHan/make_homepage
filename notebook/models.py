from django.db import models
from core import models as core_models
from category import models as category_models


class Notebook(core_models.TimeStampedModel):

    title = models.TextField(default="")
    category = models.ForeignKey(
        category_models.Categorycode, related_name="notebook", on_delete=models.CASCADE
    )
    image = models.ImageField(blank=True)
    text = models.TextField(default="")
