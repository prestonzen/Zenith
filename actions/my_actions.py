##################################################################################
#  You can add your actions in this file or create any other file in this folder #
##################################################################################

import requests
import datetime as dt
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import time

"""
#For Upcoming Voice Support Feature
import speech_recognition as sr
import subprocess
from gtts import gTTS
from translate import Translator
"""

"""
class ActionExampleAction(Action):

    def name(self) -> Text:
        return "action_my_action" #lower case

    def run(
            self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # do something.
        return []
"""


# Slot Set Actions

class ActionSetIP(Action):

    def name(self) -> Text:
        return "action_set_ip"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ip_address = tracker.latest_message['text']  # Collect IP Address
        # ip_address = next(tracker.get_latest_entity_values(“IP_Address”), None)
        dispatcher.utter_message(text=f"I've saved the IP Address: {ip_address}")  # utter to confirm

        return [SlotSet("slot_ip_address", ip_address)]  # First is the Slot, Second is the Python Variable

class ActionSetEmail(Action):

    def name(self) -> Text:
        return "action_set_email"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        email = tracker.latest_message['text']
        # email = tracker.latest_message['entities']
        # email = next(tracker.get_latest_entity_values(“Email”), None)

        if not email:
            dispatcher.utter_message(text="I don't have an email saved.")
        else:
            # ip_address = Filter ip_address input for code injection
            # As long as I don't bind mount local files into docker then code injection is relatively isolated
            dispatcher.utter_message(text=f"Alright I've got the email: {email}")
        return [SlotSet("slot_email", email)]  # Correct. First section is Slot. Second is Python Variable

class ActionSetDomain(Action):

    def name(self) -> Text:
        return "action_set_domain"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        domain = tracker.latest_message['text']  # Collect data from user input
        dispatcher.utter_message(text=f"I've saved the domain: {domain}")  # utter to confirm

        return [SlotSet("slot_domain", domain)]  # First is the Slot, Second is the Python Variable

class ActionSetUsername(Action):

    def name(self) -> Text:
        return "action_set_username"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        username = tracker.latest_message['text']
        dispatcher.utter_message(text=f"I'll remember the username {username}.")
        return [SlotSet("slot_username", username)]

class ActionSetCVE(Action):

    def name(self) -> Text:
        return "action_set_cve"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        cve = tracker.latest_message['text']  # Collect CVE
        # ip_address = next(tracker.get_latest_entity_values(“IP_Address”), None)
        dispatcher.utter_message(text=f"I've saved the CVE: {cve}")  # utter to confirm

        return [SlotSet("slot_cve", cve)]  # First is the Slot, Second is the Python Variable

### General Functions ###

class ActionTellTime(Action):  # WORKS

    def name(self) -> Text:
        return "action_tell_time"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f"The current date and time is {dt.datetime.now()}")

        return []

class ActionTellJoke(Action):  # WORKS

    def name(self) -> Text:
        return "action_tell_joke"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = "https://jokes10.p.rapidapi.com/random"
        headers = {
            'x-rapidapi-host': "jokes10.p.rapidapi.com",
            'x-rapidapi-key': ""
        }

        jokeresponse = requests.request("GET", url, headers=headers)
        jokeJSON = (jokeResponse.json())  # Stores a variable named jokeJSON with the value of the request response formatted as a JSON
        dispatcher.utter_message(jokeJSON[0]["joke_text"])  # prints the jokeJSON variable's 1st dictionary (Zero indexed) then looks for the key "joke_text"
        time.sleep(3)
        dispatcher.utter_message(jokeJSON[0]["joke_punchline"])  # prints the jokeJSON variable's 1st dictionary (Zero indexed) then looks for the key "joke_punchline"
        return []

### Checks ###

