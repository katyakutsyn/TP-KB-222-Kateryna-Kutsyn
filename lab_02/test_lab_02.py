import unittest
import io
import os
import csv
from unittest.mock import patch
from lab_02 import load_data, save_data, add_new_element, delete_element, update_element, print_all_list

class TestLab2Script(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_lab2.csv"
        self.test_data = [
            {"name": "John", "phone": "9675643454", "age": "21", "email": "john@example.com"},
            {"name": "Alice", "phone": "734586290", "age": "19", "email": "alice@example.com"},
        ]

    def tearDown(self):
        # Clean up the test file after each test
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass

    def test_load_data(self):
        with open(self.test_file, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "phone", "age", "email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.test_data)

        loaded_data = load_data(self.test_file)
        self.assertEqual(loaded_data, self.test_data)

    def test_save_data(self):
        save_data(self.test_file, self.test_data)
        loaded_data = load_data(self.test_file)
        self.assertEqual(loaded_data, self.test_data)

    def test_add_new_element(self):
        with patch('builtins.input', side_effect=["Bob", "5555555555", "30", "bob@example.com"]):
            add_new_element(self.test_data)
            self.assertEqual(len(self.test_data), 3)

    def test_delete_element(self):
        with patch('builtins.input', return_value="John"):
            delete_element(self.test_data)
            self.assertEqual(len(self.test_data), 1)

    def test_update_element(self):
        with patch('builtins.input', side_effect=["Alice", "Bob", "5555555555", "30", "bob@example.com"]):
            update_element(self.test_data)
            self.assertEqual(self.test_data[0]["name"], "Bob")

    def test_print_all_list(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print_all_list(self.test_data)
            output = mock_stdout.getvalue()
            self.assertIn("John", output)
            self.assertIn("Alice", output)

if __name__ == '__main__':
    unittest.main()
