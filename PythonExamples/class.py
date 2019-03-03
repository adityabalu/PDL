

class A(object):
    """docstring for A"""
    def __init__(self, a=4, b=10, c=20):
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a
    
    @property
    def b(self):
        return self._b
    
    @property
    def c(self):
        return self._c
    
    def __repr__(self):
        return "A Object"


if __name__ == '__main__':
    a = A(4,6,8)
    print(a)
    print(a.a)
    print(a.b)
    print(a.c)
    b = A()
    print(b)
    print(b.a)
    print(b.b)
    print(b.c)
