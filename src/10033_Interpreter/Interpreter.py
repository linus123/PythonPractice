import sys

class Interpreter:

    def __init__(self, init_ram):
        self.DEFAULT_VALUE = '000'
        self._registers = [0] * 10
        self._ram = [self.DEFAULT_VALUE] * 1000

        counter = 0

        for init_ram_value in init_ram :
            self._ram[counter] = self._convert_to_valid_value_or_default(init_ram_value)
            counter += 1

    def get_register_value(self, index):
        return self._convert_to_printable_string(self._registers[index])

    def get_ram_value(self, index):
        return self._ram[index]

    def execute(self):
        program_counter = 0
        instruction_count = 1

        current_command = self._ram[program_counter]

        while current_command != '100':

            value1 = int(current_command[1])
            value2 = int(current_command[2])

            program_counter += 1

            # self._print_state()

            if current_command[0] == '2':
                self._set_register_to_value(value1, value2)
            elif current_command[0] == '3':
                self._add_value_to_register(value1, value2)
            elif current_command[0] == '4':
                self._multiply_value_by_register(value1, value2)
            elif current_command[0] == '5':
                self._copy_register_value(value1, value2)
            elif current_command[0] == '6':
                self._add_register_value(value1, value2)
            elif current_command[0] == '7':
                self._multiply_register_value(value1, value2)
            elif current_command[0] == '8':
                self._copy_value_from_ram(value1, value2)
            elif current_command[0] == '9':
                self._copy_value_to_ram(value1, value2)
            elif current_command[0] == '0':
                program_counter = self._get_new_program_counter(value1, value2, program_counter)

            instruction_count += 1
            current_command = self._ram[program_counter]

        return instruction_count

    def _set_register_to_value(self, register_index, value):
        self._registers[register_index] = value

    def _add_value_to_register(self, register_index, value):
        raw_value = self._registers[register_index] + value
        self._registers[register_index] = self._get_modulated_value(raw_value)

    def _multiply_value_by_register(self, register_index, value):
        raw_value = self._registers[register_index] * value
        self._registers[register_index] = self._get_modulated_value(raw_value)

    def _copy_register_value(self, destination, source):
        self._registers[destination] = self._registers[source]

    def _add_register_value(self, destination, source):
        raw_value = self._registers[destination] + self._registers[source]

        self._registers[destination] = self._get_modulated_value(raw_value)

    def _multiply_register_value(self, destination, source):
        raw_value = self._registers[destination] * self._registers[source]
        self._registers[destination] = self._get_modulated_value(raw_value)

    def _copy_value_from_ram(self, destination, source):
        ram_index = self._registers[source]
        self._registers[destination] = int(self._ram[ram_index])

    def _copy_value_to_ram(self, source_register_index, destination_ram):
        ram_index = self._registers[destination_ram]
        self._ram[ram_index] = self._convert_to_printable_string(self._registers[source_register_index])

    def _get_new_program_counter(self, destination_loc_reg_index, eval_reg_index, current_program_counter):

        if self._registers[eval_reg_index] == 0:
            return current_program_counter

        return self._registers[destination_loc_reg_index]

    def _get_modulated_value(self, value):
        return value % 1000

    def _convert_to_valid_value_or_default(self, val):
        if val is None:
            return self.DEFAULT_VALUE

        try:
            val_as_int = int(val)

        except ValueError:

            return self.DEFAULT_VALUE

        if (val_as_int < 1000):
            return self._convert_to_printable_string(val_as_int)

        return self.DEFAULT_VALUE

    def _convert_to_printable_string(self, val):
        return '{0:03d}'.format(val)

    def _print_state(self):
        print(self._registers)
        print(self._ram)
        print()

#####################################

def read_case_from_standard_in():
    current_line = sys.stdin.readline().rstrip()

    case = []

    while current_line != "":
        case.append(current_line)
        current_line = sys.stdin.readline().rstrip()

    return case


def read_from_standard_in():
    case_count_line = sys.stdin.readline().rstrip()

    case_count = int(case_count_line)

    #read blank line
    sys.stdin.readline()

    for count in range(case_count):
        case = read_case_from_standard_in()
        interp = Interpreter(case)
        command_count = interp.execute()
        print(command_count)

        if (count < case_count - 1):
            print()

def main():
    read_from_standard_in()


if __name__ == '__main__':
    main()