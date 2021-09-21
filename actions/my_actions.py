##################################################################################
#  You can add your actions in this file or create any other file in this folder #
##################################################################################

import requests
import datetime as dt
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

"""
class ActionMyAction(Action):

    def name(self) -> Text:
        return "action_my_action"

    def run(
            self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # do something.
        return []
"""

class ActionTellTime(Action): #WORKS

    def name(self) -> Text:
        return "action_tell_time"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"The current date and time is {dt.datetime.now()}")

        return []

class ActionSetEmail(Action):

    def name(self) -> Text:
        return "action_set_email"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        email = tracker.latest_message['text']
        #email = tracker.latest_message['entities']
        #email = next(tracker.get_latest_entity_values(“Email”), None)

        if not email:
            dispatcher.utter_message(text="I don't have an email saved.")
        else:
            #ip_address = Filter ip_address input for code injection
            dispatcher.utter_message(text=f"Alright I've got the email: {email}")
        return [SlotSet("slot_email", email)] #Correct. First section is Slot. Second is Python Variable

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

class ActionLeakDBCheck(Action):

    def name(self) -> Text:
        return "action_leak_db_check"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        email = tracker.get_slot("slot_email")
        #email = tracker.latest_message["email"]
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
                    dispatcher.utter_message(text="I found something.") #utters a message in Zenith
                    for each in all_data[:3]: #remove [:3] to check data before creating a pastebin
                        dispatcher.utter_message(each.strip())
                    if result_length > 3:
                        text = ""
                        for each in all_data:
                            text += each
                        data = {'api_dev_key': 'EiL9ngnoApmKM83C0B88aDE23Ud3uSnN',
                                'api_option': 'paste',  # this will create new paste
                                'api_paste_private ': '2',
                                'api_paste_code': text,  # your actual text you want to paste
                                'api_paste_expire_date': '10M'  # this will make the pastebin link temporary
                                }
                        pastebin = requests.post("https://pastebin.com/api/api_post.php", data=data)
                        dispatcher.utter_message(text=f"You get the picture so rather than me listing all {result_length} of them here's a link with them all" + pastebin.text)
                else:
                    dispatcher.utter_message(text="I didn't find anything useful.")
            else:
                dispatcher.utter_message(text="I didn't find anything useful.")

        return []

class ActionSetIP(Action):

    def name(self) -> Text:
        return "action_set_ip"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ip_address = tracker.latest_message['text']#Collect IP Address
        #ip_address = next(tracker.get_latest_entity_values(“IP_Address”), None)
        dispatcher.utter_message(text=f"I've saved the IP Address: {ip_address}") #utter to confirm

        return [SlotSet("slot_ip_address", ip_address)] #First is the Slot, Second is the Python Variable

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
            #ip_address = Filter ip_address input for code injection
            dispatcher.utter_message(text=f"Here's a Shodan search link for that IP Address: https://www.shodan.io/search?query={ip_address}")
        return []

"""

class ActionPersonSearch(Action):

    def name(self) -> Text:
        return "action_person_search"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        name = tracker.get_slot('name')
        #name = Filter ip_address input for code injection
        #name = name.replace(" ", "+")
        dispatcher.utter_message(text=f"Here's a person search link: https://whitepages.com/search?query={name}")


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

"""
class ActionSetName(Action):

    def name(self) -> Text:
        return "action_set_name"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"I'll remember your name {text}.")
        return [SlotSet("name", text)]
"""