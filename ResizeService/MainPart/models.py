from typing import Any
from django.db import models

class ImagesConsolidation(models.Model):
    original_url = models.URLField(verbose_name="Путь до оригинала")


class ImageModel(models.Model):
    original_image = models.ForeignKey(ImagesConsolidation, on_delete=models.CASCADE, verbose_name="Оригинальное изображение")
    url = models.URLField(verbose_name="Путь до изображения")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
