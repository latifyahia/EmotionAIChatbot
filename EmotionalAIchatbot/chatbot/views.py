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


# Create your views here.
def home(request):

    r = requests.get('http://localhost:3000/emotion')
    jsonData = r.json()
    emotion = jsonData[0]['currentEmotion']


    return render(request, "home.html")


def chatbox(request):
    return render(request, "chatbox.html")

def about(request):
    return render(request, "about.html")

# Create your views here.
