# Cross-Language Specification — Log Analyzer

## 1. Objective

Define a language-independent algorithm that analyzes web server log entries and calculates request statistics. The specification will be used to implement and test the same algorithm in multiple programming languages.

## 2. Algorithm Description

The Log Analyzer processes structured web server log entries and calculates:

- Total number of valid requests.
- Number of successful requests (HTTP status codes 200–299).
- Number of client errors (HTTP status codes 400–499).
- Number of server errors (HTTP status codes 500–599).
- Number of unique visitors based on IP addresses.
- Error rate as a percentage of valid requests with status codes 400–599.

Malformed entries must be excluded from all statistics and counted separately.

## 3. Input Format

The algorithm accepts a list of log entries in the following format:

`IP_ADDRESS - - [TIMESTAMP] "METHOD PATH PROTOCOL" STATUS_CODE SIZE`

Example:

```text
192.168.1.10 - - [13/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 1024
192.168.1.11 - - [13/Nov/2026:10:01:00 +0000] "POST /login HTTP/1.1" 401 512
192.168.1.10 - - [13/Nov/2026:10:02:00 +0000] "GET /api HTTP/1.1" 500 256
```

### Input Rules

- Each valid entry must contain an IP address, HTTP method, path, protocol, status code, and response size.
- Status codes must be integers between 100 and 599.
- Response size must be a non-negative integer.
- Empty input is allowed.
- Invalid or malformed entries must not stop the analysis of subsequent entries.

## 4. Output Format

The algorithm returns a JSON-compatible object with the following fields:

```json
{
  "total_requests": 3,
  "successful_requests": 1,
  "client_errors": 1,
  "server_errors": 1,
  "unique_visitors": 2,
  "error_rate": 66.67,
  "malformed_entries": 0
}
```

### Output Rules

- `total_requests` counts all valid entries.
- `successful_requests` counts status codes from 200 to 299.
- `client_errors` counts status codes from 400 to 499.
- `server_errors` counts status codes from 500 to 599.
- `unique_visitors` counts distinct IP addresses among valid entries.
- `error_rate` is the percentage of valid requests with status codes from 400 to 599, rounded to two decimal places.
- `malformed_entries` counts entries rejected by validation.
- If there are no valid requests, `error_rate` must be `0.0`.

## 5. Edge Cases

1. Empty input list.
2. Input containing only malformed entries.
3. Multiple requests from the same IP address.
4. Requests with status codes 200, 301, 404, and 503.
5. Missing or invalid status codes.
6. Negative response sizes.
7. A mixture of valid and malformed entries.
8. A valid request list with no errors.
9. Requests containing paths with spaces encoded according to the log format.
10. A single valid request with an error status code.

## 6. Test Cases

### Test Case 1 — Normal Input

**Input:** Three valid requests with status codes 200, 401, and 500. Two distinct IP addresses.

**Expected Output:**

```json
{
  "total_requests": 3,
  "successful_requests": 1,
  "client_errors": 1,
  "server_errors": 1,
  "unique_visitors": 2,
  "error_rate": 66.67,
  "malformed_entries": 0
}
```

### Test Case 2 — Empty Input

**Input:** An empty list.

**Expected Output:**

```json
{
  "total_requests": 0,
  "successful_requests": 0,
  "client_errors": 0,
  "server_errors": 0,
  "unique_visitors": 0,
  "error_rate": 0.0,
  "malformed_entries": 0
}
```

### Test Case 3 — Repeated Visitors

**Input:** Three valid requests from the same IP address, with status codes 200, 200, and 204.

**Expected Output:**

```json
{
  "total_requests": 3,
  "successful_requests": 3,
  "client_errors": 0,
  "server_errors": 0,
  "unique_visitors": 1,
  "error_rate": 0.0,
  "malformed_entries": 0
}
```

### Test Case 4 — Client and Server Errors

**Input:** Four valid requests with status codes 200, 301, 404, and 503.

**Expected Output:**

```json
{
  "total_requests": 4,
  "successful_requests": 1,
  "client_errors": 1,
  "server_errors": 1,
  "unique_visitors": 4,
  "error_rate": 50.0,
  "malformed_entries": 0
}
```

### Test Case 5 — Malformed Entries

**Input:** Two valid requests and two malformed entries, one with a missing status code and one with a negative response size. The valid requests have status codes 200 and 404 and come from different IP addresses.

**Expected Output:**

```json
{
  "total_requests": 2,
  "successful_requests": 1,
  "client_errors": 1,
  "server_errors": 0,
  "unique_visitors": 2,
  "error_rate": 50.0,
  "malformed_entries": 2
}
```

### Test Case 6 — All Entries Malformed

**Input:** Three malformed log entries.

**Expected Output:**

```json
{
  "total_requests": 0,
  "successful_requests": 0,
  "client_errors": 0,
  "server_errors": 0,
  "unique_visitors": 0,
  "error_rate": 0.0,
  "malformed_entries": 3
}
```

### Test Case 7 — Single Server Error

**Input:** One valid request with status code 503.

**Expected Output:**

```json
{
  "total_requests": 1,
  "successful_requests": 0,
  "client_errors": 0,
  "server_errors": 1,
  "unique_visitors": 1,
  "error_rate": 100.0,
  "malformed_entries": 0
}
```

## 7. Cross-Language Requirements

All implementations must:

- Follow the same input and output specifications.
- Apply identical validation rules.
- Produce equivalent results for every test case.
- Use the same status code classifications.
- Calculate the error rate using the same formula and rounding rule.
- Continue processing valid entries when malformed entries are encountered.

## 8. Error Rate Formula

`error_rate = (client_errors + server_errors) / total_requests * 100`

If `total_requests` is zero, return `0.0`.

## 9. Acceptance Criteria

- All seven test cases produce the expected results.
- Malformed entries are counted and excluded from statistics.
- Duplicate IP addresses count as one unique visitor.
- Error rate is rounded to two decimal places.
- The specification is independent of any particular programming language.
- Implementations can be compared using the same test data.
