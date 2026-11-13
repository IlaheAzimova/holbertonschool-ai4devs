
import unittest
from log_analyzer import LogAnalyzer

class TestRepeatedIP(unittest.TestCase):
    def test_repeated_ip(self):
        logs = [
            '192.168.1.10 - - [13/Nov/2026:10:00:00 +0000] "GET /a HTTP/1.1" 200 100',
            '192.168.1.10 - - [13/Nov/2026:10:01:00 +0000] "GET /b HTTP/1.1" 204 100',
        ]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result["unique_visitors"], 1)
        self.assertEqual(result["total_requests"], 2)

if __name__ == "__main__":
    unittest.main()
