from pprint import pprint as pp
import math

class PointND:

    def __init__(self,*args):
        for arg in args:
            if not type(arg) is float:
                raise ValueError("Cannot instantiate an object with non-float values.")
        print(args)
        self.n = len(args)
        self.t = tuple(args)

if __name__ == "__main__":
# testing PointND
    p1 = PointND(1.2, 2.1, 3.23, 4.1)
