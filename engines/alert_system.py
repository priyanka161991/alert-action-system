#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create alerts as per user's request and perform actions as instructed.

Created on Sun May 27 11:18:28 2018

@author: priyanka.v.bhalekar@gmail.com
"""
from itertools import count
import logging


class Alert():
    _instance_count = count(0)
    
    def __init__(self, alert):
        """ Initialize alert details.
        
        Arguements:
            alert (dict): Dictionary of alert details, example -
            {
             'type'    : 'login_failure',
             'sourceid': 'splunk',
             'host'    : 'ip-192-168-149-25',
             'rhost'   : '43.225.46.25',
             'id'      : '5654'
            }
            Each of the alert can have different number of keys.
            Each alert should have 'type' key.
        
        Raise:
            KeyError - if required key is missing.
            Re-raise any error that occurs
        """
        log = logging.getLogger(__name__)
        
        # Save alert details
        self.alert_info = alert
        
        # Re-raise KeyError if 'type' is missing
        try:
            self.alert_info['type']
        except KeyError:
            log.error('Missing Key - Type')
            raise
        except Exception:
            log.error('Error - Failed to read Type')
            raise
        else:
            self.type = self.alert_info['type']
            
        self.id = next(self._instance_count)

        self.actions = []

    def __str__(self):
        return 'Alert {} - {}'.format(self.id, self.type)
        
    def perform_action(self, action):
        """ Perform action.
        
        Arguments:
            action (Action Object): Action to performed
        """
        self.actions.append(action)
