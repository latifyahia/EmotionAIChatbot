# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from urllib import request

from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import FaceAttributeType
from msrest.authentication import CognitiveServicesCredentials
from typing import Any, Text, Dict, List
import os
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import urllib, json


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


        return []

# class EmotionAction(Action):
#
#     def name(self) -> Text:
#         return "emotion_form"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         required_slots = ["emotion"]
#
#         for slot_name in required_slots:
#             if tracker.slots.get(slot_name) is None:
#                 return[SlotSet("requested_slots"), slot_name]
#
#         return[SlotSet("requested_slot"), None]





class ActionEmotionSubmit(Action):


    def name(self) -> Text:
        return "action_submit_emotion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            r = requests.get('http://localhost:3000/emotion')
            jsonData = r.json()
            emotion = jsonData[0]['currentEmotion']
            return [SlotSet("emotion", emotion)]


## Action for joke taken from https://github.com/rgstephens/jokebot/blob/master/actions/actions.py
class ActionRandom(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_random_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            request = json.loads(requests.get("http://api.icndb.com/jokes/random").text)
            joke = request["value"][
                "joke"
            ]  # extract a joke from returned json response
            dispatcher.utter_message(joke)  # send the message back to the user
            return []