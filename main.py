#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Alert-Action System. Let user create alerts and then perform
series of actions on any alert. Using past behaviour of user,
suggest actions he/she can perform on given alert.

Created on Sun May 27 10:39:42 2018

@author: priyanka.v.bhalekar@gmail.com

Usage:
  main.py
  main.py -h | --help
  main.py --version

 Options:
   -h, --help       Show this message.
   --version        Print the version.
"""

from docopt import docopt
import json

from engines.action_system import Action
from engines.alert_system import Alert
from engines.recommend import (
   enhance_recommend_system,
   recommend_actions,
)


def main(args):
    # Save all alerts with their type as key
    alerts = {}
    
    # Ask user for input
    while(True):
        print('----------------------------------------')
        print('0. Exit')
        print('1. Create an alert')
        print('2. Perform actions')
        print('----------------------------------------')
        try:
            choice = int(input('Please enter your choice :'))
        except Exception:
            print('Please enter only interger values.')
            continue
        
        if choice == 0:
            print('Exit')
            return
        elif choice == 1:
            print('Please enter Alert details in JSON format.')
            alert_details = input()
            
            # Parse JSON
            try:
                alert_details = json.loads(alert_details)
            except Exception:
                print('Not a valid JSON')
                continue
            
            # Create Alert
            try:
                alert = Alert(alert_details)
            except Exception:
                print('Error - Failed to create Alert')
                continue
            
            # Add to alerts dictionary
            alerts[alert.id] = alert
            print('Alert Created with id : ', alert.id)
        
            # Recommend action sequence to perform
            recommend_actions(alert.type)
        elif choice == 2:
            print('Please enter Action to be performed in JSON format.')
            action_details = input()
            
            # Parse JSON
            try:
                action_details = json.loads(action_details)
            except Exception:
                print('Not a valid JSON')
                continue
            
            # Create Action
            try:
                action = Action(action_details)
            except Exception:
                print('Failed to create Action')
                continue
            
            # Look for alert using alert id
            try:
                alert = alerts[action.action_info['alert_id']]
            except KeyError:
                print('Alert does not exist.')
            else:
                alert.perform_action(action)
                enhance_recommend_system(
                    alert.type,
                    action.action_info['action_name']
                )
        else:
            print('Wrong Choice.')
     
 
if __name__ == '__main__':
    ARGS = docopt(__doc__, version='0.0.1')
    try:
        main(ARGS)
    except Exception:
        print('Uncaught Exception Occured.')
        raise
