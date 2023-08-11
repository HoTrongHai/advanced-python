
def func_print(func):
    print("Starting with function")
    func()
    print("End function")

def func_a():
    print("Inside function a")

def func_b(b):
    print('Do somthing with function b')
    return b + 1

# func_print(func_a)

################

def func_print_2(func):
    def _wrapper(*args, **kwargs):
        print("Starting with function")
        rv = func(*args, **kwargs)
        print("End function")
        return rv
    return _wrapper


func_b = func_print_2(func_b)

# print(func_b(111))

# new_func_mix_a = func_print_2(func_a)
# print(new_func_mix_a())


@func_print_2                             # func parameter is `func_c`
def func_c(c):
    print('Do something inside func c')
    return c + 2

# print(func_c(100))


@func_print_2
def func_d(d1, d2, d3=123):
    print('Do something inside func d')
    return d1 + d2 + d3

# print(func_d(d1=1, d2=10))


###############
# Example: measure time of function
import time

def how_much_time(f):

    def _wrapper(*args, **kwargs):
        start = time.time()
        rv = f(*args, **kwargs)
        end = time.time()
        total = end - start
        print(total)
        return rv, total

    return _wrapper


@how_much_time
def heavy_func(r):
    for i in range(r):
        time.sleep(1)

    return True

rv, total =  heavy_func(5)

print(rv, total)



