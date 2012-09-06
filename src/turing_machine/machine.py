class Machine(object):
    def __init__(self, states, input_alphabet, tape_alphabet,
                 transition_function, start_state, accept_state, reject_state):

        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state

        self.tape = []
        self.tape_head = 0

    def run(self):
        pass
