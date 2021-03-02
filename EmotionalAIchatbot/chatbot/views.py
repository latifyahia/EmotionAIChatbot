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

    print(request.GET);
    # #- EXAMPLE CODE TAKEN FROM https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/Face/rest/detect.py *
    # # This key will serve all examples in this document.
    # KEY = "d814559c8ef445b5abb3e834eb7de8e9"
    #
    # # This endpoint will be used in all examples in this quickstart.
    # ENDPOINT = "https://emotionalfacialazure.cognitiveservices.azure.com/"
    #
    # face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
    #
    # # Image of face(s)
    # face1_url = 'https://media-exp1.licdn.com/dms/image/C5603AQGQQIx5sDcX4A/profile-displayphoto-shrink_200_200/0/1587739656825?e=1616025600&v=beta&t=teG4BtNkF89RJRQijlleL7pRcaUkCNTfUebxx3vmHx0'
    # face2_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/The_famous_mustache_and_goatee.jpg/220px-The_famous_mustache_and_goatee.jpg'
    #
    # # List of url images
    # url_images = [face1_url, face2_url]
    #
    # # Attributes you want returned with the API call, a list of FaceAttributeType enum (string format)
    # face_attributes = ['age', 'gender', 'emotion']
    #
    # # Detect a face with attributes, returns a list[DetectedFace]
    # for image in url_images:
    #     detected_faces = face_client.face.detect_with_url(url=image, return_face_attributes=face_attributes)
    #     if not detected_faces:
    #         raise Exception(
    #             'No face detected from image {}'.format(os.path.basename(image)))
    #
    #     # Face IDs are used for comparison to faces (their IDs) detected in other images.
    #     for face in detected_faces:
    #         print()
    #         print('Detected face ID from', os.path.basename(image), ':')
    #         # ID of detected face
    #         print(face.face_id)
    #         # Show all facial attributes from the results
    #         print()
    #         print('Facial attributes detected:')
    #         print('Age: ', face.face_attributes.age)
    #         print('Gender: ', face.face_attributes.gender)
    #         print('Emotion: ')
    #         print('\tAnger: ', face.face_attributes.emotion.anger)
    #         print('\tContempt: ', face.face_attributes.emotion.contempt)
    #         print('\tDisgust: ', face.face_attributes.emotion.disgust)
    #         print('\tFear: ', face.face_attributes.emotion.fear)
    #         print('\tHappiness: ', face.face_attributes.emotion.happiness)
    #         print('\tNeutral: ', face.face_attributes.emotion.neutral)
    #         print('\tSadness: ', face.face_attributes.emotion.sadness)
    #         print('\tSurprise: ', face.face_attributes.emotion.surprise)
    #         print()
    #
    #     # Convert width height to a point in a rectangle
    #     def getRectangle(faceDictionary):
    #         rect = faceDictionary.face_rectangle
    #         left = rect.left
    #         top = rect.top
    #         right = left + rect.width
    #         bottom = top + rect.height
    #
    #         return ((left, top), (right, bottom))
    #
    #     # Download the image from the url, so can display it in popup/browser
    #     response = requests.get(image)
    #     img = Image.open(BytesIO(response.content))
    #
    #     # For each face returned use the face rectangle and draw a red box.
    #     print('Drawing rectangle around face... see popup for results.')
    #     print()
    #     draw = ImageDraw.Draw(img)
    #     for face in detected_faces:
    #         draw.rectangle(getRectangle(face), outline='red')
    return render(request, "home.html")


def chatbox(request):
        return render(request, "chatbox.html")


# Create your views here.

