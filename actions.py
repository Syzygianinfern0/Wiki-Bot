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
            
            ret = ''
            skip1c = 0
            skip2c = 0
            for i in query:
                if i == '(':
                    skip1c += 1
                elif i == ')'and skip2c > 0:
                    skip2c -= 1
                elif skip1c == 0 and skip2c == 0:
                    ret += i
                    
            dispatcher.utter_message(ret)

        except wikipedia.exceptions.PageError as err:
            dispatcher.utter_message("Sorry, I can't wiki that")

        return [SlotSet("wiki", query)]


