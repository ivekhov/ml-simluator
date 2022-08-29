import re
from typing import List


def valid_emails(strings: List[str]) -> List[str]:
    """Take list of potential emails and returns only valid ones"""
    valid_email_regex = "^[\w+_.-]+@[\w.-]+$"
    compiled_regex = re.compile(valid_email_regex, re.IGNORECASE)

    emails = []
    for email in strings:
        re_result = compiled_regex.fullmatch(email)
        if re_result:
            emails.append(re_result.string)

    return emails
