Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 10
>>> result = "Even" if num % 2 == 0 else "Odd"
>>> print(f"The number {num} is {result}.")
The number 10 is Even.
>>> print(f"The number {num} is {result}.")
The number 10 is Even.
>>> num = 13
>>> result = "Even" if num % 2 == 0 else "Odd"print(f"The number {num} is {result}.")
SyntaxError: invalid syntax
>>> num = 13
>>> print(f"The number {num} is {result}.")
The number 13 is Even.
>>> print(f"The number {num} is {result}.")
The number 13 is Even.
>>> 