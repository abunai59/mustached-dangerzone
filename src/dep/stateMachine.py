# State machine
# By: abunai59

#from enum import Enum

class StateMachine:
    def __init__(self, states):
        self.state = states.DEFAULT

    def current_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state
