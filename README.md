# Python Typing Hint
Introduced since Python 3.5, Python’s typing module attempts to provide a way of hinting types to help static type checkers and linters accurately predict errors.

Due to Python having to determine the type of objects during run-time, it sometimes gets very hard for developers to find out what exactly is going on in the code.

Even external type checkers like PyCharm IDE do not produce the best results; on average only predicting errors correctly about 50% of the time, according to this answer on StackOverflow.OAO.
