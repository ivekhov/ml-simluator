import random
import string
import re
import time
from typing import List


# valid_email_regex = "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
# def is_valid_email(email: str) -> bool:
#     """."""
#     return bool(re.fullmatch(valid_email_regex, email))


def random_char(char_num) -> str:
    """Generate random chars with length given."""
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


def generate_email(length: int, domain: str="@gmail.com") -> str:
    """Generate random gmail email."""
    return str(random_char(length)+domain)


def generate_emails(length: int, count: int) -> List[str]:
    """Generate test data."""
    result = []
    for _ in range(count):
        result.append(generate_email(length))
    for _ in range(count):
        result.append(generate_email(length, "rambler"))

    return result


def valid_emails(strings: List[str]) -> List[str]:
    """Take list of potential emails and returns only valid ones"""

    # valid_email_regex = "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
    
    # solution
    valid_email_regex = "^[\w+_.-]+@[\w.-]+$"
    compiled_regex = re.compile(valid_email_regex, re.IGNORECASE)


    def is_valid_email(email: str) -> bool:
        # return bool(re.fullmatch(valid_email_regex, email))
        # return bool(re.findall(valid_email_regex, email))

        # solution
        return bool(compiled_regex.fullmatch(email))


    emails = []
    for email in strings:
        # if is_valid_email(email):
        #     emails.append(email)
        
        # solution #1
        if len(email) > 0:

            re_result = compiled_regex.fullmatch(email)
            if re_result:
                emails.append(re_result.string)

        # re_result = compiled_regex.findall(email)
        # if re_result:
        #     emails.append(re_result)

    return emails




def main():
    """Main function."""
    count = 1_000_000
    length = 7
    tests = generate_emails(length, count)
    # print(tests)
    start = time.time()
    print()
    result = valid_emails(tests)
    end = time.time()
    print()

    # print(result)
    
    print()
    print(end - start)


if __name__ == "__main__":
    main()


# results
# 2 mln = 2.3-2.4 --> 2.0 --> 1.25 --> 1.17 - 1.19

# strings = ['zPSmmqM@gmail.com', 'UOTaYxl@gmail.com', 'ayxENEB@gmail.com', 'AcXTABw@gmail.com', 'OotevBH@gmail.com', 'bqndBUl@gmail.com', 'uAZfVZw@gmail.com', 'zjpPxXB@gmail.com', 'wtzRFxS@gmail.com', 'ukZMpJn@gmail.com', 'bulWDRprambler', 'fAjdYQorambler', 'fDwiVJhrambler', 'YoWyFdqrambler', 'XmAAusIrambler', 'HplOSeWrambler', 'GYHBftUrambler', 'hPRJiShrambler', 'jIYrsMOrambler', 'dRCQQRPrambler']
