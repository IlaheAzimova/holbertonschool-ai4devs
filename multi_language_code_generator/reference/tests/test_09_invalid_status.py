
import unittest
from log_analyzer import LogAnalyzer

class TestInvalidStatus(unittest.TestCase):
    def test_status_below_range(self):
        log = '192.168.1.10 - - [13/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 099 100'
        result = LogAnalyzer().analyze([log])
        self.assertEqual(result["malformed_entries"], 1)

    def test_status_above_range(self):
        log = '192.168.1.10 - - [13/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 600 100'
        result = LogAnalyzer().analyze([log])
        self.assertEqual(result["malformed_entries"], 1)

if __name__ == "__main__":
    unittest.main()
