
"""Unit tests for the code review simulator."""

import unittest

from code_review import (
    format_review_report,
    review_python_code,
    summarize_findings,
)


class TestCodeReview(unittest.TestCase):
    def test_empty_source(self):
        findings = review_python_code("")
        self.assertEqual(findings[0]["severity"], "INFO")
        self.assertIn("empty", findings[0]["message"].lower())

    def test_syntax_error(self):
        findings = review_python_code("def broken(:")
        self.assertEqual(findings[0]["severity"], "ERROR")

    def test_long_line_warning(self):
        source = "value = '" + ("x" * 100) + "'"
        findings = review_python_code(source)
        self.assertTrue(
            any("88 characters" in item["message"] for item in findings)
        )

    def test_print_info(self):
        findings = review_python_code("print('debug')")
        self.assertTrue(
            any("logging" in item["message"] for item in findings)
        )

    def test_bare_except_warning(self):
        source = "try:\n    run()\nexcept:\n    pass"
        findings = review_python_code(source)
        self.assertTrue(
            any("Bare except" in item["message"] for item in findings)
        )

    def test_missing_docstring(self):
        findings = review_python_code("def calculate_total():\n    return 1")
        self.assertTrue(
            any("no docstring" in item["message"] for item in findings)
        )

    def test_short_function_name(self):
        findings = review_python_code("def go():\n    pass")
        self.assertTrue(
            any("too short" in item["message"] for item in findings)
        )

    def test_summary_counts(self):
        findings = [
            {"severity": "ERROR", "message": "Error"},
            {"severity": "WARNING", "message": "Warning"},
            {"severity": "INFO", "message": "Info"},
            {"severity": "INFO", "message": "Another info"},
        ]
        self.assertEqual(
            summarize_findings(findings),
            {"ERROR": 1, "WARNING": 1, "INFO": 2},
        )

    def test_report_format(self):
        findings = [{"severity": "WARNING", "line": 3, "message": "Example"}]
        report = format_review_report(findings)
        self.assertIn("Code Review Report", report)
        self.assertIn("Warnings: 1", report)
        self.assertIn("(line 3)", report)

    def test_clean_code(self):
        findings = review_python_code(
            'def calculate_total():\n    """Calculate a total."""\n'
            "    return 10\n"
        )
        self.assertTrue(
            any("No issues detected" in item["message"] for item in findings)
        )


if __name__ == "__main__":
    unittest.main()
