import unittest
from Interpreter import Interpreter


class InterpreterTests(unittest.TestCase):

    def test_create_should_init_all_registers_to_zero(self):
        interpreter = Interpreter([])

        for index in range(10) :
            self.assertEqual('000', interpreter.get_register_value(index))

    def test_create_should_init_all_ram_to_zero_give_empty_set(self):
        interpreter = Interpreter([])

        for index in range(1000) :
            self.assertEqual('000', interpreter.get_ram_value(index))

    def test_should_set_ram_given_value(self):
        interpreter = Interpreter(['100'])

        self.assertEqual('100', interpreter.get_ram_value(0))

        for index in range(1, 1000) :
            self.assertEqual('000', interpreter.get_ram_value(index))

    def test_should_ignore_invalid_ram_value(self):
        interpreter = Interpreter(['', None, 'Some non Int', '1000'])

        self.assertEqual('000', interpreter.get_ram_value(0))
        self.assertEqual('000', interpreter.get_ram_value(1))
        self.assertEqual('000', interpreter.get_ram_value(2))
        self.assertEqual('000', interpreter.get_ram_value(3))

    def test_should_do_nothing_given_single_halt_value(self):
        interpreter = Interpreter(['100'])
        interpreter.execute()

        for index in range(10) :
            self.assertEqual('000', interpreter.get_register_value(index))

    def test_2dn_should_set_register_d_to_n(self):
        interpreter = Interpreter(['201', '100'])

        instruction_count = interpreter.execute()

        self.assertEqual('001', interpreter.get_register_value(0))
        self.assertEqual(2, instruction_count)

        ##

        interpreter = Interpreter(['299', '100'])

        instruction_count = interpreter.execute()

        self.assertEqual('009', interpreter.get_register_value(9))
        self.assertEqual(2, instruction_count)

    def test_3dn_should_add_n_to_register_d(self):
        interpreter = Interpreter(['308', '100'])

        instruction_count = interpreter.execute()

        self.assertEqual('008', interpreter.get_register_value(0))
        self.assertEqual(2, instruction_count)

        ##

        interpreter = Interpreter(['308', '302', '100'])

        instruction_count = interpreter.execute()

        self.assertEqual('010', interpreter.get_register_value(0))
        self.assertEqual(3, instruction_count)

    def test_4dn_should_multiply_d_by_n(self):
        interpreter = Interpreter(['408', '100'])

        instruction_count = interpreter.execute()

        self.assertEqual('000', interpreter.get_register_value(0))
        self.assertEqual(2, instruction_count)

        ##

        interpreter = Interpreter(['302', '407', '100'])

        instruction_count = interpreter.execute()

        self.assertEqual('014', interpreter.get_register_value(0))
        self.assertEqual(3, instruction_count)

    def test_5ds_should_set_register_d_to_the_value_of_register_s(self):
        interpreter = Interpreter(['209', '510', '100'])

        instruction_count = interpreter.execute()

        self.assertEqual('009', interpreter.get_register_value(0))
        self.assertEqual('009', interpreter.get_register_value(1))
        self.assertEqual(3, instruction_count)

    def test_6ds_should_add_register_d_to_the_value_of_register_s(self):
        interpreter = Interpreter(['209', '211', '610', '100'])

        instruction_count = interpreter.execute()

        self.assertEqual('009', interpreter.get_register_value(0))
        self.assertEqual('010', interpreter.get_register_value(1))
        self.assertEqual(4, instruction_count)

    def test_7ds_should_multiply_register_d_to_the_value_of_register_s(self):
        interpreter = Interpreter(['209', '212', '710', '100'])

        instruction_count = interpreter.execute()

        self.assertEqual('009', interpreter.get_register_value(0))
        self.assertEqual('018', interpreter.get_register_value(1))
        self.assertEqual(4, instruction_count)

    def test_8da_should_set_register_d_to_the_value_in_ram_whose_address_is_in_register_a(self):
        interpreter = Interpreter(['203', '810', '100', '999'])

        instruction_count = interpreter.execute()

        self.assertEqual('003', interpreter.get_register_value(0))
        self.assertEqual('999', interpreter.get_register_value(1))
        self.assertEqual(3, instruction_count)

    def test_9sa_set_the_value_in_ram(self):
        interpreter = Interpreter(['209', '215', '901', '100'])

        instruction_count = interpreter.execute()

        self.assertEqual('009', interpreter.get_ram_value(5))
        self.assertEqual(4, instruction_count)

    def test_0ds_should_go_to_location_d(self):
        interpreter = Interpreter(['201', '214', '010', '201', '100'])

        instruction_count = interpreter.execute()

        self.assertEqual('001', interpreter.get_register_value(0))
        self.assertEqual(4, instruction_count)

    def test_0ds_should_not_go_to_location_d_when_s_is_zero(self):
        interpreter = Interpreter(['200', '214', '010', '201', '100'])

        instruction_count = interpreter.execute()

        self.assertEqual('001', interpreter.get_register_value(0))
        self.assertEqual(5, instruction_count)

    def test_sample_test_case(self):
        interpreter = Interpreter(['299','492','495','399','492','495','399','283','279','689','078','100','000','000','000'])

        instruction_count = interpreter.execute()

        self.assertEqual(16, instruction_count)

    def test_sample_test_case2(self):
        interpreter = Interpreter(['299','233','255','990','803','301','050','100'])

        instruction_count = interpreter.execute()

        self.assertEqual(26, instruction_count)

