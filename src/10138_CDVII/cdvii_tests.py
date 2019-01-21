import unittest

from cdvii import *


class CDVIITests(unittest.TestCase):
    def test_001(self):
        """HighwayRecord should parse line correctly for enter record"""
        hr = HighwayRecord("ABCD123 01:01:06:01 enter 17")

        self.assertEqual("ABCD123", hr.license_number)
        self.assertEqual(True, hr.is_enter)
        self.assertEqual(False, hr.is_exit)

        self.assertEqual(17, hr.ramp_number)

        self.assertEqual(1 + 60*6 + 60*60*1, hr.minute_count)

    def test_002(self):
        """HighwayRecord should parse line correctly for exit record"""
        hr = HighwayRecord("ABCD123 05:11:03:25 exit 200")

        self.assertEqual("ABCD123", hr.license_number)
        self.assertEqual(False, hr.is_enter)
        self.assertEqual(True, hr.is_exit)

        self.assertEqual(200, hr.ramp_number)

        self.assertEqual(25 + 60*3 + 60*60*11, hr.minute_count)

    def test_101(self):
        """Should ignore a beginning exit record"""

        tolls = [10, 10, 10, 10, 10, 10, 20, 20, 20, 15, 15, 15, 15, 15, 15, 15, 20, 30, 20, 15, 15, 10, 10, 10]

        highway_records = [
            HighwayRecord("765DEF 00:00:07:00 exit 95"),
            HighwayRecord("765DEF 01:01:05:59 enter 17"),
            HighwayRecord("765DEF 01:01:07:00 exit 95"),
        ]

        results = get_all_billing_records(
            tolls,
            highway_records
        )

        self.assertEqual(1, len(results))

        self.assertEqual("765DEF", results[0].license_number)
        self.assertEqual(1080, results[0].get_bill_amount())

    def test_102(self):
        """Should ignore a trailing enter record"""

        tolls = [10, 10, 10, 10, 10, 10, 20, 20, 20, 15, 15, 15, 15, 15, 15, 15, 20, 30, 20, 15, 15, 10, 10, 10]

        highway_records = [
            HighwayRecord("765DEF 01:01:05:59 enter 17"),
            HighwayRecord("765DEF 01:01:07:00 exit 95"),
            HighwayRecord("765DEF 01:02:05:59 enter 17"),
        ]

        results = get_all_billing_records(
            tolls,
            highway_records
        )

        self.assertEqual(1, len(results))

        self.assertEqual("765DEF", results[0].license_number)
        self.assertEqual(1080, results[0].get_bill_amount())

    def test_103(self):
        """Should ignore single enter record"""

        tolls = [10, 10, 10, 10, 10, 10, 20, 20, 20, 15, 15, 15, 15, 15, 15, 15, 20, 30, 20, 15, 15, 10, 10, 10]

        highway_records = [
            HighwayRecord("765DEF 01:01:05:59 enter 17"),
        ]

        results = get_all_billing_records(
            tolls,
            highway_records
        )

        self.assertEqual(0, len(results))

    def test_104(self):
        """Should ignore single exit record"""

        tolls = [10, 10, 10, 10, 10, 10, 20, 20, 20, 15, 15, 15, 15, 15, 15, 15, 20, 30, 20, 15, 15, 10, 10, 10]

        highway_records = [
            HighwayRecord("765DEF 01:01:05:59 exit 17"),
        ]

        results = get_all_billing_records(
            tolls,
            highway_records
        )

        self.assertEqual(0, len(results))

    def test_105(self):
        """Should return result for sample record"""

        tolls = [10, 10, 10, 10, 10, 10, 20, 20, 20, 15, 15, 15, 15, 15, 15, 15, 20, 30, 20, 15, 15, 10, 10, 10]

        highway_records = [
            HighwayRecord("ABCD123 01:01:06:01 enter 17"),
            HighwayRecord("765DEF 01:01:07:00 exit 95"),
            HighwayRecord("ABCD123 01:01:08:03 exit 95"),
        ]

        results = get_all_billing_records(
            tolls,
            highway_records
        )

        self.assertEqual(1, len(results))

        self.assertEqual("ABCD123", results[0].license_number)
        self.assertEqual(1860, results[0].get_bill_amount())

    def test_106(self):
        """Should return result for sample record"""

        tolls = [10, 10, 10, 10, 10, 10, 20, 20, 20, 15, 15, 15, 15, 15, 15, 15, 20, 30, 20, 15, 15, 10, 10, 10]

        highway_records = [
            HighwayRecord("765DEF 01:01:05:59 enter 17"),
            HighwayRecord("ABCD123 01:01:06:01 enter 17"),
            HighwayRecord("ABCD123 01:01:08:03 exit 95"),
        ]

        results = get_all_billing_records(
            tolls,
            highway_records
        )

        self.assertEqual(1, len(results))

        self.assertEqual("ABCD123", results[0].license_number)
        self.assertEqual(1860, results[0].get_bill_amount())


    def test_200(self):
        """Should return result for sample record"""

        tolls = [10, 10, 10, 10, 10, 10, 20, 20, 20, 15, 15, 15, 15, 15, 15, 15, 20, 30, 20, 15, 15, 10, 10, 10]

        highway_records = [
            HighwayRecord("ABCD123 01:01:06:01 enter 17"),
            HighwayRecord("765DEF 01:01:07:00 exit 95"),
            HighwayRecord("ABCD123 01:01:08:03 exit 95"),
            HighwayRecord("765DEF 01:01:05:59 enter 17")
        ]

        results = get_all_billing_records(
            tolls,
            highway_records
        )

        self.assertEqual(2, len(results))

        self.assertEqual("765DEF", results[0].license_number)
        self.assertEqual(1080, results[0].get_bill_amount())

        self.assertEqual("ABCD123", results[1].license_number)
        self.assertEqual(1860, results[1].get_bill_amount())

    def test_201(self):
        """Should work for first debug example"""
        tolls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

        highway_records = [
            HighwayRecord("GLBUVL2TPTUCVR8MKMC 05:11:03:25 exit 90"),
            HighwayRecord("YN0NO2YHIAA 05:23:02:52 enter 61"),
            HighwayRecord("YLEO3KAE3W841XAIO 05:30:19:29 enter 78"),
            HighwayRecord("B1CUWJZI0083XOG 05:15:10:27 exit 35"),
            HighwayRecord("TDRD4FM 05:19:17:50 enter 9"),
            HighwayRecord("VB5NA 05:18:14:57 exit 87"),
            HighwayRecord("AY 05:08:23:15 enter 59"),
            HighwayRecord("T5A2OHJC53WR 05:26:22:06 enter 9"),
            HighwayRecord("CM0U9YUA12Y 05:30:03:07 enter 76"),
            HighwayRecord("BKQTNZ9OT61BQ 05:24:03:51 enter 3"),
            HighwayRecord("1 05:16:22:15 enter 58"),
            HighwayRecord("1DSRVW3VVCB8SIY 05:23:01:54 enter 51"),
            HighwayRecord("ZZT 05:25:17:40 exit 13"),
            HighwayRecord("GOXOTET4P3JPR9KSQ5 05:06:11:51 enter 66"),
            HighwayRecord("CM0U9YUA12Y 05:03:20:04 exit 79"),
            HighwayRecord("UBB4LYEWM5 05:29:20:07 exit 23"),
            HighwayRecord("2R27ZSDDLG77OVIT9RJ 05:26:17:07 enter 72"),
            HighwayRecord("IRN1VCFX8KH 05:10:11:41 enter 7"),
            HighwayRecord("NVG9YKZPLPLPJ1S2LN1N 05:16:14:55 enter 99"),
            HighwayRecord("DBUA8 05:29:04:34 enter 69"),
            HighwayRecord("KHTKQO7F6 05:19:20:25 enter 66"),
            HighwayRecord("T5A2OHJC53WR 05:16:02:05 enter 62"),
            HighwayRecord("WA7MZ2EUDTJKCB 05:11:22:20 exit 79"),
            HighwayRecord("I7LP 05:04:05:35 exit 14"),
            HighwayRecord("VRQ2ECL 05:14:06:00 exit 31"),
            HighwayRecord("GV5QEE 05:28:14:00 exit 74"),
            HighwayRecord("GLBUVL2TPTUCVR8MKMC 05:03:07:47 enter 74"),
            HighwayRecord("FCP6QN207YMN 05:24:04:40 enter 96"),
            HighwayRecord("QPM870QV4D1CLWI1 05:26:23:55 enter 48"),
            HighwayRecord("D 05:05:09:54 exit 31"),
            HighwayRecord("1 05:28:13:47 enter 32"),
            HighwayRecord("1DSRVW3VVCB8SIY 05:29:04:59 exit 91"),
            HighwayRecord("QPM870QV4D1CLWI1 05:22:19:53 exit 61"),
            HighwayRecord("WL 05:17:08:04 exit 78"),
            HighwayRecord("6D51YFQB 05:10:04:03 enter 44"),
            HighwayRecord("3H4LI1KVBCX4GM 05:07:23:52 exit 1"),
            HighwayRecord("5U3BEI 05:04:03:48 exit 27"),
            HighwayRecord("NVG9YKZPLPLPJ1S2LN1N 05:15:00:22 exit 50"),
            HighwayRecord("6D51YFQB 05:28:21:22 enter 36"),
            HighwayRecord("K42FAELL48AHKPVRFY 05:23:01:50 exit 16"),
            HighwayRecord("MM09ENQ 05:13:22:09 exit 24"),
            HighwayRecord("Y30EGA6IKO3NGRFZL3IY 05:27:04:47 exit 80"),
            HighwayRecord("BGEO6D8ZUOG86 05:27:04:27 exit 41"),
            HighwayRecord("WL 05:24:09:06 enter 12"),
            HighwayRecord("22WHS9NTB3Y0TUKY 05:03:19:46 exit 89"),
            HighwayRecord("5U3BEI 05:15:11:29 exit 52"),
            HighwayRecord("KHTKQO7F6 05:13:16:17 enter 84"),
            HighwayRecord("93KWIKL 05:01:23:04 enter 77"),
            HighwayRecord("FCP6QN207YMN 05:16:06:28 enter 4"),
            HighwayRecord("YJLWF1DYJN 05:23:22:48 exit 11"),
            HighwayRecord("Y30EGA6IKO3NGRFZL3IY 05:15:11:19 exit 0"),
            HighwayRecord("LZ 05:01:12:07 exit 82"),
            HighwayRecord("BOCRA 05:30:14:26 enter 47"),
            HighwayRecord("PR8OLVNX2SATF4G 05:13:10:29 enter 77"),
            HighwayRecord("GLBUVL2TPTUCVR8MKMC 05:28:04:58 exit 59"),
            HighwayRecord("QPM870QV4D1CLWI1 05:22:02:00 enter 55"),
            HighwayRecord("ZI67765FTJ 05:20:11:16 enter 26"),
            HighwayRecord("I7LP 05:11:12:46 exit 84"),
            HighwayRecord("MW4CVD2 05:04:16:21 exit 99"),
            HighwayRecord("RZ423QQYDTRHE 05:26:09:52 enter 77"),
            HighwayRecord("YN0NO2YHIAA 05:22:12:47 enter 27"),
            HighwayRecord("6D51YFQB 05:17:01:49 exit 31"),
            HighwayRecord("6Z 05:24:13:06 exit 42"),
            HighwayRecord("YSDV2CMK49I 05:19:19:02 exit 5"),
            HighwayRecord("J3WZWPO 05:12:10:05 exit 38"),
            HighwayRecord("TJY1Q 05:22:23:33 enter 25"),
            HighwayRecord("TYQTZDE 05:24:22:06 enter 52"),
            HighwayRecord("AY 05:19:01:46 exit 97"),
            HighwayRecord("JTLC2 05:09:23:27 exit 64"),
            HighwayRecord("3112OV4J6 05:01:10:28 exit 9"),
            HighwayRecord("TDDBGG2NDZH 05:28:03:03 enter 16"),
            HighwayRecord("VB5NA 05:08:07:32 enter 15"),
            HighwayRecord("22WHS9NTB3Y0TUKY 05:29:14:46 exit 99"),
            HighwayRecord("AY 05:29:09:29 exit 81"),
            HighwayRecord("HBQ 05:08:06:52 enter 44"),
            HighwayRecord("ZBCXBO9JBXN 05:11:23:00 enter 52"),
            HighwayRecord("4RTV 05:12:00:24 exit 90"),
            HighwayRecord("BOCRA 05:15:04:09 exit 2"),
            HighwayRecord("9WJ 05:05:01:14 exit 36"),
        ]

        results = get_all_billing_records(
            tolls,
            highway_records
        )

        self.assertEqual(6, len(results))

        self.assertEqual("1DSRVW3VVCB8SIY", results[0].license_number)
        self.assertEqual(380, results[0].get_bill_amount())

        self.assertEqual("6D51YFQB", results[1].license_number)
        self.assertEqual(365, results[1].get_bill_amount())

        self.assertEqual("AY", results[2].license_number)
        self.assertEqual(1212, results[2].get_bill_amount())

        self.assertEqual("GLBUVL2TPTUCVR8MKMC", results[3].license_number)
        self.assertEqual(428, results[3].get_bill_amount())

        self.assertEqual("QPM870QV4D1CLWI1", results[4].license_number)
        self.assertEqual(318, results[4].get_bill_amount())

        self.assertEqual("VB5NA", results[5].license_number)
        self.assertEqual(876, results[5].get_bill_amount())

    def test_202(self):
        """Should work for second debug example"""
        tolls = [15, 13, 73, 25, 67, 37, 94, 98, 34, 66, 42, 34, 98, 56, 28, 14, 86, 83, 82, 49, 4, 92, 91, 99]

        highway_records = [
            HighwayRecord("alfryoy 09:18:17:51 enter 84"),
            HighwayRecord("alfryoy 09:03:18:01 exit 538"),
            HighwayRecord("zdqpndojfie 09:02:01:58 enter 730"),
            HighwayRecord("dbqu 09:21:04:06 enter 712"),
            HighwayRecord("qivqw 09:00:20:46 enter 791"),
            HighwayRecord("wowgjskfejiknuzcfa 09:05:04:30 enter 812"),
            HighwayRecord("vcz 09:19:23:25 enter 812"),
            HighwayRecord("cgbkmnjbpxhzolafhpnd 09:18:03:48 exit 149"),
            HighwayRecord("wowgjskfejiknuzcfa 09:11:14:23 exit 10"),
            HighwayRecord("zdqpndojfie 09:15:22:04 exit 944"),
            HighwayRecord("uahelxnamgj 09:06:07:00 exit 18"),
            HighwayRecord("ciqsvtzekmjpjylrjf 09:02:03:40 exit 737"),
            HighwayRecord("uk 09:17:18:31 exit 885"),
            HighwayRecord("alfryoy 09:18:00:42 enter 945"),
            HighwayRecord("ciqsvtzekmjpjylrjf 09:02:18:02 enter 198"),
            HighwayRecord("a 09:06:22:50 enter 293"),
            HighwayRecord("zdqpndojfie 09:29:23:55 exit 887"),
            HighwayRecord("cgbkmnjbpxhzolafhpnd 09:05:22:03 exit 981"),
            HighwayRecord("vcz 09:29:00:28 enter 986"),
            HighwayRecord("gwojjokuw 09:26:04:08 exit 290"),
            HighwayRecord("wowgjskfejiknuzcfa 09:00:13:32 enter 455"),
            HighwayRecord("wowgjskfejiknuzcfa 09:19:22:41 enter 857"),
            HighwayRecord("cgbkmnjbpxhzolafhpnd 09:11:21:54 enter 52"),
            HighwayRecord("gwojjokuw 09:24:19:00 enter 825"),
            HighwayRecord("ojny 09:18:08:10 enter 453"),
            HighwayRecord("vcz 09:24:17:17 enter 315"),
            HighwayRecord("ojny 09:24:22:19 enter 973"),
            HighwayRecord("a 09:18:08:42 exit 203"),
            HighwayRecord("wowgjskfejiknuzcfa 09:23:01:29 exit 844"),
            HighwayRecord("cgbkmnjbpxhzolafhpnd 09:23:20:59 exit 812"),
            HighwayRecord("kzenhsjjzhsstidoabcz 09:13:18:29 exit 756"),
            HighwayRecord("uk 09:08:01:51 exit 271"),
            HighwayRecord("wowgjskfejiknuzcfa 09:28:13:32 enter 506"),
            HighwayRecord("qivqw 09:08:11:17 enter 264"),
            HighwayRecord("wowgjskfejiknuzcfa 09:05:19:57 enter 952"),
            HighwayRecord("kzenhsjjzhsstidoabcz 09:18:10:47 exit 429"),
            HighwayRecord("alfryoy 09:13:09:08 enter 228"),
            HighwayRecord("kzenhsjjzhsstidoabcz 09:10:09:01 exit 219"),
            HighwayRecord("kzenhsjjzhsstidoabcz 09:02:08:59 exit 338"),
            HighwayRecord("cgbkmnjbpxhzolafhpnd 09:02:19:35 exit 59"),
            HighwayRecord("ciqsvtzekmjpjylrjf 09:20:15:53 exit 456"),
            HighwayRecord("a 09:15:17:03 exit 106"),
            HighwayRecord("a 09:15:06:21 enter 975"),
            HighwayRecord("qivqw 09:07:00:12 enter 169"),
            HighwayRecord("cgbkmnjbpxhzolafhpnd 09:04:00:25 exit 215"),
            HighwayRecord("uk 09:16:12:23 enter 927"),
            HighwayRecord("wowgjskfejiknuzcfa 09:26:06:33 enter 818"),
            HighwayRecord("uk 09:16:17:29 exit 673"),
            HighwayRecord("alfryoy 09:11:20:25 enter 111"),
            HighwayRecord("a 09:06:09:18 enter 774"),
            HighwayRecord("uk 09:28:14:02 enter 604"),
            HighwayRecord("kzenhsjjzhsstidoabcz 09:13:13:12 enter 593"),
            HighwayRecord("dbqu 09:19:13:07 exit 290"),
            HighwayRecord("qivqw 09:26:11:24 exit 577"),
            HighwayRecord("cgbkmnjbpxhzolafhpnd 09:15:14:20 enter 860"),
            HighwayRecord("wowgjskfejiknuzcfa 09:00:22:09 enter 324"),
            HighwayRecord("cgbkmnjbpxhzolafhpnd 09:23:06:58 exit 548"),
            HighwayRecord("zdqpndojfie 09:29:10:44 enter 869"),
            HighwayRecord("kzenhsjjzhsstidoabcz 09:10:05:18 exit 906"),
            HighwayRecord("alfryoy 09:10:21:33 exit 231"),
            HighwayRecord("alfryoy 09:29:15:56 enter 937"),
            HighwayRecord("qivqw 09:28:13:42 enter 128"),
        ]

        results = get_all_billing_records(
            tolls,
            highway_records
        )

        self.assertEqual(9, len(results))

