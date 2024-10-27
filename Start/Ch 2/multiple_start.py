# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"


class C(A, B):
    def __init__(self):
        super().__init__()

    def show_props(self):
        print(self.prop1)
        print(self.prop2)

c = C()
c.show_props()