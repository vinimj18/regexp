'''Exercise 2: Phone Number Extraction
Write a Python function that extracts and returns all phone numbers from a given text. 
Assume phone numbers are in the format (123) 456-7890 or 123-456-7890.

Example Input:
"Call me at (123) 456-7890 or 987-654-3210."

Expected Output:
["(123) 456-7890", "987-654-3210"]'''
import re

text = 'Call me at (123) 456-7890 or 987-654-3210.'


def find_phones(string):
    pattern = r'\(?\d{3}(?:\)\s)?-?\d{3}-\d{4}'
    return re.findall(pattern, string)


print(find_phones(text))
