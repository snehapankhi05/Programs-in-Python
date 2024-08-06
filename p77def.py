def square():
    x=int(input("enter number"))
    print("s=",x*x)

def area():
    n=int(input("enter base"))
    m=int(input("enter height"))

    print("area of traingle",0.5*n*m)

def areaofcir():
    n=int(input("enter radius"))


    print("area of circle",3.14*n*n)

def table():
    n = int(input("enter number"))
    m = int(input("enter multiplication number"))
    s = 1
    i = 1
    while i <= n:
        s = s * i
        print(m, "x", i, "=", s)
        i += 1

def factorial():
    n = int(input("enter number"))
    i = n
    while i >= 1:
        print(i, end="x")
        i -= 1

def oddeven():
    n = int(input("enter number"))
    i = 1
    while i <= n:
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")
        i += 1

def max():
    n=int((input("enter 1st number")))
    m=int(input("enter 2nd number"))
    if n>m:
        print("larger is==",n)
    else:
        print("larger is",m)

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


print("Press 1 for square")
print("Press 1 for square")
print("Press 2 for area of traingle")
print("Press 3 for area of circle")
print("Press 4 for table of any number")
print("Press 5 for factorial")
print("Press 6 for odd even")
print("Press 7 for max number between 2 number")
print("Press 8 for max number between 3")

op=int(input("Enter op =>"))

if op==1:
    square()
elif op==2:
    area()
elif op==3:
    areaofcir()
elif op==4:
    table()
elif op==5:
    factorial()
elif op==6:
    oddeven()
elif op==7:
    max()
elif op==8:
    max3()
else:
    print("invalid option")



#add sub mul div
#oddeven add max2