rules:
- id: hardcoded-password
  patterns:
    - pattern: $VAR = "..."
    - metavariable-regex:
        metavariable: $VAR
        regex: (?i)(password|passwd|pwd|secret|token|api_key)
  message: Hardcoded credential detected
  languages: [python]
  severity: WARNING



