
import unittest
from log_analyzer import LogAnalyzer

class TestClientError(unittest.TestCase):
    def test_client_error(self):
        log = '192.168.1.10 - - [13/Nov/2026:10:00:00 +0000] "GET /missing HTTP/1.1" 404 100'
        result = LogAnalyzer().analyze([log])
        self.assertEqual(result["client_errors"], 1)
        self.assertEqual(result["error_rate"], 100.0)

if __name__ == "__main__":
    unittest.main()
