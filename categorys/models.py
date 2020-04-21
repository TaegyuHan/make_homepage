from django.db import models
from core import models as core_models


class Category(core_models.TimeStampedModel):

    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category
