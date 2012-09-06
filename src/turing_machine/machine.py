# -*- coding: utf8 -*-

class Machine(object):
    LEFT = 1
    STOP = 0
    RIGHT = -1

    def __init__(self, input_data, states, input_alphabet, tape_alphabet,
                 transition_function, start_state, accept_state, reject_state):

        if not input_data:
            input_data = ' '

        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.transition_function = transition_function
        self.current_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state

        self.tape = list(' ' + input_data + ' ')
        self.tape_head = 1

        # Checar entradas e lançar exceções (ver definição formal no livro).

    def run(self):
        pass