class ActionLeakDBCheck(Action):

    def name(self) -> Text:
        return "action_leak_db_check"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        email = tracker.get_slot("slot_email")
        # email = tracker.latest_message["email"]
        if not email:
            dispatcher.utter_message(text="I don't have an email to check.")
        else:
            api_call_results = requests.get(
                f'https://api.weleakinfo.to/api?value={email}&type=email&key=')
            dict_result = api_call_results.json()
            if dict_result['success']:
                if dict_result['found'] > 0:
                    all_data = []
                    for each in dict_result['result']:
                        text = ""
                        line = each['line'].split(":")
                        text += "Email: "
                        text += line[0] + '\n'
                        text += "Password: "
                        if len(line) > 1:
                            text += line[1] + '\n'
                        else:
                            continue
                        text += "Source: "
                        if len(each['sources']) > 0:
                            for i in range(len(each['sources'])):
                                if i == len(each['sources']) - 1:
                                    text += each['sources'][i]
                                else:
                                    text += each['sources'][i] + ", "
                            text += '\n'
                        else:
                            text += 'Unknown\n'
                        text += "-" * 20 + '\n'
                        all_data.append(text)
                    result_length = len(all_data)
                    dispatcher.utter_message(text="I found something.")  # utters a message in Zenith
                    for each in all_data[:3]:  # remove [:3] to check data before creating a pastebin
                        dispatcher.utter_message(each.strip())
                    if result_length > 3:
                        text = ""
                        for each in all_data:
                            text += each
                        data = {'api_dev_key': '',
                                'api_option': 'paste',  # this will create new paste
                                'api_paste_private ': '2',
                                'api_paste_code': text,  # your actual text you want to paste
                                'api_paste_expire_date': '10M'  # this will make the pastebin link temporary
                                }
                        pastebin = requests.post("https://pastebin.com/api/api_post.php", data=data)
                        dispatcher.utter_message(
                            text=f"You get the picture so rather than me listing all {result_length} of them here's a link with them all" + pastebin.text)
                else:
                    dispatcher.utter_message(text="I didn't find anything useful.")
            else:
                dispatcher.utter_message(text="I didn't find anything useful.")

        return []

class ActionShodanCheck(Action):

    def name(self) -> Text:
        return "action_shodan_check"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ip_address = tracker.get_slot("slot_ip_address")
        if not ip_address:
            dispatcher.utter_message(text="I don't have an IP Address to check.")
        else:
            # ip_address = Filter ip_address input for code injection
            dispatcher.utter_message(
                text=f"Here's a Shodan search link for that IP Address: https://www.shodan.io/search?query={ip_address}")
        return []

class ActionUsernameCheck(Action):

    def name(self) -> Text:
        return "action_username_check"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        uname = tracker.get_slot('slot_username')
        # name = Filter ip_address input for code injection
        # name = name.replace(" ", "+")
        dispatcher.utter_message(text="Here's are some username search links.")
        dispatcher.utter_message(text="You'll need to type that username into this site: https://checkusernames.com")
        dispatcher.utter_message(text=f"https://knowem.com/checkusernames.php?u={uname}")
        dispatcher.utter_message(text="You'll need to manually type into this one as well: https://namechk.com/")

        return []

class ActionSearchCVE(Action):

    def name(self) -> Text:
        return "action_search_cve"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        cve = tracker.get_slot("slot_cve")
        if not cve:
            dispatcher.utter_message(text="I don't have a CVE to check.")
        else:
            # ip_address = Filter ip_address input for code injection
            dispatcher.utter_message(
                text=f"Here's a OpenCVE search link: https://www.opencve.io/cve?cvss=&search={cve}")
        return []


"""
class ActionWordpressVulns

    def name(self) -> Text:
        return "action_wordpress_vulns"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #url = tracker.get_slot('slot_domain')
        #requests.get(url)
        #if reply = 200:
            #dispatcher.utter_message(text=f"{url} is open to wp-content/uploads access.")
            #dispatcher.utter_message(text=f"Here's the link to access their site files: {url}/wp-content/uploads.")
        #else:
            #dispatcher.utter_message(text=f"{url} isn't open to wp-content/uploads access.")
"""

"""
class ActionUtterEmail(Action):

    def name(self) -> Text:
        return "action_utter_email"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        email = tracker.get_slot('email')
        if not email:
            dispatcher.utter_message(text="I don't have an email saved.")
        else:
            #ip_address = Filter ip_address input for code injection
            dispatcher.utter_message(text=f"The email I have for you is: {email}")
            #dispatcher.utter_message("This is another way to output text with multi variables. Variable 1 is {} and Variable 2 is {}".format)variable1, variable2))
        return []
"""

"""
class ActionIPCheck(Action): #Works Syntactically but not via intent

    def name(self) -> Text:
        return "action_ip_check"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        ip = requests.get("https://api.ipify.org")
        ip_text = (ip.text)
        dispatcher.utter_message(text=f"Your IP is: {ip_text}")
        #return [SlotSet("ip_address", user_ip)]


"""

"""
class ActionVirustotalCheck(Action):

    def name(self) -> Text:
        return "action_virustotal_check"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ip_address = tracker.get_slot('ip_address')
        #ip_address = Filter ip_address input for code injection
        dispatcher.utter_message(text=f"Here's what I found for that IP address: Virus Total Results from X# of Vendors")
        return []

"""
