#!/usr/bin/env python
import rospy
import random

from flexbe_core import EventState, Logger

class DetectState(EventState):

    '''
    Detect State.

    <= yes                      Detect to something.
    <= no                       Not detect to something.
    <= timeout                  time out occurs.

    '''

    def __init__(self):
        super(DetectState, self).__init__(outcomes = ['yes', 'no', 'timeout'])
    
    def execute(self, userdata):

        value = random.randint(0,5)
        Logger.loginfo('execute DetectState {}'.format(value))
        if value == 0:
            return 'timeout'
        elif value < 5:
            return 'no'
        return 'yes'

    def on_enter(self, userdata):
        start_time = rospy.Time.now()
        time_to_wait =(rospy.Time.now() - start_time).to_sec()
        Logger.loginfo('DetectState on_enter')

        while (rospy.Time.now() - start_time).to_sec() < 1.0:
            pass

    def on_exit(self, userdata):
        pass

    def on_start(self):
        pass

    def on_stop(self):
        pass