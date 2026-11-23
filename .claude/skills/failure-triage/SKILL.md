# Failure Triage and Bug Report Skill
## Activation
Use when pytest output, stack traces, Allure results, or a failing test is supplied.
## Inputs
Failure log, test name, environment details, and steps if available.
## Procedure
1. Extract failure, stack trace, assertion, timestamps, and environment.
2. Classify likely cause: product defect, test-code defect, or environment/flaky issue.
3. Separate evidence from hypotheses; suggest minimal reproduction and next checks.
4. Draft a Jira-style report; do not claim unverified root cause.
## Output
Classification and confidence; evidence; Summary; Steps to Reproduce; Actual Result; Expected Result; Severity; Priority; suggested next action.
