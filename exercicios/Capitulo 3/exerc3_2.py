"""Um objeto de função é um valor que pode ser atribuído a uma variável ou passado como argumento. Por exemplo, do_twice é uma função que toma um objeto de função como argumento e o chama duas vezes:"""

def do_twice(f):
    f()
    f()


def print_spam():
    print('spam')
do_twice(print_spam)


def do_four(f):
    do_twice(f)
    do_twice(f)
    