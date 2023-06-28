#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_states.log_state import LogState
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Jun 28 2023
@author: H. M
'''
class HelloWorldDemoSM(Behavior):
	'''
	Behavior created during in the FlexBe tutorial
	'''


	def __init__(self):
		super(HelloWorldDemoSM, self).__init__()
		self.name = 'Hello World Demo'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		hello = "Hello World!"
		# x:71 y:424, x:252 y:373
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:111 y:92
			OperatableStateMachine.add('move_forward',
										WaitState(wait_time=5.0),
										transitions={'done': 'print_greeting'},
										autonomy={'done': Autonomy.Off})

			# x:90 y:192
			OperatableStateMachine.add('print_greeting',
										LogState(text=hello, severity=Logger.REPORT_HINT),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
