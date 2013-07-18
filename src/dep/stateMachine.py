# State machine
# By: abunai59

from enum import Enum

States = Enum(DEFAULT=0, NORMAL=1, MENU=2, PAUSE=3)

class StateMachine:
    def __init__(self):
        self.state = States.DEFAULT

    def current_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state
