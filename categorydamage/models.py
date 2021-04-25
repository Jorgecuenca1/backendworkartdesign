from django.db import models


# Create your models here.

class CategoryDamage(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Name",
        help_text="Name",
    )
    color = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Color",
        help_text="Color",
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "CategoryDamage",
        verbose_name_plural = "CategoryDamage"

    def __str__(self):
        return self.name
