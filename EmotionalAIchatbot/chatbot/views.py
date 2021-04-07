import urllib
import urllib, json
import urllib3
import os
import requests
from django.shortcuts import render
from io import BytesIO
import os
from PIL import Image, ImageDraw
import requests
from django.http import JsonResponse
from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import FaceAttributeType
from msrest.authentication import CognitiveServicesCredentials


# Create your views here.
def home(request):

    r = requests.get('http://localhost:3000/emotion')
    jsonData = r.json()
    emotion = jsonData[0]['currentEmotion']


    return render(request, "home.html")


def chatbox(request):
    return render(request, "chatbox.html")

# Create your views here.
