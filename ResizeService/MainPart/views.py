import datetime
import os
import re
from io import BytesIO

import requests
from django.conf import settings
from django.shortcuts import render
from PIL import Image

from .forms import InsertImagesForm
from .models import ImageModel, ImagesConsolidation


def index(request):
    if request.method == "POST":
        form = InsertImagesForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            urls = re.split(r"https?://", form_data["urls"])
            urls.pop(0)
            result_urls = []
            erroneous_urls = []
            for _ in range(len(urls)):
                urls[_] = "https://" + urls[_]
                if not re.search(r"(\.png|\.jpg|\.jpeg|\.gif|\.raw|\.tiff|\.tif|\.JPG|\.PNG|\.JPEG)$", urls[_]):
                    return render(request=request, template_name="result.html", context={
                        "invalid_url": urls[_]
                    })
                ImagesConsolidation.objects.create(
                    original_url=urls[_]
                )
                response = requests.get(urls[_])
                if(response.ok):
                    image = Image.open(BytesIO(response.content))
                    if form_data["is_choose_resolution"]:
                        new_image = image.resize((
                            form_data["height"] if form_data["height"] else 1200,
                            form_data["weight"] if form_data["weight"] else 1200
                        ))
                    else:
                        new_image = image.resize((1200, 1200))
                    storage_media_path = settings.MEDIA_ROOT + datetime.datetime.now(
                        tz=datetime.UTC
                    ).strftime("%Y%m%d")
                    if not os.path.exists(path=storage_media_path):
                        os.mkdir(path=storage_media_path)
                    result_image_path = storage_media_path + "/" + re.search(r"(?<=\/)[^\/]+(?=\.png|\.jpg|\.jpeg|\.gif|\.raw|\.tiff|\.tif|\.JPG|\.PNG|\.JPEG)", urls[_]).group() + ".png" #Raw форматы не обрабатываются, можно добавить
                    if new_image.mode != "RGB":
                        new_image = new_image.convert("RGB")
                    new_image.save(result_image_path)
                    ImageModel.objects.create(
                        original_image_id=ImagesConsolidation.objects.last().id,
                        url=result_image_path
                    )
                    result_urls.append(ImageModel.objects.filter(
                        original_image__original_url=urls[_]
                    ).last().url)
                else:
                    erroneous_urls.append(urls[_])
            return render(request=request, template_name="result.html", context={
                "erroneous_urls": erroneous_urls,
                "host": "https://" + request.get_host() + "/",
                "result_urls": result_urls
            })
    else:
        return render(request=request, template_name="index.html", context={
            "form": InsertImagesForm(request.POST)
        })
