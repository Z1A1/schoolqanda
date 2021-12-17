from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker,FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
#
# class ValidateNameForm(FormValidationAction):
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
