# Game state machine
# By: abunai59

from dep.stateMachine import StateMachine
from dep.enum import Enum

class GameStateMachine(StateMachine):
    States = Enum(DEFAULT=0, NORMAL=1, MENU=2, PAUSE=3)
    state = States.DEFAULT

    # Extended methods
    def __init__(self):
        StateMachine(self.States)

    def current_state(self):
        return StateMachine.current_state(self)

    def set_state(self, new_state):
        StateMachine.set_state(self, new_state)
