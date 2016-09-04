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

    def test_should_ignore_invalid_ram_value(self):
        interpreter = Interpreter(['', None, 'Some non Int', '1000'])

        self.assertEquals('000', interpreter.get_ram_value(0))
        self.assertEquals('000', interpreter.get_ram_value(1))
        self.assertEquals('000', interpreter.get_ram_value(2))
        self.assertEquals('000', interpreter.get_ram_value(3))

    def test_should_do_nothing_given_single_halt_value(self):
        interpreter = Interpreter(['100'])
        interpreter.execute()

        for index in range(10) :
            self.assertEquals('000', interpreter.get_register_value(index))

    def test_2dn_should_set_register_d_to_n(self):
        interpreter = Interpreter(['201', '100'])
        interpreter.execute()
        self.assertEquals('001', interpreter.get_register_value(0))

        interpreter = Interpreter(['299', '100'])
        interpreter.execute()
        self.assertEquals('009', interpreter.get_register_value(9))

    def test_3dn_should_add_n_to_register_d(self):
        interpreter = Interpreter(['308', '100'])
        interpreter.execute()
        self.assertEquals('008', interpreter.get_register_value(0))

        interpreter = Interpreter(['308', '302', '100'])
        interpreter.execute()
        self.assertEquals('010', interpreter.get_register_value(0))

    def test_4dn_should_multiply_d_by_n(self):
        interpreter = Interpreter(['408', '100'])
        interpreter.execute()
        self.assertEquals('000', interpreter.get_register_value(0))

        interpreter = Interpreter(['302', '407', '100'])
        interpreter.execute()
        self.assertEquals('014', interpreter.get_register_value(0))

    def test_5ds_should_set_register_d_to_the_value_of_register_s(self):
        interpreter = Interpreter(['209', '510', '100'])
        interpreter.execute()
        self.assertEquals('009', interpreter.get_register_value(0))
        self.assertEquals('009', interpreter.get_register_value(1))
