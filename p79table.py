def table():
    n = int(input("enter number"))
    m = int(input("enter multiplication number"))
    s = 1
    i = 1
    while i <= n:
        s = s * i
        print(m, "x", i, "=", s)
        i += 1
table()