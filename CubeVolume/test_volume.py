#Unittest module for volume.py

import unittest
import volume

def test_Volume(self):
    self.assertEqual(volume.Volume(10), 1000)   #Pass condition 
    self.assertEqual(volume.Volume(-5), -125)   #Fail condition, code does not accept negative numbers
    self.assertEqual(volume.Volume("hi"), 45)   #Fail condition, code does not accept a string as a parameter

if __name__ == "__main__":
    unittest.main()