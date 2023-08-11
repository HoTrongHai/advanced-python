"""
Techwith Tim
"""

class SomeClass:
    pass

def function_a(a, b):
    return a + b

class Dog():
    def __init__(self):
        self.no_exit_method()


###############

def make_class():
    class A_Class():
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return f"Name: {self.name}"

    return A_Class


cls_definition = make_class()

cls_object = cls_definition("HaiCode")
#
# print(cls_definition)
#
# print(cls_object)

#############
# Define if-else statement in a function
def if_else_contain_func(x):
    if x > 1:
        def greater_than_one():
            print(f"Value {x} is greater than 1")
        return greater_than_one
    else:
        def less_than_one():
            print(f"Value {x} is greater than 1")
        return less_than_one

_func = if_else_contain_func(2)

# print(_func)
#
# print(_func())

####################
import inspect

# print(inspect.getsource(_func))
print(inspect.get)

