def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+2)

recurse(3, 0)
