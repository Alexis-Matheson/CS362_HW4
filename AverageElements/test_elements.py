#Unittest module for elements.py

import unittest
import elements

def test_average(self):
    self.assertEqual(elements.average([94,57,35]), 62.00)   #Pass condition
    self.assertEqual(elements.average(["h"]), 56)           #Fail condition, code cannot find the average of a character
    self.assertEqual(elements.average([-5,-5]), -5)

def test_createList(self):
    self.assertEqual(elements.createList(-4), 0)            #Fail condition, code does not generate list when given a negative number
    self.assertEqual(elements.createList(0), [])            #input 0 to create and empty array

if __name__ == "__main__":
    unittest.main()