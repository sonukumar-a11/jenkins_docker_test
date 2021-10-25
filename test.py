import unittest
import anagram_check
class InequalityTest(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(anagram_check.check_anagaram("listen" , "silent") , "listen is anagrams with silent")

    def test_not_equal(self):
        self.assertNotEqual(anagram_check.check_anagaram("Sonu" , "Mnuo") , "Sonu aren't anagrams with Monu")
    
    def test_not_found(self):
        self.assertEqual(anagram_check.check_anagaram("Sonu" , "Mnuo") , "Sonu aren't anagrams with Mnuo")

if __name__ == '__main__':
    unittest.main()