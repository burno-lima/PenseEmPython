def check_fermat(a,b,c, n):
    if n > 2 and a**n + b**n  != c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work")


def inputNumber():
    a = int(input("Digite um numero: "))
    b = int(input("Digite outro numero: "))
    c = int(input("Digite outro numero: "))
    n = int(input("Ultimo numero: "))

    check_fermat(a, b, c, n)

inputNumber()
