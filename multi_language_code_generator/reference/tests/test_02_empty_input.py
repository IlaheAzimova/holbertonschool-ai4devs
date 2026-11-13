
import unittest
from log_analyzer import LogAnalyzer

class TestEmptyInput(unittest.TestCase):
    def test_empty_input(self):
        result = LogAnalyzer().analyze([])
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["unique_visitors"], 0)
        self.assertEqual(result["error_rate"], 0.0)

if __name__ == "__main__":
    unittest.main()
