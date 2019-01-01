import unittest

from crypt_kicker2 import decrypt_lines, get_letter_map_from_encrypted_main_line


class CryptKicker2Tests(unittest.TestCase):
    def test_001(self):
        """get_letter_map_from_encrypted_main_line should return none of line not found"""
        lines = [
            "a",
            "c"
        ]

        result = get_letter_map_from_encrypted_main_line(lines)

        self.assertIsNone(result)

    def test_002(self):
        """get_letter_map_from_encrypted_main_line should return none when line does not match is not word possible"""
        lines = [
            "xnm ceuob lrtzv itah egfd tsmrx nm ypwq ktj",
        ]

        result = get_letter_map_from_encrypted_main_line(lines)

        self.assertIsNone(result)

    def test_003(self):
        """get_letter_map_from_encrypted_main_line should return none when line is not letter possible"""
        lines = [
            "xoo ceuob lrtzv ita hegfd tsmr xnm ypwq ktj",
        ]

        result = get_letter_map_from_encrypted_main_line(lines)

        self.assertIsNone(result)

    def test_004(self):
        """get_letter_map_from_encrypted_main_line should letter map when encrypted main line found"""
        lines = [
            "xnm ceuob lrtzv ita hegfd tsmr xnm ypwq ktj",
        ]

        result = get_letter_map_from_encrypted_main_line(lines)

        self.assertIsNotNone(result)

        self.assertEqual("t", result["x"])
        self.assertEqual("h", result["n"])
        self.assertEqual("e", result["m"])

    def test_201(self):
        """Should return no solution given no strings to master line length"""
        lines = [
            "a",
            "c"
        ]

        result = decrypt_lines(lines)

        self.assertEqual(1, len(result))
        self.assertEqual(result[0], "No solution.")

    def test_202(self):
        """Should return no solution given a string that does NOT match the main line"""
        lines = [
            "xnm ceuob lrtzv ita hegfd tsmr xnm ypwq www"
        ]

        result = decrypt_lines(lines)

        self.assertEqual(1, len(result))
        self.assertEqual(result[0], "No solution.")

    def test_203(self):
        """Should return the main line when given JUST the main line"""
        lines = [
            "xnm ceuob lrtzv ita hegfd tsmr xnm ypwq ktj"
        ]

        result = decrypt_lines(lines)

        self.assertEqual(1, len(result))
        self.assertEqual(result[0], "the quick brown fox jumps over the lazy dog")

    def test_500(self):
        """Should solve the problem given the in the problem write up"""
        lines = [
            "vtz ud xnm xugm itr pyy jttk gmv xt otgm xt xnm puk ti xnm fprxq",
            "xnm ceuob lrtzv ita hegfd tsmr xnm ypwq ktj",
            "frtjrpgguvj otvxmdxd prm iev prmvx xnmq"
        ]

        result = decrypt_lines(lines)

        self.assertEqual(3, len(result))

        self.assertEqual(result[0], "now is the time for all good men to come to the aid of the party")
        self.assertEqual(result[1], "the quick brown fox jumps over the lazy dog")
        self.assertEqual(result[2], "programming contests are fun arent they")

    def test_501(self):
        """Should solve the problem given in udebug"""
        lines = [
            "vtz ud xnm xugm itr pyy jttk gmv xt otgm xt xnm puk ti xnm fprxq",
            "xnm ceuob lrtzv ita hegfd tsmr znm ypwq ktj",
            "frtjrpgguvj otvxmdxd prm iev prmvx xnmq",
            "xnm ceuob lrtzv ita hegfd tsmr xnm ypwq ktj",
            "vtz ud xnm xugm itr pyy jttk gmv xt otgm xt xnm puk ti xnm fprxq",
            "frtjrpgguvj otvxmdxd prm iev prmvx xnmq"
        ]

        result = decrypt_lines(lines)

        self.assertEqual(6, len(result))

        self.assertEqual(result[0], "now is the time for all good men to come to the aid of the party")
        self.assertEqual(result[1], "the quick brown fox jumps over whe lazy dog")
        self.assertEqual(result[2], "programming contests are fun arent they")
        self.assertEqual(result[3], "the quick brown fox jumps over the lazy dog")
        self.assertEqual(result[4], "now is the time for all good men to come to the aid of the party")
        self.assertEqual(result[5], "programming contests are fun arent they")
