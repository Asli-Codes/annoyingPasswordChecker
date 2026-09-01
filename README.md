# Annoying Password Checker 🔐

A playful password validation project built with Python and Streamlit.

Instead of showing all password errors at once, the app reveals the rules one by one.  
Every time the user fixes one problem, another rule appears.

Basically: **your password is never good enough. :)**

---

## Features

The password checker includes rules such as:

- Minimum 10 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character
- No repeated patterns like `sifresifre`
- No common words such as `password`, `admin` or `qwerty`
- No simple sequences like `123` or `abc`
- No three identical characters in a row
- Password cannot start with a number
- Password cannot end with a special character
- The sum of the digits must be greater than 10
- At least two different special characters
- First and last characters cannot be the same
- And a few more unnecessarily annoying rules :)

---

## How It Works

The project is separated into two main parts:

### `app.py`

Handles the Streamlit interface.

It takes the password entered by the user, sends it to the validator and displays the result.

### `passwordValidator.py`

Contains the password validation logic.

Each function has a small responsibility, such as:

```python
hasUppercase(password)
hasDigit(password)
hasRepeatedPattern(password)
