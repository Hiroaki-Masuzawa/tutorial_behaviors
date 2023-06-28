#!/usr/bin/env python
import rospy
import random
from flexbe_core import EventState, Logger

class MultiDividedState(EventState):
    '''
    MultiDividedState State.

    <= path1    go to path1.
    <= path2    go to path2.
    <= path3    go to path3.
    <= path4    go to path4.

    '''

    def __init__(self):
        super(MultiDividedState, self).__init__(outcomes = ['path1', 'path2', 'path3', 'path4'])
    
    def execute(self, userdata):
        rospy.sleep(1.0)
        value = random.randint(1, 4)
        Logger.loginfo('execute MultiDividedState {}'.format(value))
        if value == 1:
            return 'path1'
        elif value == 2:
            return 'path2'
        elif value == 3:
            return 'path3'
        elif value == 4:
            return 'path4'

    def on_enter(self, userdata):
        pass

    def on_exit(self, userdata):
        pass

    def on_start(self):
        pass

    def on_stop(self):
        pass

