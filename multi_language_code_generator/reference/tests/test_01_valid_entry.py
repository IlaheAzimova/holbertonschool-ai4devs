
import unittest
from log_analyzer import LogAnalyzer

class TestValidEntry(unittest.TestCase):
    def test_valid_entry(self):
        log = '192.168.1.10 - - [13/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 100'
        result = LogAnalyzer().analyze([log])
        self.assertEqual(result["total_requests"], 1)
        self.assertEqual(result["successful_requests"], 1)
        self.assertEqual(result["malformed_entries"], 0)

if __name__ == "__main__":
    unittest.main()
