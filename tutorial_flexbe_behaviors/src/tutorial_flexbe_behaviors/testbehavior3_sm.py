#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from tutorial_flexbe_behaviors.testsubbehavior1_sm import TestSubBehavior1SM
from tutorial_flexbe_states.multi_divided import MultiDividedState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Jun 28 2023
@author: H. M
'''
class TestBehavior3SM(Behavior):
	'''
	test
	'''


	def __init__(self):
		super(TestBehavior3SM, self).__init__()
		self.name = 'TestBehavior3'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(TestSubBehavior1SM, 'TestSubBehavior1')
		self.add_behavior(TestSubBehavior1SM, 'TestSubBehavior1_2')
		self.add_behavior(TestSubBehavior1SM, 'TestSubBehavior1_3')
		self.add_behavior(TestSubBehavior1SM, 'TestSubBehavior1_4')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:109 y:513, x:640 y:503
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:196 y:49
			OperatableStateMachine.add('multiDivied',
										MultiDividedState(),
										transitions={'path1': 'TestSubBehavior1', 'path2': 'TestSubBehavior1_2', 'path3': 'TestSubBehavior1_3', 'path4': 'TestSubBehavior1_4'},
										autonomy={'path1': Autonomy.Off, 'path2': Autonomy.Off, 'path3': Autonomy.Off, 'path4': Autonomy.Off})

			# x:313 y:216
			OperatableStateMachine.add('TestSubBehavior1_2',
										self.use_behavior(TestSubBehavior1SM, 'TestSubBehavior1_2'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:548 y:215
			OperatableStateMachine.add('TestSubBehavior1_3',
										self.use_behavior(TestSubBehavior1SM, 'TestSubBehavior1_3'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:743 y:210
			OperatableStateMachine.add('TestSubBehavior1_4',
										self.use_behavior(TestSubBehavior1SM, 'TestSubBehavior1_4'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:96 y:212
			OperatableStateMachine.add('TestSubBehavior1',
										self.use_behavior(TestSubBehavior1SM, 'TestSubBehavior1'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
