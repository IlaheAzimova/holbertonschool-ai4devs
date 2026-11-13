
import unittest
from log_analyzer import LogAnalyzer

class TestMalformedLine(unittest.TestCase):
    def test_malformed_line(self):
        result = LogAnalyzer().analyze(["this is not a valid log"])
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["malformed_entries"], 1)

if __name__ == "__main__":
    unittest.main()
