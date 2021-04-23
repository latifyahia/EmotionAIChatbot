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
from .models import UserData
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request, "home.html")

def updateEmotions(request):
    current_user = request.user
    data = {'success': False}
    if request.method=='POST':
        emotion = request.POST.get('emotion')
        dataUser = UserData();
        dataUser.user = current_user;
        dataUser.emotion = emotion
        dataUser.save()
        data['success'] = True
    return JsonResponse(data)

def chatbox(request):
    return render(request, "chatbox.html")

def about(request):
    return render(request, "about.html")

def profile(request):

    userEmotions = {
        'happy': 0,
        'sad': 0,
        'angry': 0,
        'neutral': 0,
        'fearful': 0,
        'surprised': 0,
        'disgusted': 0,
    }
    current_user = request.user
    userData = UserData.objects.all()

    for data in userData:
        emotion = data
        if(str(emotion.user) == str(current_user)):
            print(emotion)
            if(str(emotion) == 'Happy'):
                userEmotions['happy'] += 1

            elif(str(emotion) == 'Sad'):
                userEmotions['sad'] += 1

            elif(str(emotion) == 'Angry'):
                userEmotions['angry'] += 1

            elif(str(emotion) == 'Neutral'):
                userEmotions['neutral'] += 1

            elif(str(emotion) == 'Fearful'):
                userEmotions['fearful'] += 1

            elif(str(emotion) == 'Surprised'):
                userEmotions['surprised'] += 1

            elif(str(emotion) == 'Disgusted'):
                userEmotions['disgusted'] += 1


    # userDataName = userData.user
    # print(userData.user)
    print(userEmotions)
    return render(request, "data.html", {'userEmotions':userEmotions})
