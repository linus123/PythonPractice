class Interpreter :

    def __init__(self, init_ram):
        self.DEFAULT_VALUE = '000'
        self._registers = [self.DEFAULT_VALUE] * 10
        self._ram = [self.DEFAULT_VALUE] * 1000

        counter = 0

        for init_ram_value in init_ram :
            self._ram[counter] = self._convert_to_valid_value_or_default(init_ram_value)
            counter += 1

    def get_register_value(self, index):
        return self._registers[index]

    def get_ram_value(self, index):
        return self._ram[index]

    def _convert_to_valid_value_or_default(self, val):

        if val is None:
            return self.DEFAULT_VALUE

        try:
            val_as_int = int(val)

        except ValueError:

            return self.DEFAULT_VALUE

        if (val_as_int < 1000):
            return '{0:03d}'.format(val_as_int)

        return self.DEFAULT_VALUE
