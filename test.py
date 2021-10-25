import unittest
import anagram_check
class InequalityTest(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(anagram_check.check_anagaram("listen" , "silent") , "listen is anagrams with silent")

    def test_not_equal(self):
        self.assertEqual(anagram_check.check_anagaram("Sonu" , "Monu") , "Sonu aren't anagrams with Monu")

if __name__ == '__main__':
    unittest.main()