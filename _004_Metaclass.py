
class Test:
    pass


# print(Test, type(Test))    # Test is type object

# test_obj = Test()

# print(test_obj, type(test_obj)) # object >> class >> type


def func_a(a, b ,c):
    return None

# print(type(func_a))  # <class 'function'>



# Type2 = type('Type2', (), {'a': 222})  # Class name, tuple of base, attrs
"""
class Type2:
    a = 222
"""


# print(Type2)

# print(Type2().a)

# attrs_class = Type2.__dict__
# attrs_ins = Type2().__dict__
#
#
#
# print(set(attrs_class.keys()) - set(attrs_ins.keys()))

# Type2 = type('Type2', (), {'a': 222})  # Class name, tuple of base, attrs

class MetaHaiCode(type):
    def __new__(self, class_name, bases, attrs): # Initiate class type/definition >> can hook creation of class type

        # _class_name = class_name.upper()
        _attrs = attrs
        _attrs["_my_attr"] = 123   # add new attribute of class level

        return type(class_name, bases, _attrs)




class PythonCode(metaclass=MetaHaiCode):
    b = 222
    c = "hello"
    def func_python(self):
        return "ABC"
    def __init__(self): # Initiate object of the class
        self.a = 444    # attribute of instance level

python_code = PythonCode()
attrs = python_code.__dict__
print(python_code._my_attr)

