#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Allow user to specify action to be performed on alert.

Created on Sun May 27 13:00:06 2018

@author: priyanka.v.bhalekar@gmail.com
"""
from itertools import count
import logging


class Action():
    _instance_count = count(0)
    
    def __init__(self, action):
        """Initialize action.
        
        Arguments:
            action (dict): Action information
            
        Raise:
            KeyError - if any of the required key missing.
            Re-raise any error that occurs
        """
        log = logging.getLogger(__name__)
        
        self.action_info = action
        
        try:
            self.action_info['action_name']
        except KeyError:
            log.error('Missing Key - action_name')
            raise
        
        try:
            self.action_info['alert_id']
        except KeyError:
            log.error('Missing Key - alert_id')
            raise

        self.id = next(self._instance_count)
        
    def __str__(self):
        return 'Action {} - {}'.format(
            self.id, 
            self.action_info['action_name']
        )
