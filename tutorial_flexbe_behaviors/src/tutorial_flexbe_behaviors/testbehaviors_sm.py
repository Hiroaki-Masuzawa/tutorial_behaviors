#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from tutorial_flexbe_states.detect import DetectState
from tutorial_flexbe_states.move_forward import MoveForwardState
from tutorial_flexbe_states.stop import StopState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Jun 28 2023
@author: H. M
'''
class TestBehaviorsSM(Behavior):
	'''
	Test
	'''


	def __init__(self):
		super(TestBehaviorsSM, self).__init__()
		self.name = 'TestBehaviors'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:767 y:90, x:326 y:240
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:73 y:69
			OperatableStateMachine.add('moveForward',
										MoveForwardState(),
										transitions={'done': 'detect'},
										autonomy={'done': Autonomy.Off})

			# x:532 y:76
			OperatableStateMachine.add('stop',
										StopState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:270 y:61
			OperatableStateMachine.add('detect',
										DetectState(),
										transitions={'yes': 'stop', 'no': 'moveForward', 'timeout': 'failed'},
										autonomy={'yes': Autonomy.Off, 'no': Autonomy.Off, 'timeout': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
