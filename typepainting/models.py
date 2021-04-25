from django.db import models


# Create your models here.

class TypePainting(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Name",
        help_text="Name",
    )




    class Meta:
        ordering = ["id"]
        verbose_name = "TypePainting",
        verbose_name_plural = "TypePainting"

    def __str__(self):
        return self.name