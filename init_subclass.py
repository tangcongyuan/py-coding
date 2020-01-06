from typing import (
    Any,
)

class Base:
    def __init_subclass__(cls,
                          abstract: bool = False,
                          **kwargs: Any) -> None:
        print(f'Base class __init_subclass__.')
        print(f'cls = {cls}.')
        print(f'abstract = {abstract}.')
        print(f'**kwargs = {kwargs}.')

class Derived(Base,
              abstract = True,
              key='value'):
    def __init_subclass__(cls,
                          abstract: bool = False,
                          **kwargs: Any) -> None:
        print(f'Derived class __init_subclass__.')
        print(f'cls = {cls}.')
        print(f'abstract = {abstract}.')
        print(f'**kwargs = {kwargs}.')


if __name__ == '__main__':
    d = Derived()