
import unittest
from log_analyzer import LogAnalyzer

class TestMixedEntries(unittest.TestCase):
    def test_mixed_entries(self):
        logs = [
            '192.168.1.10 - - [13/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 100',
            'invalid entry',
            '192.168.1.11 - - [13/Nov/2026:10:01:00 +0000] "GET /missing HTTP/1.1" 404 100',
            '',
        ]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result["total_requests"], 2)
        self.assertEqual(result["malformed_entries"], 2)
        self.assertEqual(result["unique_visitors"], 2)
        self.assertEqual(result["error_rate"], 50.0)

if __name__ == "__main__":
    unittest.main()
