import uuid
from functools import lru_cache

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy


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


class XcelerateBaseModel(CTModel):
    updated_at = models.DateTimeField(
        verbose_name=ugettext_lazy("Updated at"), auto_now_add=True, null=True
    )
    created_at = models.DateTimeField(
        verbose_name=ugettext_lazy("Created at"), auto_now=True, null=True
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs) -> None:
        if "update_fields" in kwargs:
            update_fields = kwargs.get("update_fields") or []
            if "updated_at" not in update_fields:
                kwargs["update_fields"].append("updated_at")

        super().save(*args, **kwargs)


class XcelerateUUIDBaseModel(XcelerateBaseModel):
    uuid = models.CharField(
        verbose_name=ugettext_lazy("UUID"), unique=True, default=generate_uuid4
    )

    def __hash__(self) -> int:
        return hash(self.uuid)

    class meta:
        abstract = True

    def __str__(self):
        return self.uuid
