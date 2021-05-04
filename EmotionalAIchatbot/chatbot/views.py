import urllib
import urllib, json
import urllib3
import os
import requests
from django.contrib.auth.decorators import login_required
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

def lolly(request):
    return render(request, "lolly.html")

def about(request):
    return render(request, "about.html")

@login_required(login_url='login')
def profile(request):

    userEmotions = {
        'happy': 0,
        'sad': 0,
        'angry': 0,
        'neutral': 0,
        'fearful': 0,
        'surprised': 0,
        'disgusted': 0,
        'userName': '',
        'firstName': '',
        'lastName':'',
        'emailAddress':'',
        'dateJoined': '',
        'lastLogin': '',
    }
    current_user = request.user
    userData = UserData.objects.all()
    userEmotions['userName'] = str(current_user.username)
    userEmotions['firstName'] = str(current_user.first_name)
    userEmotions['lastName'] = str(current_user.last_name)
    userEmotions['emailAddress'] = str(current_user.email)
    dateJoined = str(current_user.date_joined)
    lastLogin = str(current_user.last_login)

    dateJoinedParsed = dateJoined[0:10]
    lastLoginParsed = lastLogin[0:10]

    userEmotions['dateJoined'] = dateJoinedParsed
    userEmotions['lastLogin'] = lastLoginParsed

    print(userEmotions['userName'])

    for data in userData:
        emotion = data
        if(str(emotion.user) == str(current_user)):
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

    return render(request, "data.html", {'userEmotions':userEmotions})
