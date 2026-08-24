'''
Concepts Covered: Equality (`==`) and Inequality (`!=`), Case-Insensitive String Testing via `.lower()`, Numerical Comparisons (`>`, `<`, `>=`, `<=`), Compound Logical Conditions (`and`, `or`), Boolean Values (`True`, `False`), and PEP 8 Comparison Formatting.

Task: Build an authentication and parameter validator that enforces strict access criteria.
'''

#variables for login attempt
submitted_username = "   sYSteM_aDmIn "
access_clearance_level = 7

#database match variable
stored_username = "system_admin"

#condition for granting access
if stored_username == submitted_username.lower().rstrip().lstrip() and access_clearance_level >= 5:
    print("Access authorized")

#more variables for checking condition
failed_attempts = 2
account_locked = True

if failed_attempts > 3 or account_locked:
    print("Security lockout triggered")