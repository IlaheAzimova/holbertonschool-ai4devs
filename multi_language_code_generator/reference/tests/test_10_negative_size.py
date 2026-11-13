
import unittest
from log_analyzer import LogAnalyzer

class TestNegativeSize(unittest.TestCase):
    def test_negative_size(self):
        log = '192.168.1.10 - - [13/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 -1'
        result = LogAnalyzer().analyze([log])
        self.assertEqual(result["malformed_entries"], 1)
        self.assertEqual(result["total_requests"], 0)

if __name__ == "__main__":
    unittest.main()
