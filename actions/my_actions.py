##################################################################################
#  You can add your actions in this file or create any other file in this folder #
##################################################################################

import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MyAction(Action):

    def name(self):
        return 'action_my_action'

    def run(self, dispatcher, tracker, domain):
        # do something.
        return []

"""
class ActionReceiveName(Action):

    def name(self) -> Text:
        return "action_receive_name"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"I'll remember your name {text}.")
        return [SlotSet("name", text)]
"""

class ActionSetEmail(Action):

    def name(self) -> Text:
        return "action_set_email"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        email = tracker.latest_message['email']
        dispatcher.utter_message(text=f"Confirming the email I have is: {email}")
        return [SlotSet("email", email)]

class ActionLeakDBCheck(Action):

    def name(self) -> Text:
        return "action_leak_db_check"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        email = tracker.get_slot("email")
        api_call_results = requests.get(
            f'https://api.weleakinfo.to/api?value={email}&type=email&key=IEMF-RJXT-HEBD-ENDQ')
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
                    print(each.strip())
                if result_length > 3:
                    text = ""
                    for each in all_data:
                        text += each
                    data = {'api_dev_key': 'EiL9ngnoApmKM83C0B88aDE23Ud3uSnN',
                            'api_option': 'paste',  # this will create new paste
                            'api_paste_code': text,  # your actual text you want to paste
                            'api_paste_expire_date': '10M'  # this will make the pastebin link temporary
                            }
                    pastebin = requests.post("https://pastebin.com/api/api_post.php", data=data)
                    dispatcher.utter_message(text=f"You get the picture so rather than me listing all {result_length} of them here's a link with them all" + pastebin.text)
            else:
                dispatcher.utter_message(text="I didn't find anything useful.")
        else:
            dispatcher.utter_message(text="I didn't find anything useful.")


"""
class LeakDBCheck(Action):

    def name(self):
        return 'action_leak_db_check'

    def run(self, dispatcher, tracker, domain):
        email = tracker.latest_message['Email']
        leak_results_raw = requests.get("https://api.weleakinfo.to/api?value=" + email + "&type=email&key=IEMF-RJXT-HEBD-ENDQ")
        leak_results = leak_results_raw
        return leak_results
"""
"""
class ActionLeakDBCheck(Action):

    def name(self) -> Text:
        return "action_leak_db_check"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="This is what I found")
"""