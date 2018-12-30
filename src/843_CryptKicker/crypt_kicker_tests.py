import unittest

from crypt_kicker import crypt_decrypt, SingleWord


class CryptKickerTests(unittest.TestCase):
    def test_200(self):
        """Should return no solution when work is not letter possible for a long word"""
        dictionary = ["documentation"]

        result = crypt_decrypt("nymewoxdkdsax", dictionary)
        self.assertEqual("*************", result)

    def test_201(self):
        """Should return no solution when long word does not have matching word length"""
        dictionary = ["documentation"]

        result = crypt_decrypt("nymewoxdkdsy", dictionary)
        self.assertEqual("************", result)

    def test_202(self):
        """Should return hit for a single long word"""
        dictionary = ["documentation"]

        result = crypt_decrypt("nymewoxdkdsyx", dictionary)
        self.assertEqual("documentation", result)

    def test_203(self):
        """Should return hit for a single long word"""
        dictionary = ["documentation"]

        result = crypt_decrypt("nymewoxdkdsyx nymewoxdkdsyx", dictionary)
        self.assertEqual("documentation documentation", result)

    def test_204(self):
        """Should return hit for two words with no common letters"""
        dictionary = ["fun", "ask"]

        result = crypt_decrypt("pex kcu", dictionary)
        self.assertNotEqual("*** ***", result)
        self.assertTrue(result == "fun ask" or result == "ask fun", "result was : " + result)

    def test_205(self):
        """Should return hit for two words"""
        dictionary = ["fun", "foo"]

        result = crypt_decrypt("pex pyy", dictionary)
        self.assertEqual("fun foo", result)

        result = crypt_decrypt("pyy pex", dictionary)
        self.assertEqual("foo fun", result)

        dictionary = ["foo", "fun"]

        result = crypt_decrypt("pex pyy", dictionary)
        self.assertEqual("fun foo", result)

        result = crypt_decrypt("pyy pex", dictionary)
        self.assertEqual("foo fun", result)

    def test_206(self):
        """Should return no solution when solution is NOT letter possible"""

        dictionary = ["fol", "foo"]

        result = crypt_decrypt("pex pyy", dictionary)
        self.assertEqual("*** ***", result)

        result = crypt_decrypt("pyy pex", dictionary)
        self.assertEqual("*** ***", result)

        dictionary = ["foo", "fol"]

        result = crypt_decrypt("pex pyy", dictionary)
        self.assertEqual("*** ***", result)

        result = crypt_decrypt("pyy pex", dictionary)
        self.assertEqual("*** ***", result)

    def test_207(self):
        """Should return no solution when solution is NOT letter possible"""

        dictionary = ["fun", "ask"]

        result = crypt_decrypt("pex kpu", dictionary)
        self.assertEqual("*** ***", result)

        result = crypt_decrypt("kpu pex", dictionary)
        self.assertEqual("*** ***", result)


    # ***********

    def test_100(self):
        dictionary = ["foo"]

        result = crypt_decrypt("      ", dictionary)
        self.assertEqual(None, result)

    def test_101(self):
        dictionary = ["foo"]

        result = crypt_decrypt("  afs  ", dictionary)
        self.assertEqual("***", result)

        result = crypt_decrypt("  aff  ", dictionary)
        self.assertEqual("foo", result)

    def test_102(self):
        dictionary = ["dog", "cat", "web"]

        result = crypt_decrypt("xyz abc pqr", dictionary)
        self.assertIn(result, ["cat web dog", "cat dog web", "web cat dog", "web dog cat", "dog cat web", "dog web cat"])

    def test_103(self):
        dictionary = ["aa"]

        result = crypt_decrypt("  bc      bf", dictionary)
        self.assertEqual("** **", result)

    def test_104(self):
        dictionary = ["foo"]

        result = crypt_decrypt("  aas    ", dictionary)
        self.assertEqual("***", result)

    def test_105(self):
        dictionary = ["foo"]

        result = crypt_decrypt("  ass    ", dictionary)
        self.assertEqual("foo", result)

    def test_106(self):
        dictionary = ["foo", "bas"]

        result = crypt_decrypt("  ass  qck    ass ", dictionary)
        self.assertEqual("foo bas foo", result)

    def test_001(self):
        """Should return the empty string given an empty string"""
        dictionary = []

        result = crypt_decrypt("", dictionary)
        self.assertEqual(None, result)

        result = crypt_decrypt(" ", dictionary)
        self.assertEqual(None, result)

    def test_002(self):
        """Should return the empty string given an empty string and anything in the decrypted words"""
        dictionary = ["some stuff"]

        result = crypt_decrypt("", dictionary)
        self.assertEqual(None, result)

        result = crypt_decrypt("  ", dictionary)
        self.assertEqual(None, result)

    def test_003(self):
        """Should return the expected result given a single letter for encrypted and decrypted words"""
        dictionary = ["a"]
        result = crypt_decrypt("b", dictionary)
        self.assertEqual("a", result)

        dictionary = ["c"]
        result = crypt_decrypt("b", dictionary)
        self.assertEqual("c", result)

        dictionary = ["e"]
        result = crypt_decrypt("b", dictionary)
        self.assertEqual("e", result)

    def test_004(self):
        """Should return first possible result when single letter has more than one solution"""
        dictionary = ["a", "b"]
        result = crypt_decrypt("c", dictionary)
        self.assertIn(result, ["a", "b"])

        dictionary = ["c", "d"]
        result = crypt_decrypt("a", dictionary)
        self.assertIn(result, ["c", "d"])

    def test_005(self):
        """Should return expected solution given two single letter dictionary and two single letter encrypted words"""
        dictionary = ["a", "b"]

        result = crypt_decrypt("c d", dictionary)
        self.assertIn(result, ["a b", "b a"])

        result = crypt_decrypt("d c", dictionary)
        self.assertIn(result, ["a b", "b a"])

        result = crypt_decrypt("c d d", dictionary)
        self.assertIn(result, ["a b b", "b a a"])

        result = crypt_decrypt("c c d", dictionary)
        self.assertIn(result, ["a a b", "b b a"])

    def test_006(self):
        """Should return no solution given two single letter words without single solution"""
        dictionary = ["a"]
        result = crypt_decrypt("b c", dictionary)
        self.assertEqual("* *", result)

        dictionary = ["z"]
        result = crypt_decrypt("b c", dictionary)
        self.assertEqual("* *", result)

    def test_007(self):
        """Should return expected solution given two single letter words"""
        dictionary = ["a"]
        result = crypt_decrypt("c c", dictionary)
        self.assertEqual("a a", result)

    def test_008(self):
        """Should return expected solution given three single letter words"""
        dictionary = ["a"]
        result = crypt_decrypt("c c c", dictionary)
        self.assertEqual("a a a", result)

    def test_009(self):
        """Should not return solution given two letter words with no solution"""
        dictionary = ["aa"]
        result = crypt_decrypt("bb cc", dictionary)
        self.assertEqual("** **", result)

    def test_010(self):
        """Should return solution with three letters"""
        dictionary = ["aab", "aac"]
        result = crypt_decrypt("xxy xxz", dictionary)
        self.assertIn(result, ["aac aab", "aab aac"])

    def test_011(self):
        """Should not return solution when two letter words have no solution can a change in letters"""
        dictionary = ["ab"]
        result = crypt_decrypt("bc cd", dictionary)
        self.assertEqual("** **", result)

        dictionary = ["ab"]
        result = crypt_decrypt("bc bd", dictionary)
        self.assertEqual("** **", result)

        dictionary = ["ab"]
        result = crypt_decrypt("cc dd", dictionary)
        self.assertEqual("** **", result)

    def test_012(self):
        """Should return expected solution when two letter words have single solution for both words"""
        dictionary = ["aa"]
        result = crypt_decrypt("bb bb", dictionary)
        self.assertEqual("aa aa", result)

    def test_013(self):
        """Should return expected solution two letter words have single solution with different letters"""
        dictionary = ["ab"]
        result = crypt_decrypt("bc bc", dictionary)
        self.assertEqual("ab ab", result)

    def test_014(self):
        """Should return expected solution when duplication decrypted words are given"""
        dictionary = ["ab", "ab"]
        result = crypt_decrypt("xy", dictionary)
        self.assertEqual("ab", result)

    def test_015(self):
        """Should return one of multiple solutions with two letters"""
        dictionary = ["ab", "cd"]
        result = crypt_decrypt("xy xy", dictionary)
        self.assertIn(result, ["ab ab", "cd cd"])

        dictionary = ["cd", "ab"]
        result = crypt_decrypt("xy xy", dictionary)
        self.assertIn(result, ["ab ab", "cd cd"])

    def test_016(self):
        """Should not return solution when encrypted word length do not match decrypted word length"""
        dictionary = ["a"]
        result = crypt_decrypt("xy", dictionary)
        self.assertEqual("**", result)

        dictionary = ["ab"]
        result = crypt_decrypt("xyz", dictionary)
        self.assertEqual("***", result)

    def test_017(self):
        """Should not return solution when words are not letter possible"""
        dictionary = ["ab"]
        result = crypt_decrypt("xx", dictionary)
        self.assertEqual("**", result)

        dictionary = ["abc"]
        result = crypt_decrypt("xxy", dictionary)
        self.assertEqual("***", result)

    def test_018(self):
        """Should not return solution word is not letter possible with duplicate letters"""
        dictionary = ["aba"]
        result = crypt_decrypt("xyx", dictionary)
        self.assertEqual("aba", result)

    def test_019(self):
        """Should return solution when one of multiple solutions with two letters where first decrypted word is rejected"""
        dictionary = ["xx", "cd"]
        result = crypt_decrypt("xy", dictionary)
        self.assertEqual("cd", result)

    def test_020(self):
        """Should return solution with single encrypted word and single decrypted word"""
        dictionary = ["abc"]
        result = crypt_decrypt("xyz", dictionary)
        self.assertEqual("abc", result)

    def test_021(self):
        """Should return solution there are more that two solutions"""
        dictionary = ["ab", "bc", "de", "fg"]
        result = crypt_decrypt("hi hi", dictionary)
        self.assertIn(result, ["ab ab", "bc bc", "de de", "fg fg"])

    def test_022(self):
        """Should use single option as a way of clearing all other options that match by letter"""
        dictionary = ["bc", "ab", "bb"]
        result = crypt_decrypt("yy xy yz", dictionary)
        self.assertEqual("bb ab bc", result)

    def test_023(self):
        """Should find solution that ONLY is solved by letter maps"""
        dictionary = ["eb", "bc"]

        result = crypt_decrypt("yz xy", dictionary)
        self.assertEqual("bc eb", result)

        result = crypt_decrypt("xy yz", dictionary)
        self.assertEqual("eb bc", result)

    def test_024(self):
        """Should return solution by using letters that match across different words"""
        dictionary = ["ef", "ab", "bc"]
        result = crypt_decrypt("xy yz", dictionary)
        self.assertEqual("ab bc", result)

    def test_025(self):
        """Should leave spaces in solution intact"""
        dictionary = ["cd"]
        result = crypt_decrypt("ab  ab", dictionary)
        self.assertEqual("cd cd", result)

    def test_026(self):
        """Should leave spaces in no solution intact"""
        dictionary = ["xx"]
        result = crypt_decrypt("ab    ab", dictionary)
        self.assertEqual("** **", result)

    def test_sample_input_should_pass(self):
        """Should return expected solution from the directions sample"""
        dictionary = ["and", "dick", "jane", "puff", "spot", "yertle"]

        result = crypt_decrypt("bjvg xsb hxsn xsb qymm xsb rqat xsb pnetfn", dictionary)
        self.assertEqual("dick and jane and puff and spot and yertle", result)

        result = crypt_decrypt("xxxx yyy zzzz www yyyy aaa bbbb ccc dddddd", dictionary)
        self.assertEqual("**** *** **** *** **** *** **** *** ******", result)

    def test_udebug_5(self):
        """Should return expected solution from the directions sample"""
        dictionary = ["ball", "is", "a", "uses",
                      "not", "one", "two", "too", "i", "like", "also", "are",
                      "no", "btw", "by", "the", "way"]

        result = crypt_decrypt("a ybhd baic oks", dictionary)
        self.assertEqual("i also like btw", result)

    def test_udebug_1(self):
        """Should return expected solution from the directions sample"""
        dictionary = ["baseball", "football", "basketball", "tennis", "ball", "is", "a", "sport", "which", "uses",
                      "not", "one", "two", "player", "players", "too", "i", "like", "also", "these", "are", "sports",
                      "soccer", "no", "chess", "btw", "by", "the", "way"]

        result = crypt_decrypt("a ybhd baic hdttcu oks", dictionary)
        self.assertEqual("i also like soccer btw", result)

        result = crypt_decrypt("c pu iuo hcsw owiict", dictionary)
        self.assertEqual("* ** *** **** ******", result)

        result = crypt_decrypt("a ybhd baic hdttcu", dictionary)
        self.assertEqual("i also like soccer", result)

        result = crypt_decrypt("lrsglrww as r sexvh", dictionary)
        self.assertEqual("baseball is a sport", result)

        result = crypt_decrypt("dffbqtoo sk t kjfcb bff", dictionary)
        self.assertEqual("football is a sport too", result)

        result = crypt_decrypt("knnwqndd hg j gmnbw wnn", dictionary)
        self.assertEqual("******** ** * ***** ***", result)

        result = crypt_decrypt("u wuqe bdaebdww", dictionary)
        self.assertEqual("i like baseball", result)

        result = crypt_decrypt("c pu iuo hcsw owiict", dictionary)
        self.assertEqual("* ** *** **** ******", result)

        result = crypt_decrypt("xhwkw fiw kldixk xwzzak yddxmfjj mfkqwxmfjj mfkwmfjj", dictionary)
        self.assertEqual("these are sports tennis football basketball baseball", result)

        result = crypt_decrypt("micvc tbc vwfbmv mff mchhev pffmdtoo dtvacmdtoo dtvcdtoo jicvv", dictionary)
        self.assertEqual("these are sports too tennis football basketball baseball chess", result)

        result = crypt_decrypt("mysrs bus rehumr mhh msggar ohhmjbxx jbrksmjbxx jbrsjbxx rkaagq", dictionary)
        self.assertEqual("***** *** ****** *** ****** ******** ********** ******** ******", result)

        result = crypt_decrypt("miana pfa ndcfmn mcc mallbn sccmqpjj qpnoamqpjj qpnaqpjj nceeaf", dictionary)
        self.assertEqual("these are sports too tennis football basketball baseball soccer", result)

        result = crypt_decrypt("w rvez vwum ezkkmg dj psm trj", dictionary)
        self.assertEqual("i also like soccer by the way", result)

        result = crypt_decrypt("b fkry kbew ryggwa qu liw tfurbvw", dictionary)
        self.assertEqual("* **** **** ****** ** *** *******", result)

    def test_udebug_2(self):
        """Should return expected solution from the directions sample"""
        dictionary = ["one",
                      "two",
                      "three",
                      "four",
                      "five",
                      "six",
                      "seven",
                      "eight",
                      "nine",
                      "ten",
                      "eleven",
                      "twelve",
                      "thirteen",
                      "fourteen",
                      "fifteen",
                      "banana",
                      "apple",
                      "cucumber",
                      "something",
                      "else",
                      "must",
                      "do",
                      "for",
                      "this",
                      "is",
                      "boring"]

        result = crypt_decrypt("aa", dictionary)
        self.assertEqual("**", result)

        result = crypt_decrypt("abcdefg", dictionary)
        self.assertEqual("*******", result)

        result = crypt_decrypt("qlc pcf xvotq qlxhix pvix nsnsdjxf", dictionary)
        self.assertEqual("two for eight twelve five cucumber", result)

        result = crypt_decrypt("lmen cu jfjfxaeb smeyne sdcbseez sdcu wlfb wcwseez uco wcne aizizi albczk sez", dictionary)
        self.assertEqual("**** ** ******** ****** ******** **** **** ******* *** **** ****** ****** ***", result)

        result = crypt_decrypt("its ibnz kwwqd fncd zsxdibnrj phphxlda fshaiddr itdqcd nz", dictionary)
        self.assertEqual("two this apple five something cucumber fourteen twelve is", result)

        result = crypt_decrypt("bfupxiim xcre fmi duex re ztmtmt zfprmv eisim irvcx", dictionary)
        self.assertEqual("fourteen this one must is banana boring seven eight", result)

        result = crypt_decrypt("nbi nsbmlb xirydqqn inq siylnh dalk nlnq xljq lk kqjqn", dictionary)
        self.assertEqual("*** ****** ******** *** ****** **** **** **** ** *****", result)

        result = crypt_decrypt("obf okzc brbmbf tngx czp tnx ojn tngxobbf", dictionary)
        self.assertEqual("ten this eleven four six for two fourteen", result)

        result = crypt_decrypt("hthyhv uirqohhv xi ohv bhyhv aiqgvj bifhosgvj ivh bgd frbo", dictionary)
        self.assertEqual("eleven fourteen do ten seven boring something one six must", result)

        result = crypt_decrypt("za yplplp asphn ajazak qtin moxskp", dictionary)
        self.assertEqual("** ****** ***** ****** **** ******", result)

        result = crypt_decrypt("ejn eiftbqjak xrxrfdtu je ajat ixbt dxxju zdbdbd", dictionary)
        self.assertEqual("*** ********* ******** ** **** **** ***** ******", result)

        result = crypt_decrypt("iona ettka flfluyaz ulcm yxzowp akca canaw mvx xwa cod mhozmaaw aophm maw ixlz", dictionary)
        self.assertEqual("five apple cucumber must boring else seven two one six thirteen eight ten four", result)

        result = crypt_decrypt("vewii fpi irsev myyni gf ru vlf prpi kfw", dictionary)
        self.assertEqual("three one eight apple do is two nine for", result)

        result = crypt_decrypt("koe vrxrg se ruvr egr", dictionary)
        self.assertEqual("two seven do else one", result)

        result = crypt_decrypt("gj jev qsj xjt qmnb bvyve bno izbq vfvyve raeaea xjztqvve qmtvv", dictionary)
        self.assertEqual("do one two for this seven six must eleven banana fourteen three", result)

        result = crypt_decrypt("aip tzbcc tdq ia lflfuscb cwcncr xqb xqfb sqbire tcr svrvrv xixtccr ciezt xinc", dictionary)
        self.assertEqual("six three two is cucumber eleven for four boring ten banana fifteen eight five", result)

        result = crypt_decrypt("sfsysl ozgss itithusg arp ovsfys jrys uegrlc htao jrjossl osl jeg", dictionary)
        self.assertEqual("eleven three cucumber six twelve five boring must fifteen ten for", result)

        result = crypt_decrypt("kuv mk qedo alzqub eqck dkcku eliz elz kykcku pskyck", dictionary)
        self.assertEqual("*** ** **** ****** **** ***** **** *** ****** ******", result)

        result = crypt_decrypt("laaug bixfjggw bixf gung ngmgw", dictionary)
        self.assertEqual("apple fourteen four else seven", result)

        result = crypt_decrypt("ushg cost ciym cicgmmd ko orugf fgrafooe mwzofgreu mrb", dictionary)
        self.assertEqual("**** **** **** ******* ** ***** ******** ********* ***", result)

        result = crypt_decrypt("zuml sbscsx vursatwxk zumlassx egxgxg atwv uxs vwj asx zwzassx atlss vscsx", dictionary)
        self.assertEqual("four eleven something fourteen banana this one six ten fifteen three seven", result)

        result = crypt_decrypt("iecdn yjl kpwn xj rgvgvg yjplniiv upupkril nqj niv jvi ndelniiv wez yeoi", dictionary)
        self.assertEqual("eight for must do banana fourteen cucumber two ten one thirteen six five", result)

        result = crypt_decrypt("evl ncococ ad hstawm yjyxyw", dictionary)
        self.assertEqual("*** ****** ** ****** ******", result)

        result = crypt_decrypt("giiej fnhp qrqj lrv whwhzxjp ujq usn xgqgqg", dictionary)
        self.assertEqual("apple four nine six cucumber ten two banana", result)

        result = crypt_decrypt("bubycck un ywuzycck djny cuqwy ywzcc vlwlk iuuzl otwl ojb ejbtkq vtc ojsb lzvl", dictionary)
        self.assertEqual("******* ** ******** **** ***** ***** ***** ***** **** *** ****** *** **** ****", result)

        result = crypt_decrypt("lqj kfrfrf nimecm gq myuxn nca njtxqhcmp xrnx wjlcmp qhlxx", dictionary)
        self.assertEqual("*** ****** ****** ** ***** *** ********* **** ****** *****", result)

        result = crypt_decrypt("vdvk zwckk zwdczkkv ujekzwdvy kxuk mjc", dictionary)
        self.assertEqual("nine three thirteen something else for", result)

        result = crypt_decrypt("fuo xfjaboou odhpb xdno ndti lx iabss srts vxbjcg iyx", dictionary)
        self.assertEqual("*** ******** ***** **** **** ** ***** **** ****** ***", result)

        result = crypt_decrypt("hwx vxar hwqbmq lx pggbq okoq", dictionary)
        self.assertEqual("two four twelve do apple nine", result)

        result = crypt_decrypt("evck lzhuexxs lclexxs efz lzu ck mhmhwixu evuxx scsx xdxnxs kzwxevcso lzhu izucso efxdnx", dictionary)
        self.assertEqual("this fourteen fifteen two for is cucumber three nine eleven something four boring twelve", result)

        result = crypt_decrypt("ngrgc nmt omrg fxxhg ueymcs lqghrg cmcg", dictionary)
        self.assertEqual("seven six five apple boring twelve nine", result)

        result = crypt_decrypt("xdkbxjjg xdkn xvw gkgj xdbjj qkzj jkfdx qwmbxjjg qkqxjjg lmt bx qnxd detcut", dictionary)
        self.assertEqual("******** **** *** **** ***** **** ***** ******** ******* *** ** **** ******", result)

        result = crypt_decrypt("iaqu wh teqt bhdlsz uph ucdtt lq slst jljutts mamaibtd uclq", dictionary)
        self.assertEqual("must do else boring two three is nine fifteen cucumber this", result)

        result = crypt_decrypt("ljdxv rql vglyhl kjhl srolvxjqd ir js", dictionary)
        self.assertEqual("eight one twelve five something do is", result)

        result = crypt_decrypt("df nxrn yfjpts yctctc rpl", dictionary)
        self.assertEqual("do else boring banana six", result)

        result = crypt_decrypt("hukl vspbnj kodon ltpoo oqodon bk abdo iccqo objtl ksholtbnj", dictionary)
        self.assertEqual("must boring seven three eleven is five apple eight something", result)

        result = crypt_decrypt("ybyqyl gmqy sumpsyyl gxep svybqy supyy svx", dictionary)
        self.assertEqual("eleven five thirteen four twelve three two", result)

        result = crypt_decrypt("tmjfuj odpztjje tmd odz nh onuj jnbxt onotjje", dictionary)
        self.assertEqual("twelve fourteen two for is five eight fifteen", result)

        result = crypt_decrypt("dmdldz ihxzinna bdgzinna bdgz kd uhyt gygc", dictionary)
        self.assertEqual("****** ******** ******** **** ** **** ****", result)

        result = crypt_decrypt("oupxk hed hesd kxdoo koy kroqco zeduyp huco", dictionary)
        self.assertEqual("eight for four three ten twelve boring five", result)

        result = crypt_decrypt("kakm zigc zic bykyky ikm tao dqat demwjm dqacdmmk jn mr", dictionary)
        self.assertEqual("**** **** *** ****** *** *** **** ****** ******** ** **", result)

        result = crypt_decrypt("hpbwdinax ctctbqwg optg onmw drp hny kp anaw hwmwa drwemw bthd paw", dictionary)
        self.assertEqual("something cucumber four five two six do nine seven twelve must one", result)


    def test_SingleWord_test001(self):
        sw = SingleWord("a")
        self.assertEqual("a", sw.word)
        self.assertEqual("a", sw.unique_letter_word)

    def test_SingleWord_test002(self):
        sw = SingleWord("ab")
        self.assertEqual("ab", sw.word)
        self.assertEqual("ab", sw.unique_letter_word)

    def test_SingleWord_test004(self):
        sw = SingleWord("aa")
        self.assertEqual("aa", sw.word)
        self.assertEqual("a", sw.unique_letter_word)

    def test_SingleWord_test005(self):
        sw = SingleWord("aabb")
        self.assertEqual("aabb", sw.word)
        self.assertEqual("ab", sw.unique_letter_word)

def main():
    unittest.main()


if __name__ == '__main__':
    main()
