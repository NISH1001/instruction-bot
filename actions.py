#!/usr/bin/env python3


from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionSwitchOff(Action):
    def name(self):
        return 'action_switch_off'

    def run(self, dispatcher, tracker, domain):
        light = tracker.get_slot('light')
        dispatcher.utter_message("Switching off {}".format(light))
        return []

class ActionSwitchOn(Action):
    def name(self):
        return 'action_switch_on'

    def run(self, dispatcher, tracker, domain):
        light = tracker.get_slot('light')
        dispatcher.utter_message("Switching on {}".format(light))
        print(light)
        return []


def main():
    pass

if __name__ == "__main__":
    main()

