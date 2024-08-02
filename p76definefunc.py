def square():
    x=int(input("enter number"))
    print("s=",x*x)
square()
def area():
    n=int(input("enter base"))
    m=int(input("enter height"))

    print("area of traingle",0.5*n*m)
area()
def areaofcir():
    n=int(input("enter radius"))


    print("area of circle",3.14*n*n)
areaofcir()
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
def factorial():
    n = int(input("enter number"))
    i = n
    while i >= 1:
        print(i, end="x")
        i -= 1
factorial()
def oddeven():
    n = int(input("enter number"))
    i = 1
    while i <= n:
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")
        i += 1
oddeven()
def max():
    n=int((input("enter 1st number")))
    m=int(input("enter 2nd number"))
    if n>m:
        print("larger is==",n)
    else:
        print("larger is",m)
max()
def max3():
    n=int(input("enter 1st number"))
    m = int(input("enter 2nd number"))
    o = int(input("enter 3rd number"))
    if n>m and n>o:
        print("1st number is greater")
    elif m>n and m>0:
        print("2nd number is larger")
    else:
        print("3rd number is larger")


max3()
