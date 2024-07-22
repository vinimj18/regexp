'''
Exercise 5: Date Extraction
Write a Python function that extracts all dates from a given text. Dates should be in the format DD/MM/YYYY or DD-MM-YYYY.

Example Input:
"Important dates are 12/04/2021 and 25-12-2022."

Expected Output:
["12/04/2021", "25-12-2022"]
'''
import re

text = 'Important dates are 12/04/2021 and 25-12-2022.'
date_regex = re.compile(r'\d{2}[-/]\d{2}[-/]\d{4}')


def extract_dates(text):
    return re.findall(date_regex, text)


print(extract_dates(text))
