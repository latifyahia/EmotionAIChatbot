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
from EmotionalAIChatbot import EmotionAIChatbot


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


class EmotionAction(Action):

    def name(self) -> Text:
        return "emotion_form"



    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        required_slots = ["emotion"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return[SlotSet("requested_slots"), slot_name]

        def getEmotion(request)
            emotion = request.POST.get('emotions')


        return[SlotSet("requested_slot"), None]

