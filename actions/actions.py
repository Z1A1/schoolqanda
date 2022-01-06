from typing import Any, Text, Dict, List
from databaseintegeration import DataUpdate
#
from rasa_sdk import Action, Tracker,FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
#
# class ValidateNameForm(FormValidationAction):
class Actionsubmit(Action):
    def name(self) -> Text:

      return "action_submit"
    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
      DataUpdate(tracker.get_slot("acedamicyear"),    
      tracker.get_slot("address"),tracker.get_slot("child_grade"),
      tracker.get_slot("child_name"),tracker.get_slot("dob"),tracker.get_slot("email"),tracker.get_slot("first_name_last_name"),tracker.get_slot("gaurdian"),
      tracker.get_slot("phone"),tracker.get_slot("school"),tracker.get_slot( "schooldetails")) 
      dispatcher.utter_message("Thanks for the valuable feedback. ")
      return() 

class ValidateName(FormValidationAction):

    def name(self) -> Text:

        return "validate_school_form"


    def validate_first_name_last_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""
        print(f"First name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"first_name_last_name": None}
        else:
            return {"first_name_last_name": slot_value}
    def validate_acedamicyear(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
       if slot_value == "2021":
           
           return{"acedamicyear": slot_value}

       else:
           dispatcher.utter_message(text="Please select current year")
           return {"acedamicyear": None}    


   
 #class ActionHelloWorld(Action):
#
    # def name(self) -> Text:
        # return "action_hello_world"
#
    # def run(self, dispatcher: CollectingDispatcher,
             #tracker: Tracker,
             #domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
         #dispatcher.utter_message(text="Hello World!")
#
        # return []
