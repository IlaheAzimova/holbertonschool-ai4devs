
import unittest
from log_analyzer import LogAnalyzer

class TestInvalidIP(unittest.TestCase):
    def test_invalid_ip(self):
        log = 'invalid-ip - - [13/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 100'
        result = LogAnalyzer().analyze([log])
        self.assertEqual(result["malformed_entries"], 1)
        self.assertEqual(result["total_requests"], 0)

if __name__ == "__main__":
    unittest.main()
