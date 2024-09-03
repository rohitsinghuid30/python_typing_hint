from datetime import datetime
from typing import AnyStr

# on functions
def print_list(a: list) -> None:
    print(a)

# run this command -> mypy app.py -> following output has found.
print_list([1,2,3])
# print_list("1") # output - app.py:9: error: Argument 1 to "print_list" has incompatible type "str"; expected "list[Any]"  [arg-type]
# print_list(1) # output - app.py:10: error: Argument 1 to "print_list" has incompatible type "int"; expected "list[Any]"  [arg-type]


# on function -return - int
def myfunc(x: int) -> None:
    print(x)

# myfunc("1") # output : app.py:17: error: Argument 1 to "myfunc" has incompatible type "str"; expected "int"  [arg-type]
myfunc(1)


# on function - return - str
def myfunc2(b: str) -> None:
    print(b)

# myfunc2(1)
myfunc2("1")


# on function - return - str 2
def myfunction(myparameter: int)-> str:
    return f"{myparameter} is correct parameter"

print(myfunction(12))


# other fucntion
def otherfucntion(myparam:int) -> str:
    return f"{myparam}"


print(otherfucntion(2))


# datetime datatype
def mydate(param:datetime)->str:
    return f"Current datetime is {param}"


print(mydate(datetime.now()))

# Return int -> int and sum
def add(x:int)->int:
    return x + 10

print(add(10))


# return int and return str functions




