from django.db import models
from core import models as core_models


class Portfolio(core_models.TimeStampedModel):

    title = models.TextField(default="")
    image = models.ImageField(blank=True)
    text = models.TextField(default="")


# Create your models here.
