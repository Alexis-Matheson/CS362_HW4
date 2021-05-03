#Unittest file to test firstlast.py name generator

import unittest
import firstlast

def test_validate(self):
    self.assertEqual(firstlast.validate("Alexis"), True)        #Pass condition, this is a valid name
    self.assertEqual(firstlast.validate("Matheson"), False)     #Fail condition, this is a valid name
    self.assertEqual(firstlast.validate("12345"), True)         #Fail condition, this name is invalid

