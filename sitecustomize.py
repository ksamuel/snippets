import builtins

from prettyprint import pprint as pretty_print

try:
    
    from rich.pretty import install
    install()
    from rich.traceback import install
    install()
    from rich.pretty import pprint
    builtins.pp = builtins.pprint = pprint 
 
except ImportError:
    def pprint(obj):
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


 
class Printer(float):

    def __call__(self, *args, **kwargs):
        pprint(*args, **kwargs)
    def __truediv__(self, other):
        pprint(other)

    def __rtruediv__(self, other):
        pprint(other)


pp = Printer()
