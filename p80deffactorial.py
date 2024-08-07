def factorial():
    n = int(input("enter number"))
    i = n
    while i >= 1:
        print(i, end="x")
        i -= 1
factorial()