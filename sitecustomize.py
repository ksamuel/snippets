import builtins
import asyncio
import sys
from functools import partial
from collections import *
from pprint import pprint as pretty_print
from inspect import getmembers, ismethod, stack

import logging


import __main__

if not hasattr(__main__, "__file__"):
    logging.getLogger("asyncio").setLevel("ERROR")


STDLIB_COLLECTIONS = (
    str,
    bytes,
    int,
    float,
    complex,
    memoryview,
    dict,
    tuple,
    set,
    bool,
    bytearray,
    frozenset,
    slice,
    deque,
    defaultdict,
    OrderedDict,
    Counter,
)


def is_public_attribute(obj, name, methods=()):
    return not name.startswith("_") and name not in methods and hasattr(obj, name)


def attributes(obj):
    members = getmembers(type(obj))
    methods = {name for name, val in members if callable(val)}
    is_allowed = partial(is_public_attribute, methods=methods)
    return {name: getattr(obj, name) for name in dir(obj) if is_allowed(obj, name)}


try:
    import chime

    chime.theme("material")
    chime.notify_exceptions()
except ImportError:
    pass

try:
    if sys.__excepthook__ is sys.excepthook:
        from rich.pretty import install

        install()
        from rich.traceback import install

        replaced_hook = install(show_locals=True)
        current_hook = sys.excepthook

        def hook(*args, **kwargs):
            print("na")
            replaced_hook(*args, **kwargs)
            current_hook(*args, **kwargs)

        sys.excepthook = hook

    from rich.pretty import pprint

    class Printer(float):
        def __call__(self, *args, **kwargs):
            pprint(*args, **kwargs)

        def __truediv__(self, other):
            pprint(other)

        def __rtruediv__(self, other):
            pprint(other)

    builtins.pp = builtins.pprint = Printer()

except ImportError:
    pass


def inspect(obj):
    if isinstance(obj, STDLIB_COLLECTIONS):
        pretty_print(obj)
    else:
        try:
            name = "class " + obj.__name__
        except AttributeError:
            name = obj.__class__.__name__ + "()"
        class_name = obj.__class__.__name__
        print(name + ":")
        attrs = attributes(obj)
        if not attrs:
            print("    <No attributes>")
        for name, val in attributes(obj).items():
            print("   ", name, "=", val)


builtins.inspect = inspect

