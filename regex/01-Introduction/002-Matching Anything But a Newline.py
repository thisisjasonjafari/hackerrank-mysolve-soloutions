import sys
import re
regex_pattern = r"...\....\....\....$"  # Do not delete 'r'.


test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())
