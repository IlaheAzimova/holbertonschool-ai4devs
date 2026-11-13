
import unittest
from log_analyzer import LogAnalyzer

class TestServerError(unittest.TestCase):
    def test_server_error(self):
        log = '192.168.1.10 - - [13/Nov/2026:10:00:00 +0000] "GET /api HTTP/1.1" 503 100'
        result = LogAnalyzer().analyze([log])
        self.assertEqual(result["server_errors"], 1)
        self.assertEqual(result["error_rate"], 100.0)

if __name__ == "__main__":
    unittest.main()
