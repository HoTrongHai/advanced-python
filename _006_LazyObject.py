import operator


class ClassA:
    def __init__(self, a3):
        self.a1 = 1
        self.a2 = "a2"
        self.a3 = a3

    def __repr__(self):
        return f"({self.a1}, {self.a2}, {self.a3})"

class ClassB:
    def __init__(self, b):
        self.b = b

    def __repr__(self):
        return f"({self.b})"


###################
empty_object = object()


def make_sure_setup_wrapped(func):
    def _inner(self, *args, **kwargs):
        if self._wrapped is empty_object:
            self._setup()
        return func(self._wrapped, *args, **kwargs)      # Same self._wrapped.func(*args, **kwargs)
    return _inner

def make_sure_setup_wrapped_calling(func, *args, **kwargs):
    def _inner(self):
        if self._wrapped is empty_object:
            self._setup()

        return func(self._wrapped, *args, **kwargs)
    return _inner


class LazyObject:
    def __init__(self):
        self._wrapped = empty_object

    # def __getattr__(self, item):
    #     if self._wrapped is empy_object:
    #         self._setup()
    #     return getattr(self._wrapped, item)

    __getattr__ = make_sure_setup_wrapped(getattr)

    def __setattr__(self, key, value):
        # This will setup attribute dict of self, not self._wrapped
        if key == '_wrapped':
            self.__dict__[key] = value

        return make_sure_setup_wrapped_calling(setattr, key, value)(self)

    def __delattr__(self, item):
        return make_sure_setup_wrapped_calling(delattr, item)(self)

    # Introspection support
    __dir__ = make_sure_setup_wrapped(dir)

    # List/Tuple/Dictionary support
    __getitem__ = make_sure_setup_wrapped(operator.getitem)
    __setitem__ = make_sure_setup_wrapped(operator.setitem)
    __delitem__ = make_sure_setup_wrapped(operator.delitem)
    __iter__ = make_sure_setup_wrapped(iter)
    __len__ = make_sure_setup_wrapped(len)


    def _setup(self):
        raise NotImplementedError("Need to provide setup for wrapped object in subclass")

class ClassLazy_A(LazyObject):
    def _setup(self):
        self._wrapped = ClassA(a3 = "777")


lazy_obj_a = ClassLazy_A()
lazy_obj_a.new_attr = "ABC"
del lazy_obj_a.new_attr

print(lazy_obj_a)
