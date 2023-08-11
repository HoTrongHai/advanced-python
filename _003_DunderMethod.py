
class Class_A:
    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return f"A value = {self.a}"


    def __add__(self, other):
        return Class_A(self.a + other.a)

    def __mul__(self, other):
        return self.a * other

    def __call__(self, new_value):
        print(f"Calling form {self}")
        return self.a + new_value


def add_one_and_print_me(current_value):
    rev = current_value + 1
    print(f"Return value: {rev}")

    return rev



a_obj = Class_A(a=123)
b_obj = Class_A(a=4)


c_obj = a_obj + b_obj

c_obj.new_func = add_one_and_print_me


print(hasattr(a_obj, 'new_func'))
print(hasattr(b_obj, 'new_func'))


print(hasattr(c_obj, 'new_func'))

print(c_obj.new_func(555))
