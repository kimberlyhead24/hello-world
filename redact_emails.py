import re
def redact_emails(emails):
  pattern = r"([\w.%+-]+)@([\w.-]+)"
  replacement = r"[REDACTED]"
  new_emails = [re.sub(pattern, replacement, email) for email in emails]
  return new_emails

emails1 = [
    "contact me at alice@example.com",
    "bob.smith+test@sub.domain.org is another",
]
redact_emails(emails1)
