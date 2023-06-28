#!/usr/bin/env python
import rospy

from flexbe_core import EventState, Logger

class StopState(EventState):
    '''
    Stop State.

    <= done                      done.

    '''
    
    def __init__(self):
        super(StopState, self).__init__(outcomes = ['done'])
    
    def execute(self, userdata):
        
        Logger.loginfo('execute StopState')
        return 'done'

    def on_enter(self, userdata):
        pass

    def on_exit(self, userdata):
        pass

    def on_start(self):
        pass

    def on_stop(self):
        pass