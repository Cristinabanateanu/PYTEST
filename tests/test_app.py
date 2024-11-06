# test_app.py
import sys
import os
import unittest
from unittest.mock import patch
import io


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from app import to_uppercase, to_lowercase, main
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
# UNIT TESTS
class TestAppUnit(unittest.TestCase):
    """
    Unit tests for basic string transformation functions (to_uppercase and to_lowercase).
    These tests verify that the functions behave as expected with typical inputs.
    """

    def test_to_uppercase(self):
        """
        Test to verify the to_uppercase function:
        
        - Checks that lowercase letters are converted to uppercase correctly.
        - Verifies that mixed-case strings are fully converted to uppercase.
        - Ensures that numeric strings are unaffected by the transformation.
        """
        self.assertEqual(to_uppercase("hello"), "HELLO")
        self.assertEqual(to_uppercase("Hello World!"), "HELLO WORLD!")
        self.assertEqual(to_uppercase("1234"), "1234")  # Test with numbers

    def test_to_lowercase(self):
        """
        Test to verify the to_lowercase function:
        
        - Checks that uppercase letters are converted to lowercase correctly.
        - Verifies that mixed-case strings are fully converted to lowercase.
        - Ensures that numeric strings are unaffected by the transformation.
        """
        self.assertEqual(to_lowercase("HELLO"), "hello")
        self.assertEqual(to_lowercase("Hello World!"), "hello world!")
        self.assertEqual(to_lowercase("1234"), "1234")  # Test with numbers


# INTEGRATION TESTING
class TestAppIntegration(unittest.TestCase):
    """
    Integration tests for the main function, which combines multiple components (input, 
    output, and transformation functions) to verify correct behavior for different choices.
    """

    @patch("builtins.input", side_effect=["1", "hello world"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_main_uppercase(self, mock_stdout, mock_input):
        """
        Integration test for the uppercase option (option 1):
        
        - Simulates user input for option 1 with a lowercase string.
        - Verifies that the output shows the correct uppercase transformation.
        """
        main()
        self.assertIn("Text în majuscule: HELLO WORLD", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["2", "HELLO WORLD"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_main_lowercase(self, mock_stdout, mock_input):
        """
        Integration test for the lowercase option (option 2):
        
        - Simulates user input for option 2 with an uppercase string.
        - Verifies that the output shows the correct lowercase transformation.
        """
        main()
        self.assertIn("Text în litere mici: hello world", mock_stdout.getvalue())


# FUNCTIONAL TESTING
class TestAppFunctional(unittest.TestCase):
    """
    Functional tests to validate the end-to-end behavior of the application’s main features, 
    simulating user input and checking program output for different scenarios.
    """

    @patch("builtins.input", side_effect=["1", "Test Functional"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_functional_uppercase(self, mock_stdout, mock_input):
        """
        Functional test for the uppercase option (option 1):
        
        - Simulates a full test for the uppercase option, verifying that the program correctly
          converts the input text to uppercase and outputs it.
        """
        main()
        self.assertIn("Text în majuscule: TEST FUNCTIONAL", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["2", "Test Functional"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_functional_lowercase(self, mock_stdout, mock_input):
        """
        Functional test for the lowercase option (option 2):
        
        - Simulates a full test for the lowercase option, verifying that the program correctly
          converts the input text to lowercase and outputs it.
        """
        main()
        self.assertIn("Text în litere mici: test functional", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["3", ""])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_functional_invalid_option(self, mock_stdout, mock_input):
        """
        Functional test for an invalid option (option 3):
        
        - Simulates user input for an invalid option, verifying that the program responds
          with an appropriate error message.
        """
        main()
        self.assertIn("Opțiune invalidă.", mock_stdout.getvalue())


# Run all tests
if __name__ == "__main__":
    unittest.main()
