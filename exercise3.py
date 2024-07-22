'''Exercise 3: URL Validation
Write a Python function to validate if a given string is a valid URL. A valid URL for this exercise:

Starts with http:// or https://.
Followed by one or more alphanumeric characters or dots.
Optionally includes a port number, path, query, and fragment.

Example Input:
"https://www.example.com/path?query=1#fragment"

Expected Output:
True
'''
import re

text = 'https://www.example.com/path?query=1#fragment'
pattern = r'^http[s]?://\w{3}.?\w+.\w+/(\w+)?(?:\?query=\d+)?(?:#\w+)?'


def validate_link(string):
    return bool(re.match(pattern, string))


print(validate_link(text))
