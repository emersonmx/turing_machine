# -*- coding: utf8 -*-

import time

class Machine(object):
    """Classe abstrata para uma Máquina de Turing.

    Attributos:
        input_data: é o dado de entrada para a máquina.
        states: é o conjunto de estados da máquina.
        input_alphabet: é o alfabeto de entrada da máquina.
        tape_alphabet: é o alfabeto da fita.
        transition_function: é a função de transição.
        start_state: é o estado inicial.
        accept_state: é o estado de aceitação.
        reject_state: é o estado de rejeição.

        _step: contador de iteração.
        _io_head: cabeçote de leitura e escrita.
        _current_state: estado atual.
    """

    def __init__(self):
        """Inicia a classe com os tipos vazios."""
        object.__init__(self)

        self.input_data = list()

        self.states = tuple()
        self.input_alphabet = tuple()
        self.tape_alphabet = tuple()
        self.transition_function = dict()

        self.start_state = ''
        self.accept_state = ''
        self.reject_state = ''

        self.movement = tuple()

        self._step = 1
        self._io_head = 0
        self._current_state = self.start_state

    def _config_validator(self):
        """Checa a configuração da máquina (ver definição formal no livro)."""
        pass

    def _process(self, debug):
        """Realiza o processamento da máquina."""
        pass

    def run(self, step_delay=1, debug=False):
        """Inicia a execução da máquina.

        Args:
            step_delay: é o tempo de impressão das informações no modo debug.
            debug: ativa o modo de debug da máquina.

        Retorno:
            O valor boleano True, caso o a máquina aceitou a entrada ou False
            caso contrário.
        """

        self._config_validator()

        self._current_state = self.start_state

        return_value = False
        running = True

        while running:
            if self._current_state == self.accept_state:
                return_value = True
                running = False
            elif self._current_state == self.reject_state:
                return_value = False
                running = False
            else:
                self._process(debug)

            if debug:
                time.sleep(step_delay)

            self._step += 1

        return return_value

class SimpleMachine(Machine):
    """Implementação de uma Máquina de Turing simples.

    Essa implementação da Máquina de Turing, usa uma fita preenchida com
    espaços. A entrada é colocada na fita e o cabeçote é posicionado no símbolo
    da extrema esquerda. Só foi usado apenas dois tipos de movimento,
    esquerdo ('left') e direito ('right').
    """

    def __init__(self):
        """Chama o construtor da classe base para inicializar os atributos."""
        Machine.__init__(self)

    def _config_validator(self):
        """Veja Machine._config_validator"""
        pass

    def _process(self, debug):
        """Ver Machine._process"""
        if debug:
            print 'Step: %d' % self._step
            print 'Tape: %s' % self.input_data

        value = self.input_data[self._io_head]

        transition = self.transition_function[self._current_state][value]
        next_state = transition[0]
        new_value = transition[1]
        head_movement = transition[2]
        self.input_data[self._io_head] = new_value

        if debug:
            print 'Current state: %s' % self._current_state
            print 'Read \"%s\"' % value

            if self._current_state != next_state:
                print 'Next state: %s' % next_state

            if value != new_value:
                print 'Write \"%s\"' % new_value

            print 'Moves %s' % head_movement

        if head_movement == self.movement[0]:
            self._io_head -= 1
            if self._io_head < 0:
                self.input_data.insert(0, ' ')
                self._io_head = 0

        elif head_movement == self.movement[1]:
            self._io_head += 1
            if self._io_head >= len(self.input_data):
                self.input_data.append(' ')
                self._io_head = len(self.input_data) - 1

        self._current_state = next_state

        if debug:
            print 'New tape: %s\n' % self.input_data

if __name__ == '__main__':
    number = int(raw_input('Number: '))

    m = SimpleMachine()

    m.input_data = list('0' * number)
    m.states = ('q1', 'q2', 'q3', 'q4', 'q5', 'qa', 'qr')
    m.input_alphabet = tuple('0')
    m.tape_alphabet = tuple(' 0x')

    m.movement = ('left', 'right')

    m.transition_function = {
        m.states[0]: {
            m.tape_alphabet[0]:
                [m.states[6], m.tape_alphabet[0], m.movement[1]],
            m.tape_alphabet[1]:
                [m.states[1], m.tape_alphabet[0], m.movement[1]],
            m.tape_alphabet[2]: [m.states[6], m.tape_alphabet[2], m.movement[1]]
        },
        m.states[1]: {
            m.tape_alphabet[0]:
                [m.states[5], m.tape_alphabet[0], m.movement[1]],
            m.tape_alphabet[1]:
                [m.states[2], m.tape_alphabet[2], m.movement[1]],
            m.tape_alphabet[2]: [m.states[1], m.tape_alphabet[2], m.movement[1]]
        },
        m.states[2]: {
            m.tape_alphabet[0]:
                [m.states[4], m.tape_alphabet[0], m.movement[0]],
            m.tape_alphabet[1]:
                [m.states[3], m.tape_alphabet[1], m.movement[1]],
            m.tape_alphabet[2]: [m.states[2], m.tape_alphabet[2], m.movement[1]]
        },
        m.states[3]: {
            m.tape_alphabet[0]:
                [m.states[6], m.tape_alphabet[0], m.movement[1]],
            m.tape_alphabet[1]:
                [m.states[2], m.tape_alphabet[2], m.movement[1]],
            m.tape_alphabet[2]: [m.states[3], m.tape_alphabet[2], m.movement[1]]
        },
        m.states[4]: {
            m.tape_alphabet[0]:
                [m.states[1], m.tape_alphabet[0], m.movement[1]],
            m.tape_alphabet[1]:
                [m.states[4], m.tape_alphabet[1], m.movement[0]],
            m.tape_alphabet[2]: [m.states[4], m.tape_alphabet[2], m.movement[0]]
        }
    }

    m.start_state = m.states[0]
    m.accept_state = m.states[5]
    m.reject_state = m.states[6]

    if m.run(0, True):
        print '\nAccepted!'
    else:
        print '\nRejected!'

