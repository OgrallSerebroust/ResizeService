import datetime
import re
import requests
import os
import random
from django.conf import settings
from django.shortcuts import render
from io import BytesIO
from PIL import Image
from .forms import InsertImagesForm
from .models import ImagesConsolidation, ImageModel

def index(request):
    if request.method == "POST":
        form = InsertImagesForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            urls = re.split("http.:\/\/", form_data["urls"])
            urls.pop(0)
            result_urls = []
            for _ in range(len(urls)):
                urls[_] = "https://" + urls[_]
                ImagesConsolidation.objects.create(
                    original_url=urls[_]
                )
                response = requests.get(urls[_])
                image = Image.open(BytesIO(response.content))
                if form_data["is_choose_resolution"]:
                    new_image = image.resize((
                        form_data["height"] if form_data["height"] else 1200,
                        form_data["weight"] if form_data["weight"] else 1200
                    ))
                else:
                    new_image = image.resize((1200, 1200))
                storage_media_path = settings.MEDIA_ROOT + datetime.datetime.now().strftime("%Y%m%d")
                if not os.path.exists(path=storage_media_path):
                    os.mkdir(path=storage_media_path)
                result_image_path = storage_media_path + "/" + str(random.randint(1, 999999)) + ".png"
                new_image.save(result_image_path)
                ImageModel.objects.create(
                    original_image_id=ImagesConsolidation.objects.last().id,
                    url=result_image_path
                )
                result_urls.append(ImageModel.objects.filter(
                    original_image__original_url=urls[_]
                ).last().url)
            return render(request=request, template_name="result.html", context={
                "host": "https://" + request.get_host() + "/",
                "result_urls": result_urls
            })
    else:
        return render(request=request, template_name="index.html", context={
            "form": InsertImagesForm(request.POST)
        })
