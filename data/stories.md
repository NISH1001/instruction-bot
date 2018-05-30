## simple greeting
* greet
    - utter_greet

## simple good bye
* goodbye
    - utter_goodbye

## switch off device
* greet
    - utter_greet
* switch_off
    - utter_ask_device_off
* switch_off{"light" : "bulb"}
    - slot{"light": "bulb"}
    - action_switch_off

## switch off device
* greet
    - utter_greet
* switch_off{"light" : "bulb"}
    - slot{"light": "bulb"}
    - action_switch_off

## switch on device
* greet
    - utter_greet
* switch_on
    - utter_ask_device_on
* switch_on{"light" : "bulb"}
    - slot{"light": "bulb"}
    - action_switch_on

## switch on device
* greet
    - utter_greet
* switch_off{"light" : "bulb"}
    - slot{"light": "bulb"}
    - action_switch_on
