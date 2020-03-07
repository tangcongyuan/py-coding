#! /usr/bin/env python3

from functools import wraps


def require_authentication(*args, **kwargs):
    '''
        This decorator will work both with and without arguments passed.
    '''
    def decorated(func):
        @wraps(func)
        def inner(*original_args, **original_kwargs):
            print(f'Checking authentication with *args: {args}, **kwargs: {kwargs}.')
            results = func(*original_args, **original_kwargs)
            print(f'After calling decorated function')
            return results
        return inner
    
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        # called with @decorator
        return decorated(args[0])
    # called with @decorator(*args, **kwargs)
    return decorated


@require_authentication('args1', 'args2', kwarg1='kwarg1')
def do_something(*args, **kwargs):
    print(f'Inside do_something with *args: {args}, **kwargs: {kwargs}.')


class another_authentication:
    '''
        This is the class based decorator doing the same thing.
    '''
    def __init__(self, *args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            # called as @decorator
            self.function = args[0]
            self.args = args[1:]
            self.kwargs = kwargs
        else:
            # called as @decorator(*args, **kwargs)
            self.function = None
            self.args = args
            self.kwargs = kwargs
    
    def __call__(self, func=None, *args, **kwargs):
        @wraps(func)
        def inner(*original_args, **original_kwargs):
            print(f'Before calling decorated function with *args: {original_args}, **kwargs: {original_kwargs}.')
            results = func(*original_args, **original_kwargs)
            print(f'After calling decorated function')
            return results
        if not func:
            # called as @decorator
            print(f'Before calling decorated function with *args: {self.args}, **kwargs: {self.kwargs}.')
            results = self.function(*self.args, **self.kwargs)
            print(f'After calling decorated function')
            return results
        # called as @decorator(*args, **kwargs)
        return inner


@another_authentication('args1', 'args2', kwarg1='kwarg1')
def do_the_same_thing(*args, **kwargs):
    print(f'Inside do_the_same_thing with *args: {args}, **kwargs: {kwargs}.')


if __name__ == "__main__":
    do_something()
    do_the_same_thing()
