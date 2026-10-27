class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, Pointer Arithmetic={self.pointer_arithmetic}, First appeared in {self.year}"

    def __repr__(self):
        return f"{vars(self)}"

    def is_dynamic(self):
        return self.typing == "Dynamic"


def run_tests():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)
    c_plus_plus = ProgrammingLanguage("C++", "Static", False, 1983, True)

    print(python)
    print(repr(python))

    assert python.reflection is True
    assert python.is_dynamic() is True
    assert python.year == 1991
    assert python.pointer_arithmetic is False
    assert ruby.reflection is True
    assert visual_basic.is_dynamic() is False
    assert c_plus_plus.pointer_arithmetic is True

