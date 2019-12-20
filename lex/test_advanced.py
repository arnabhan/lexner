import sys
import os
import unittest
from lexner import get_named_entities, get_processed_text

class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_cases(self):
        test_cases = []
        error=False
        with open(os.path.dirname(__file__) + '/tok_test.txt', 'r', encoding='utf-8') as tcases:
            test_cases = tcases.readlines()
        for i in range(0, len(test_cases), 2):
            text = test_cases[i].strip()
            expected = test_cases[i+1].strip()
            annotations = get_named_entities(text)
            processed_text = get_processed_text(annotations)
            if processed_text.strip() != expected.strip():
                error = True
                print("Actual:\n" + processed_text)
                print("Expected:\n" + expected)
        self.assertFalse(error)

if __name__ == '__main__':
    unittest.main()
