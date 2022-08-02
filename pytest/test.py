import unittest

from example import panagram,palindrome,pramaility,frequency

class TestDiv(unittest.TestCase):
    def test_panagram(self):
        assert panagram("the quick brown fox jumps over the lazy dog") == True
        assert not panagram("the quick brown fox jumped over the lazy dog") == True

    def test_palindrome (self):
        self.assertEqual(palindrome(121),True)
        self.assertEqual(palindrome(122),False)
    
    def test_pramility (self):
        self.assertEqual(pramaility(13),True)
        self.assertNotEqual(pramaility(13),False)
    
    def test_frequency (self):
        assert frequency('aabbbc') == {'a': 2, 'c': 1, 'b': 3}
