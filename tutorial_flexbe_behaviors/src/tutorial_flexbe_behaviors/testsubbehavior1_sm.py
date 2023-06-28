#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from tutorial_flexbe_states.sub_state import SubState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Jun 28 2023
@author: H. M
'''
class TestSubBehavior1SM(Behavior):
	'''
	test
	'''


	def __init__(self):
		super(TestSubBehavior1SM, self).__init__()
		self.name = 'TestSubBehavior1'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:424 y:358
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:215 y:70
			OperatableStateMachine.add('substateA',
										SubState(),
										transitions={'path1': 'substateB', 'path2': 'substateC'},
										autonomy={'path1': Autonomy.Off, 'path2': Autonomy.Off})

			# x:46 y:232
			OperatableStateMachine.add('substateB',
										SubState(),
										transitions={'path1': 'finished', 'path2': 'substateC'},
										autonomy={'path1': Autonomy.Off, 'path2': Autonomy.Off})

			# x:273 y:240
			OperatableStateMachine.add('substateC',
										SubState(),
										transitions={'path1': 'substateB', 'path2': 'failed'},
										autonomy={'path1': Autonomy.Off, 'path2': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
