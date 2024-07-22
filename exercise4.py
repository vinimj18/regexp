'''
Exercise 4: Password Strength Checker
Write a Python function that checks if a given password is strong. 
A strong password for this exercise:

Is at least 8 characters long.
Contains at least one uppercase letter, one lowercase letter, one digit, 
and one special character (e.g., !@#$%^&*()).

Example Input:
"StrongPass1!"

Expected Output:
True
'''
import re

regexp = re.compile(
    r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*()])(?!.*[\s]).{8,}$'
)


def is_strong_password(password):
    return bool(re.match(regexp, password))


password1 = 'StrongPass1!'
password2 = 'strongpass!'

print(is_strong_password(password1))
print(is_strong_password(password2))
