# -*- coding: utf8 -*-

import time

class Machine(object):
    def __init__(self, input_data, states, input_alphabet, tape_alphabet,
                 transition_function, start_state, accept_state, reject_state,
                 movement):

        if not input_data:
            input_data = ' '

        self.input_data = list(' ' + input_data + ' ')

        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.transition_function = transition_function

        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state

        self.movement = movement

        # Checar entradas e lançar exceções (ver definição formal no livro).

    def run(self, step_delay=1):
        pass

class SimpleMachine(Machine):
    def __init__(self, input_data, states, input_alphabet, tape_alphabet,
                 transition_function, start_state, accept_state, reject_state,
                 movement):
        Machine.__init__(self, input_data, states, input_alphabet,
                         tape_alphabet, transition_function, start_state,
                         accept_state, reject_state, movement)

    def run(self, step_delay=1):
        step = 1
        io_head = 1
        running = True
        current_state = self.start_state

        while running:
            print 'Step: %d' % step
            print 'Tape: %s' % self.input_data

            value = self.input_data[io_head]
            if current_state == self.accept_state:
                return True
            elif current_state == self.reject_state:
                return False
            else:
                transition = self.transition_function[current_state][value]
                next_state = transition[0]
                new_value = transition[1]
                head_movement = transition[2]
                self.input_data[io_head] = new_value

                print 'Current state: %s' % current_state
                print 'Read \"%s\"' % value

                if current_state != next_state:
                    print 'Next state: %s' % next_state

                if value != new_value:
                    print 'Write \"%s\"' % new_value

                if head_movement == self.movement[0]:
                    print 'Moves left'
                    io_head -= 1
                    if io_head < 0:
                        self.input_data.insert(0, ' ')
                        io_head = 0

                elif head_movement == self.movement[1]:
                    print 'Moves right'
                    io_head += 1
                    if io_head >= len(self.input_data):
                        self.input_data.append(' ')
                        io_head = len(self.input_data) - 1

                current_state = next_state

            print 'New tape: %s\n' % self.input_data
            step += 1
            time.sleep(step_delay)


if __name__ == '__main__':
    input_data = '0' * 16
    states = ('q1', 'q2', 'q3', 'q4', 'q5', 'qa', 'qr')
    input_alphabet = tuple('0')
    tape_alphabet = tuple(' 0x')

    transition_function = {
        states[0]: {
            tape_alphabet[0]: [states[6], tape_alphabet[0], 'right'],
            tape_alphabet[1]: [states[1], tape_alphabet[0], 'right'],
            tape_alphabet[2]: [states[6], tape_alphabet[2], 'right']
        },
        states[1]: {
            tape_alphabet[0]: [states[5], tape_alphabet[0], 'right'],
            tape_alphabet[1]: [states[2], tape_alphabet[2], 'right'],
            tape_alphabet[2]: [states[1], tape_alphabet[2], 'right']
        },
        states[2]: {
            tape_alphabet[0]: [states[4], tape_alphabet[0], 'left'],
            tape_alphabet[1]: [states[3], tape_alphabet[1], 'right'],
            tape_alphabet[2]: [states[2], tape_alphabet[2], 'right']
        },
        states[3]: {
            tape_alphabet[0]: [states[6], tape_alphabet[0], 'right'],
            tape_alphabet[1]: [states[2], tape_alphabet[2], 'right'],
            tape_alphabet[2]: [states[3], tape_alphabet[2], 'right']
        },
        states[4]: {
            tape_alphabet[0]: [states[1], tape_alphabet[0], 'right'],
            tape_alphabet[1]: [states[4], tape_alphabet[1], 'left'],
            tape_alphabet[2]: [states[4], tape_alphabet[2], 'left']
        }
    }

    start_state = states[0]
    accept_state = states[5]
    reject_state = states[6]

    m = SimpleMachine(input_data, states, input_alphabet, tape_alphabet,
                      transition_function, start_state, accept_state,
                      reject_state, ('left', 'right'))

    if m.run(0.2):
        print 'Accepted!'
    else:
        print 'Rejected!'

