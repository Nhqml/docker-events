import inspect
from collections.abc import Collection
from typing import TypeVar, Union

from . import consts
from .types import DockerEvent

# Get all types (classes) defined in module 'consts'
types = inspect.getmembers(consts, inspect.isclass)
# Define Attr as any type in 'consts' module
Attr = TypeVar('Attr', *map(lambda t: t[1], types))


def filter_attr_is(Attr_Type: Attr):
    def filter_(event: DockerEvent, match: Union[Attr_Type, Collection[Attr_Type]]):
        if isinstance(match, Attr_Type):
            match = [match]
        return Attr_Type(event[Attr_Type.__name__]) in match

    return filter_


for name, type_ in types:
    # If type is an enum, create an associated filter
    if issubclass(type_, consts.enum.Enum):
        func = filter_attr_is(type_)

        func_name = f'filter_{name.lower()}_is'
        func.__name__ = func_name
        func.__doc__ = f'Returns wether event matches (one of) the given {name}.'

        globals()[func_name] = func
