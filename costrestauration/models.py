from django.db import models

from categorydamage.models import CategoryDamage
from leveldamage.models import LevelDamage

# Create your models here.
from typepainting.models import TypePainting


class CostRestauration(models.Model):

    level_damage = models.ForeignKey(
        LevelDamage, on_delete=models.DO_NOTHING,
        verbose_name="LevelDamage",
        help_text="LevelDamage",
    )

    category_damage = models.ForeignKey(
        CategoryDamage, on_delete=models.DO_NOTHING,
        verbose_name="CategoryDamage",
        help_text="CategoryDamage",
    )

    type_painting= models.ForeignKey(
        TypePainting, on_delete=models.DO_NOTHING,
        verbose_name="TypePainting",
        help_text="TypePainting",
    )

    cost = models.PositiveBigIntegerField(
        null=False, blank=False,
        default=1, verbose_name="Cost",
        help_text="Cost",
    )

    class Meta:
        ordering=["id"]
        verbose_name="CostRestauration",
        verbose_name_plural="CostRestauration"

    def __str__(self):
        return self.orden.typepainting.name