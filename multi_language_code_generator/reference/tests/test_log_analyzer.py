
import unittest

from log_analyzer import LogAnalyzer


def make_log(ip="192.168.1.10", status=200, size=100):
    return (
        f'{ip} - - [13/Nov/2026:10:00:00 +0000] '
        f'"GET /home HTTP/1.1" {status} {size}'
    )


class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_valid_entry(self):
        result = self.analyzer.analyze([make_log()])
        self.assertEqual(result["total_requests"], 1)
        self.assertEqual(result["successful_requests"], 1)

    def test_empty_input(self):
        result = self.analyzer.analyze([])
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["error_rate"], 0.0)

    def test_repeated_ip(self):
        result = self.analyzer.analyze([
            make_log(status=200),
            make_log(status=204),
        ])
        self.assertEqual(result["unique_visitors"], 1)

    def test_client_error(self):
        result = self.analyzer.analyze([make_log(status=404)])
        self.assertEqual(result["client_errors"], 1)
        self.assertEqual(result["error_rate"], 100.0)

    def test_server_error(self):
        result = self.analyzer.analyze([make_log(status=503)])
        self.assertEqual(result["server_errors"], 1)

    def test_redirect_is_not_error(self):
        result = self.analyzer.analyze([make_log(status=301)])
        self.assertEqual(result["error_rate"], 0.0)
        self.assertEqual(result["total_requests"], 1)

    def test_malformed_line(self):
        result = self.analyzer.analyze(["this is not a log"])
        self.assertEqual(result["malformed_entries"], 1)
        self.assertEqual(result["total_requests"], 0)

    def test_invalid_ip(self):
        result = self.analyzer.analyze([make_log(ip="invalid-ip")])
        self.assertEqual(result["malformed_entries"], 1)

    def test_invalid_status_below_range(self):
        result = self.analyzer.analyze([make_log(status=99)])
        self.assertEqual(result["malformed_entries"], 1)

    def test_invalid_status_above_range(self):
        result = self.analyzer.analyze([make_log(status=600)])
        self.assertEqual(result["malformed_entries"], 1)

    def test_negative_size(self):
        line = make_log().rsplit(" ", 1)[0] + " -1"
        result = self.analyzer.analyze([line])
        self.assertEqual(result["malformed_entries"], 1)

    def test_mixed_valid_and_invalid(self):
        result = self.analyzer.analyze([
            make_log(status=200),
            "invalid entry",
            make_log(ip="192.168.1.11", status=404),
            "",
        ])
        self.assertEqual(result["total_requests"], 2)
        self.assertEqual(result["malformed_entries"], 2)
        self.assertEqual(result["unique_visitors"], 2)
        self.assertEqual(result["error_rate"], 50.0)

    def test_all_entries_malformed(self):
        result = self.analyzer.analyze(["bad", "", "also bad"])
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["malformed_entries"], 3)
        self.assertEqual(result["error_rate"], 0.0)

    def test_successful_status_range(self):
        result = self.analyzer.analyze([
            make_log(status=200),
            make_log(status=201),
            make_log(status=299),
        ])
        self.assertEqual(result["successful_requests"], 3)

    def test_error_rate_rounding(self):
        result = self.analyzer.analyze([
            make_log(status=404),
            make_log(ip="192.168.1.11", status=200),
            make_log(ip="192.168.1.12", status=200),
        ])
        self.assertEqual(result["error_rate"], 33.33)


if __name__ == "__main__":
    unittest.main()
