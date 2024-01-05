from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from main.base_models import XcelerateUUIDBaseModel


class ArchExample(XcelerateUUIDBaseModel):
    test_name = models.CharField(verbose_name=_("Test name"), null=True, max_length=255)
    test_age = models.IntegerField(
        verbose_name=_("Test age"),
        null=True,
        validators=[MaxValueValidator(130), MinValueValidator(0)],
    )

    class meta:
        db_table = "xcelerate_archexample"
        verbose_name = _("Arch Example")
        verbose_name_plural = _("Arch Examples")
