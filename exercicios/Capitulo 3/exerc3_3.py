"""Escreva uma função que desenhe uma grade como a seguinte:"""
"""   + - - - - + - - - - +
        |            |            |
        |            |            |
        |            |            |
        |            |            |
       + - - - - + - - - - +
        |            |            |
        |            |            |
        |            |            |
        |            |            |
        + - - - - + - - - - +"""
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def top():
    print('+ - - - -', end=' ')

def meio():
    print('|        ', end=' ')

def tops():
    do_twice(top)
    print("+")

def meios():
    do_twice(meio)
    print("|")

def row():
    tops()
    do_four(meios)

def columas():
    do_twice(row)
    tops()

columas()
