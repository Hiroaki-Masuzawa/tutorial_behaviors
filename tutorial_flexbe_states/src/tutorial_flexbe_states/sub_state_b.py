#!/usr/bin/env python
import rospy
import random
from flexbe_core import EventState, Logger

class SubState2(EventState):
    '''
    SubState State.

    <= path1    go to path1.
    <= path2    go to path2.
    <= path3    go to path3.

    '''

    def __init__(self):
        super(SubState2, self).__init__(outcomes = ['path1', 'path2', 'path3'])
    
    def execute(self, userdata):
        rospy.sleep(1.0)
        value = random.randint(1, 2)
        Logger.loginfo('execute SubState {}'.format(value))
        if value == 1:
            return 'path1'
        elif value == 2:
            return 'path2'

    def on_enter(self, userdata):
        pass

    def on_exit(self, userdata):
        pass

    def on_start(self):
        pass

    def on_stop(self):
        pass

