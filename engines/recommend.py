#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Recommend what actions to perform when User create
an alert based on his past behaviour.

Created on Sun May 27 16:45:25 2018

@author: priyanka.v.bhalekar@gmail.com
"""
from collections import defaultdict


# Save actions performed on a particular alert.
suggestions = defaultdict(set)


def recommend_actions(alert_type):
    """Look for actions performed in the past for similar
    alerts.
    
    Arguments:
        alert_type (str): Type alert. Example - 'Login Failure'
    """
    suggest_actions = suggestions.get(alert_type)
    if suggest_actions:
        print('Perform following sequence of actions - ')
        print('----------------------------------------')
        for num, suggestion in enumerate(suggest_actions):
            print('%d %s' % (num, suggestion.upper()))
        print('----------------------------------------')


def enhance_recommend_system(alert_type, action_name):
    """Enhance recommandation system by keeping track of
    alerts and actions performed by user.
    
    Arguments:
        alert_type (str): Type alert. Example - 'Login Failure'
        action_name (str): Name of the action performed. Example -
            'Get IP Reputation'
    """
    suggestions[alert_type].add(action_name)
