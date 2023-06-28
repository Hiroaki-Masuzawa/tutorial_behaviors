#!/usr/bin/env python
import rospy

from flexbe_core import EventState, Logger

class MoveForwardState(EventState):
    '''
    MoveForward State.

    <= done                         Send command to move forward.

    '''

    def __init__(self):
        super(MoveForwardState, self).__init__(outcomes = ['done'])
    
    def execute(self, userdata):
        start_time = rospy.Time.now()

        while (rospy.Time.now() - start_time).to_sec() < 1.0:
            pass

        Logger.loginfo('execute MoveForwardState')
        return 'done'

    def on_enter(self, userdata):
        Logger.loginfo('MoveForwardState on_enter')
        pass

    def on_exit(self, userdata):
        pass

    def on_start(self):
        pass

    def on_stop(self):
        pass

