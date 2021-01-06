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

    # This key will serve all examples in this document.
    KEY = "cae5a86bdf7942608dc7b54a9a65f238"

    # This endpoint will be used in all examples in this quickstart.
    ENDPOINT = "https://emotionalaichatbot.cognitiveservices.azure.com/"

    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

    # Detect a face in an image that contains a single face
    single_face_image_url = 'https://www.biography.com/.image/t_share/MTQ1MzAyNzYzOTgxNTE0NTEz/john-f-kennedy---mini-biography.jpg'
    single_image_name = os.path.basename(single_face_image_url)
    # We use detection model 2 because we are not retrieving attributes.
    detected_faces = face_client.face.detect_with_url(url=single_face_image_url, detectionModel='detection_02')
    if not detected_faces:
        raise Exception('No face detected from image {}'.format(single_image_name))

    # Display the detected face ID in the first single-face image.
    # Face IDs are used for comparison to faces (their IDs) detected in other images.
    print('Detected face ID from', single_image_name, ':')
    for face in detected_faces: print (face.face_id)
    print()

    # Save this ID for use in Find Similar
    first_image_face_ID = detected_faces[0].face_id

    # Detect a face in an image that contains a single face
    single_face_image_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
    single_image_name = os.path.basename(single_face_image_url)
    # We use detection model 2 because we are not retrieving attributes.
    detected_faces = face_client.face.detect_with_url(url=single_face_image_url, detectionModel='detection_02')
    if not detected_faces:
        raise Exception('No face detected from image {}'.format(single_image_name))

    # Convert width height to a point in a rectangle
    def getRectangle(faceDictionary):
        rect = faceDictionary.face_rectangle
        left = rect.left
        top = rect.top
        right = left + rect.width
        bottom = top + rect.height

        return ((left, top), (right, bottom))


    # Download the image from the url
    response = requests.get(single_face_image_url)
    img = Image.open(BytesIO(response.content))

    # For each face returned use the face rectangle and draw a red box.
    print('Drawing rectangle around face... see popup for results.')
    draw = ImageDraw.Draw(img)
    for face in detected_faces:
        draw.rectangle(getRectangle(face), outline='red')

    # Display the image in the users default image browser.
    img.show()
    return render(request, "home.html")
