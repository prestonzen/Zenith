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
        leak_results = requests.get("https://api.weleakinfo.to/api?value=" + email + "&type=email&key=IEMF-RJXT-HEBD-ENDQ")
        return leak_results