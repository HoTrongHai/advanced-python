
def process_request_handle(request):
    # Do something with request
    print(request)
    return request

class Middleware_A:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def make_something(self, request):
        print(f"Inside {self.__class__}, make something with {self.a}, {self.b}, {request}")
        return request, self.a, self.b


class Middleware_B:
    def __init__(self, c):
        self.c = c

    def make_something(self, request):
        print(f"Inside {self.__class__}, make something with {self.c}, {request}")
        return request, self.c

# Normal: request >> handle by process_request_handle
request = "A request"
process_request_handle(request)

# Then now we want to change behavior of the function `processs_request` with flexible middleware

def make_middleware(middle_obj, handle_func, request):
    # What is request paramter ?
    request_change_by_middle, *args = middle_obj.make_something(request)
    request_final = handle_func(request_change_by_middle)
    return request_final

# make_middleware(Middleware_A(a=1, b=2), process_request_handle, request)
# new_request = make_middleware(Middleware_B(c="CCC"), lambda r: r + "BBB", request)


def make_middleware2(middle_obj, handle_function):
    def _inner_func(request):
        request_change_by_middle, *args = middle_obj.make_something(request)
        request_final = handle_function(request_change_by_middle)
        return request_final
    return _inner_func

mixed_func = make_middleware2(Middleware_A(a=1, b=2), process_request_handle)


mixed_func(request)