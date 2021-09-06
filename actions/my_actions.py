##################################################################################
#  You can add your actions in this file or create any other file in this folder #
##################################################################################

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, ReminderScheduled, ConversationPaused, ConversationResumed, FollowupAction, Restarted, ReminderScheduled
import requests

class MyAction(Action):

    def name(self):
        return 'action_my_action'

    def run(self, dispatcher, tracker, domain):
        # do something.
        return []

class LeakDBCheck(Action):

    def name(self):
        return 'action_leak_db_check'

    def run(self, dispatcher, tracker, domain):
        email = tracker.latest_message['Email']
        leak_results_raw = requests.get("https://api.weleakinfo.to/api?value=" + email + "&type=email&key=IEMF-RJXT-HEBD-ENDQ")
        leak_results = leak_results_raw
        return leak_results
"""
import requests

api_call_results = requests.get(
    'https://api.weleakinfo.to/api?value=test12456&type=email&key=IEMF-RJXT-HEBD-ENDQ')

result = api_call_results.json()
#print(result)

if result['found'] > 0:
    all_data = []
    for each in result['result']:
        text = ""
        line = each['line'].split(":")

        text += "Email: "
        text += line[0] + '\n'

        text += "Password: "
        text += line[1] + '\n'

        text += "Source: "
        if len(each['sources']) > 0:
            for i in each['sources']:
                text += i
            text += '\n'
        else:
            text += 'Unknown\n'
        text += "\n"
        
        all_data.append(text)
    print(f"I found {len(all_data)} records and they are:")

    for each in all_data:
        print(each)
    if len(all_data) > 3:
        print(
            f"You get the picture. There are {len(all_data)} in total so instead of me listing "
            f"them all here, this is a link with the rest.")
        temp = ""
        
        for each in all_data:
            temp += each
            
        pastebin = requests.post("https://pastebin.com/api/api_post.php", data=temp)

else:
    print("No passwords were found 👍")

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