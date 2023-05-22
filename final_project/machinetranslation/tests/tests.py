
from ..translator import english_to_french, french_to_english
import unittest

class TestFrenchTranslator(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french("null"), "Bonjour")
        self.assertEqual(english_to_french("Hello"), "Bonjour") 

class TestEnglishTranslator(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english("null"), "Hello")
        self.assertEqual(french_to_english("Bonjour"), "Hello") 

unittest.main()