#!/usr/bin/python3

import unittest
from io import StringIO
from airbnbconsole import Console
import sys

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.airbnbconsole = Console()

    def test_help(self):
        # Redirect stdout to capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        self.airbnbconsole.help()
        expected_output = "\nDocumented commands (type help <topic>):\n========================================\nEOF  help  quit\n\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

        # Reset stdout
        sys.stdout = sys.__stdout__

    def test_non_interactive_mode(self):
        # Redirect stdout to capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        self.airbnbconsole.non_interactive()
        expected_output = "\nDocumented commands (type help <topic>):\n========================================\nEOF  help  quit\n\n(hbnb) "
        self.assertEqual(captured_output.getvalue(), expected_output)

        # Reset stdout
        sys.stdout = sys.__stdout__

    def test_loop(self):
        # Mock user input
        inputs = ['help', 'quit']
        original_input = airbnbconsole.input
        airbnbconsole.input = lambda _: inputs.pop(0)

        # Redirect stdout to capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        self.airbnbconsole.loop()
        expected_output = "\nDocumented commands (type help <topic>):\n========================================\nEOF  help  quit\n\n(hbnb) "
        self.assertEqual(captured_output.getvalue(), expected_output)

        # Reset stdout and console.input
        sys.stdout = sys.__stdout__
        airbnbconsole.input = original_input

if __name__ == '__main__':
    unittest.main()

