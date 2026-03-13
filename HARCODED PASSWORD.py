rules:
  - id: detect-hardcoded-password
    languages: [python, javascript, go, java]
    message: "Se detectó una posible contraseña grabada en el código (hardcoded). Esto es una mala práctica de seguridad."
    severity: WARNING
    patterns:
      - pattern-either:
          - pattern: $VAR = "..."
          - pattern: $VAR = '...'
      - metavariable-regex:
          metavariable: $VAR
          regex: (?i)^(password|passwd|secret|api_key|token|pwd)$
      - pattern-not: $VAR = ""