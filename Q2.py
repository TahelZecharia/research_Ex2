
def lastcall(func):
    """
    This decorator checks whether the current input used before.
    If not - it runs the function as usual. If so - it does not run the function, but writes an appropriate message.

    1) The function f1 accepts an int and returns an int:
     >>> f1(4) # first call of f1 with 4
     16
     >>> f1(4) # second call of f1 with 4
     I already told you that the answer is 16!
     >>> f1(91) # first call of f1 with 91
     8281
     >>> f1(4) # third call of f1 with 4
     I already told you that the answer is 16!
     >>> f1(91) # second call of f1 with 4
     I already told you that the answer is 8281!

     2) The function f2 accepts a str and returns str.upper():
     >>> f2("hello") # first call of f2 with "hello"
     'HELLO'
     >>> f2("abcdefg") # first call of f2 with "abcdefg"
     'ABCDEFG'
     >>> f2("abcdefg") # second call of f2 with "abcdefg"
     I already told you that the answer is ABCDEFG!
     >>> f2("hello") # second call of f2 with "hello"
     I already told you that the answer is HELLO!

     3) The function f3 accepts a tuple and returns the sum of its elements:
     >>> f3((1,2,3,4)) # first call of f3 with (1,2,3,4)
     10
     >>> f3((10,10,10,10,10,10,10,10,10,10)) # first call of f3 with (10,10,10,10,10,10,10,10,10,10)
     100
     >>> f3((1,2,3,4)) # second call of f3 with (1,2,3,4)
     I already told you that the answer is 10!

     4) Testing all functions:
     >>> f1(4) # forth call of f1 with 4
     I already told you that the answer is 16!
     >>> f2("hello") # third call of f2 with "hello"
     I already told you that the answer is HELLO!
     >>> f3((10,10,10,10,10,10,10,10,10,10)) # first call of f3 with (10,10,10,10,10,10,10,10,10,10)
     I already told you that the answer is 100!
     >>> f1(5) # first call of f1 with 4
     25
    """

    def wrapper(x, last_calls={}):

        func_name = func.__name__
        # Checks if this function has already used the decorator:
        if func_name not in last_calls.keys():
            last_calls[func_name] = {}
        # Checks if the function has already checked the current argument:
        if x in last_calls[func_name].keys():
            print(f"I already told you that the answer is {last_calls[func_name][x]}!")
        else:
            answer = func(x)
            last_calls[func_name][x] = answer
            return answer
    return wrapper

@lastcall
def f1(x: int):
    return x**2

@lastcall
def f2(s: str):
    return s.upper()

@lastcall
def f3(x: tuple):
    ans = 0
    for item in x:
        ans += item
    return ans

if __name__ == '__main__':

    import doctest
    doctest.testmod()
