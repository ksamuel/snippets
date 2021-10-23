import builtins
from functools import partial
from collections import *
from pprint import pprint as pretty_print
from inspect import getmembers, ismethod, stack

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
    
    from rich.pretty import install
    install()
    from rich.traceback import install
    install()
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
