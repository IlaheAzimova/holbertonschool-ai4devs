
import ipaddress
import re
from typing import Any


class LogAnalyzer:
    """Analyze Apache-style access logs and calculate request statistics."""

    LOG_PATTERN = re.compile(
        r'^(\S+)\s+-\s+-\s+\[([^\]]+)\]\s+'
        r'"(\S+)\s+(.+?)\s+(\S+)"\s+(\d{3})\s+(\d+)$'
    )

    def parse_line(self, line: str) -> dict[str, Any]:
        """Parse and validate a single log entry."""
        if not isinstance(line, str):
            raise ValueError("Log entry must be a string")

        match = self.LOG_PATTERN.fullmatch(line.strip())
        if not match:
            raise ValueError("Malformed log entry")

        ip, timestamp, method, path, protocol, status, size = (
            match.groups()
        )

        try:
            ipaddress.ip_address(ip)
        except ValueError as exc:
            raise ValueError("Invalid IP address") from exc

        if not timestamp.strip():
            raise ValueError("Timestamp cannot be empty")

        if not method or not path or not protocol:
            raise ValueError("Invalid request information")

        status_code = int(status)
        response_size = int(size)

        if not 100 <= status_code <= 599:
            raise ValueError("Status code must be between 100 and 599")

        if response_size < 0:
            raise ValueError("Response size cannot be negative")

        return {
            "ip": ip,
            "timestamp": timestamp,
            "method": method,
            "path": path,
            "protocol": protocol,
            "status": status_code,
            "size": response_size,
        }

    def analyze(self, lines: list[str]) -> dict[str, Any]:
        """Analyze log entries and return aggregate statistics."""
        if not isinstance(lines, list):
            raise ValueError("Input must be a list of log entries")

        total_requests = 0
        successful_requests = 0
        client_errors = 0
        server_errors = 0
        malformed_entries = 0
        visitors = set()

        for line in lines:
            try:
                entry = self.parse_line(line)
            except ValueError:
                malformed_entries += 1
                continue

            total_requests += 1
            visitors.add(entry["ip"])
            status = entry["status"]

            if 200 <= status <= 299:
                successful_requests += 1
            elif 400 <= status <= 499:
                client_errors += 1
            elif 500 <= status <= 599:
                server_errors += 1

        if total_requests == 0:
            error_rate = 0.0
        else:
            error_rate = round(
                (client_errors + server_errors)
                / total_requests * 100,
                2,
            )

        return {
            "total_requests": total_requests,
            "successful_requests": successful_requests,
            "client_errors": client_errors,
            "server_errors": server_errors,
            "unique_visitors": len(visitors),
            "error_rate": error_rate,
            "malformed_entries": malformed_entries,
        }
