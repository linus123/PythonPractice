import unittest
from Interpreter import Interpreter


class InterpreterTests(unittest.TestCase):

    def test_create_should_init_all_registers_to_zero(self):
        interpreter = Interpreter([])

        for index in range(10) :
            self.assertEquals('000', interpreter.get_register_value(index))

    def test_create_should_init_all_ram_to_zero_give_empty_set(self):
        interpreter = Interpreter([])

        for index in range(1000) :
            self.assertEquals('000', interpreter.get_ram_value(index))

    def test_should_set_ram_given_value(self):
        interpreter = Interpreter(['100'])

        self.assertEquals('100', interpreter.get_ram_value(0))

        for index in range(1, 1000) :
            self.assertEquals('000', interpreter.get_ram_value(index))

    def test_should_ingnore_invalid_ram_value(self):
        interpreter = Interpreter(['', None, 'Some non Int', '1000'])

        self.assertEquals('000', interpreter.get_ram_value(0))
        self.assertEquals('000', interpreter.get_ram_value(1))
        self.assertEquals('000', interpreter.get_ram_value(2))
        self.assertEquals('000', interpreter.get_ram_value(3))
