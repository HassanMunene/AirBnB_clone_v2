"""
This module includes the test cases for the console
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
import console
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """
    This is a class for testing the console
    """
    def setUp(self):
        self.command = HBNBCommand()

    def tearDowm(self):
        pass

    def test_console_module_docstring(self):
        """
        test if the console module is documented
        """
        self.assertIsNot(console.__doc__, None, 'console.py needs to be documented')
        self.assertTrue(len(console.__doc__) >= 1, 'console.py docstring must be more than 1 line')

    def test_HBNBCommad_Documentation(self):
        """
        test if HBNBCommand class is documented
        """
        self.assertIsNot(HBNBCommand.__doc__, None, "You have to document the class")

    def test_prompt(self):
        """test if the prompt is as it should be"""
        self.assertEqual(self.command.prompt, '(hbnb) ')

