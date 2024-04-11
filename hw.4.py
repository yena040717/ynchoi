Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def rep_char(c, n):
...     return c * n
... 
>>> def welcome_message(name):
...     msg1 = f"Hello, {name},"
...     msg2 = "Welcome to Seoul."
...     nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
...     border = rep_char("*", nstr + 4)
...     print(border)
...     print("  " + msg1)
...     print("  " + msg2)
...     print(border)
... 
...     
