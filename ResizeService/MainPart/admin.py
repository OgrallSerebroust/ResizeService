from django.contrib import admin
from .models import ImageModel, ImagesConsolidation

class ImageAdmin(admin.ModelAdmin):
    list_display = ["url",]

class ImagesConsolidationAdmin(admin.ModelAdmin):
    list_display = ["original_url"]

admin.site.register(ImageModel, ImageAdmin)
admin.site.register(ImagesConsolidation, ImagesConsolidationAdmin)
