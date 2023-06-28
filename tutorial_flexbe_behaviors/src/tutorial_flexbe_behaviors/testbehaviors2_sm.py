#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from tutorial_flexbe_states.multi_divided import MultiDividedState
from tutorial_flexbe_states.sub_state import SubState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Jun 28 2023
@author: H. M
'''
class TestBehaviors2SM(Behavior):
	'''
	test
	'''


	def __init__(self):
		super(TestBehaviors2SM, self).__init__()
		self.name = 'TestBehaviors2'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:397 y:289, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:386 y:361, x:130 y:365
		_sm_container_0 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_container_0:
			# x:149 y:115
			OperatableStateMachine.add('substateA',
										SubState(),
										transitions={'path1': 'substateB', 'path2': 'substateC'},
										autonomy={'path1': Autonomy.Off, 'path2': Autonomy.Off})

			# x:51 y:245
			OperatableStateMachine.add('substateB',
										SubState(),
										transitions={'path1': 'failed', 'path2': 'substateC'},
										autonomy={'path1': Autonomy.Off, 'path2': Autonomy.Off})

			# x:325 y:241
			OperatableStateMachine.add('substateC',
										SubState(),
										transitions={'path1': 'substateB', 'path2': 'finished'},
										autonomy={'path1': Autonomy.Off, 'path2': Autonomy.Off})



		with _state_machine:
			# x:155 y:110
			OperatableStateMachine.add('divide',
										MultiDividedState(),
										transitions={'path1': 'Container', 'path2': 'Container', 'path3': 'finished', 'path4': 'failed'},
										autonomy={'path1': Autonomy.Off, 'path2': Autonomy.Off, 'path3': Autonomy.Off, 'path4': Autonomy.Off})

			# x:408 y:110
			OperatableStateMachine.add('Container',
										_sm_container_0,
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
