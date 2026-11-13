
import unittest
from log_analyzer import LogAnalyzer

class TestRedirect(unittest.TestCase):
    def test_redirect_is_not_error(self):
        log = '192.168.1.10 - - [13/Nov/2026:10:00:00 +0000] "GET /old HTTP/1.1" 301 100'
        result = LogAnalyzer().analyze([log])
        self.assertEqual(result["total_requests"], 1)
        self.assertEqual(result["error_rate"], 0.0)

if __name__ == "__main__":
    unittest.main()
