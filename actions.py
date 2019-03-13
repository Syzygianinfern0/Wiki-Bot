from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import json
import tweepy
import wikipedia

class ActionGetWiki(Action):
    def name(self):
        return "action_get_wiki"

    def run(self, dispatcher, tracker, domain):
        query = tracker.get_slot('wiki_query')

        try:
            query = wikipedia.summary(query)
            query = '.'.join(query.split('.')[:3]) + '.'
            while True:
                s = query.find('(')
                if s is -1:
                    break
                e = query.find(')')
                query = query[:s-1] + query[e+1:]
            dispatcher.utter_message(query)

        except wikipedia.exceptions.PageError as err:
            dispatcher.utter_message("Sorry, I can't wiki that")

        return [SlotSet("wiki", query)]


