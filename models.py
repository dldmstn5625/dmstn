from django.db import models
from core import models as core_models


class Book(core_models.TimeStampedModel):

    """ Book Model Definition """

    title = models.CharField(max_length=120)
    year = models.IntegerField()
    cover_image = models.ImageField(default="", null=True)
    rating = models.FloatField(
        default="",
    )
    categories = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="books",
        default="",
    )

    def __str__(self):
        return self.title


# Create your models here.
