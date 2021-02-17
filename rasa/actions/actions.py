# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import FaceAttributeType
from msrest.authentication import CognitiveServicesCredentials
from typing import Any, Text, Dict, List
import os
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class InformationAction(Action):

    def name(self) -> Text:
        return "name_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        required_slots = ["name"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return[SlotSet("requested_slots"), slot_name]

        return[SlotSet("requested_slot"), None]

class ActionSubmit(Action):


    def name(self) -> Text:
        return "action_submit_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_ask_name", Name=tracker.get_slot("name"))

        return []

class InformationAction2(Action):

    def name(self) -> Text:
        return "celebration_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        required_slots = ["celebration"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return[SlotSet("requested_slots"), slot_name]

        return[SlotSet("requested_slot"), None]

class ActionSubmit2(Action):


    def name(self) -> Text:
        return "action_submit_good_day"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_day_response_happy", Celebration=tracker.get_slot("celebration"))

        return []


class EmotionAction(Action):

    def name(self) -> Text:
        return "celebration_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        required_slots = ["emotion"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return[SlotSet("requested_slots"), slot_name]

        return[SlotSet("requested_slot"), None]
    def home(request):
    #- EXAMPLE CODE TAKEN FROM https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/Face/rest/detect.py *
    # This key will serve all examples in this document.
        KEY = "d814559c8ef445b5abb3e834eb7de8e9"

        # This endpoint will be used in all examples in this quickstart.
        ENDPOINT = "https://emotionalfacialazure.cognitiveservices.azure.com/"

        face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

        # Image of face(s)
        face1_url = 'https://media-exp1.licdn.com/dms/image/C5603AQGQQIx5sDcX4A/profile-displayphoto-shrink_200_200/0/1587739656825?e=1616025600&v=beta&t=teG4BtNkF89RJRQijlleL7pRcaUkCNTfUebxx3vmHx0'
        face2_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/The_famous_mustache_and_goatee.jpg/220px-The_famous_mustache_and_goatee.jpg'

        # List of url images
        url_images = [face1_url, face2_url]

        # Attributes you want returned with the API call, a list of FaceAttributeType enum (string format)
        face_attributes = ['age', 'gender', 'emotion']

        # Detect a face with attributes, returns a list[DetectedFace]
        for image in url_images:
            detected_faces = face_client.face.detect_with_url(url=image, return_face_attributes=face_attributes)
            if not detected_faces:
                raise Exception(
                    'No face detected from image {}'.format(os.path.basename(image)))

            # Face IDs are used for comparison to faces (their IDs) detected in other images.
            for face in detected_faces:
                print()
                print('Detected face ID from', os.path.basename(image), ':')
                # ID of detected face
                print(face.face_id)
                # Show all facial attributes from the results
                print()
                print('Facial attributes detected:')
                print('Age: ', face.face_attributes.age)
                print('Gender: ', face.face_attributes.gender)
                print('Emotion: ')
                print('\tAnger: ', face.face_attributes.emotion.anger)
                print('\tContempt: ', face.face_attributes.emotion.contempt)
                print('\tDisgust: ', face.face_attributes.emotion.disgust)
                print('\tFear: ', face.face_attributes.emotion.fear)
                print('\tHappiness: ', face.face_attributes.emotion.happiness)
                print('\tNeutral: ', face.face_attributes.emotion.neutral)
                print('\tSadness: ', face.face_attributes.emotion.sadness)
                print('\tSurprise: ', face.face_attributes.emotion.surprise)
                print()

class EmotionActionSubmit(Action):


    def name(self) -> Text:
        return "action_submit_emotion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        return []

