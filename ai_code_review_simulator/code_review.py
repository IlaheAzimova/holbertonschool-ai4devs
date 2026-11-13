
"""A lightweight static code review simulator."""

import ast
import re


def review_python_code(source_code):
    """Return a list of potential issues found in Python source code."""
    if not isinstance(source_code, str):
        raise TypeError("source_code must be a string")

    findings = []

    if not source_code.strip():
        return [{"severity": "INFO", "message": "Source code is empty."}]

    try:
        tree = ast.parse(source_code)
    except SyntaxError as error:
        return [{
            "severity": "ERROR",
            "message": f"Syntax error on line {error.lineno}: {error.msg}",
        }]

    lines = source_code.splitlines()

    for number, line in enumerate(lines, start=1):
        if len(line) > 88:
            findings.append({
                "severity": "WARNING",
                "line": number,
                "message": "Line exceeds 88 characters.",
            })

        if re.search(r"\bprint\s*\(", line):
            findings.append({
                "severity": "INFO",
                "line": number,
                "message": "Consider replacing debug print with logging.",
            })

        if re.search(r"\bexcept\s*:", line):
            findings.append({
                "severity": "WARNING",
                "line": number,
                "message": "Bare except catches all exceptions.",
            })

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if len(node.name) < 3:
                findings.append({
                    "severity": "WARNING",
                    "line": node.lineno,
                    "message": f"Function name '{node.name}' is too short.",
                })

            if ast.get_docstring(node) is None:
                findings.append({
                    "severity": "INFO",
                    "line": node.lineno,
                    "message": f"Function '{node.name}' has no docstring.",
                })

        if isinstance(node, ast.ExceptHandler) and node.type is None:
            # The bare-except warning is reported by the line-based check.
            pass

    if not findings:
        findings.append({
            "severity": "INFO",
            "message": "No issues detected by the basic review checks.",
        })

    return findings


def summarize_findings(findings):
    """Count findings by severity."""
    summary = {"ERROR": 0, "WARNING": 0, "INFO": 0}

    for finding in findings:
        severity = finding.get("severity", "INFO")
        if severity in summary:
            summary[severity] += 1

    return summary


def format_review_report(findings):
    """Format findings into a readable text report."""
    summary = summarize_findings(findings)
    report = [
        "Code Review Report",
        "==================",
        f"Errors: {summary['ERROR']}",
        f"Warnings: {summary['WARNING']}",
        f"Info: {summary['INFO']}",
        "",
    ]

    for finding in findings:
        line = finding.get("line")
        location = f" (line {line})" if line is not None else ""
        report.append(
            f"[{finding['severity']}]{location} {finding['message']}"
        )

    return "\n".join(report)
