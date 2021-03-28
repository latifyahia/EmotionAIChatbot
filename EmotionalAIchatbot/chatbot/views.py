import urllib3
import os
import requests
import json
from django.shortcuts import render
from io import BytesIO
import os
from PIL import Image, ImageDraw
import requests

from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import FaceAttributeType
from msrest.authentication import CognitiveServicesCredentials


# Create your views here.
def home(request):

    emotion = request.POST.get('emotions')
    print(emotion)
    return render(request, "home.html")


def chatbox(request):
        return render(request, "chatbox.html")


# Create your views here.

