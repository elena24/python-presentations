from functools import wraps


class greater_than_zero(object):
    def __init__(self, function):
        print("greater_than_zero.__init__")
        self.function = function
        self.__name__ = 'greater_than_zero'

    def __call__(self, *args, **kwargs):
        print("greater_than_zero.__call__({},{})".format(args, kwargs))
        for item in args:
            if item < 0:
                print("Invalid argument `{}`".format(item))
                return
        self.function(*args, **kwargs)


class greater_than(object):
    def __init__(self, value):
        print("greater_than_{}.__init__".format(value))
        self.value = value

    def __call__(self, function):
        print("greater_than_{}.__call__({})".format(self.value, function))

        def wrapped_f(*args, **kwargs):
            print "Inside wrapped_f()"
            for item in args:
                if item < self.value:
                    print("Invalid argument `{}`".format(item))
                    return
            function(*args, **kwargs)

        return wrapped_f


def decorator(function):
    def inner(*args, **kwargs):
        print("decorator[inner]")
        function(*args, **kwargs)
    return inner


def decorator2(function):
    @wraps(function)
    def inner(*args, **kwargs):
        print("decorator[inner]")
        function(*args, **kwargs)
    return inner


@greater_than_zero
def test(*args):
	print("test({})".format(args))

@greater_than(2)
def test2(*args):
    print("test2({})".format(args))
	
@decorator
def test3():
    pass


@decorator2
def test4():
    """Interesant nu ?"""
    pass

if __name__ == "__main__":
    test(1, 2, 3, 4, 5)
    print("-" * 10)
    test(-1, 0, 1, 2)
    print("-" * 10)
    test2(2, 3, 4, 5)
    print("-" * 10)
    test2(1, 2, 3)
    print("-" * 10)
    print(test.__name__)
    print(test2.__name__)
    print(test3.__name__)
    print(test4.__name__)
    print(test4.__doc__)
	