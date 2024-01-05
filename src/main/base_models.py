import uuid
from functools import lru_cache

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _


def generate_uuid4() -> str:
    return uuid.uuid4().hex


class CTModel(models.Model):
    @staticmethod
    @lru_cache
    def _ct(model) -> ContentType:
        return ContentType.objects.get_for_model(model)

    @classmethod
    def ct(cls) -> ContentType:
        return cls._ct(cls)

    class Meta:
        abstract = True


class XcelerateCommonBaseModel(CTModel):
    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"), auto_now_add=True, null=True
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created at"), auto_now=True, null=True
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs) -> None:
        if "update_fields" in kwargs:
            update_fields = kwargs.get("update_fields") or []
            if "updated_at" not in update_fields:
                kwargs["update_fields"].append("updated_at")

        super().save(*args, **kwargs)


class XcelerateUUIDBaseModel(XcelerateCommonBaseModel):
    uuid = models.CharField(
        verbose_name=_("UUID"),
        editable=True,
        unique=True,
        default=generate_uuid4,
        max_length=42,
    )

    class Meta:
        abstract = True

    def __hash__(self) -> int:
        return hash(self.uuid)

    def __str__(self):
        return self.uuid
