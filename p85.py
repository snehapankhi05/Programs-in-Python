def add(x,y):
    print("addition=", x + y)

def sub(x,y):
    print("sub=", x - y)

def mul(x,y):
    print("mul=",x*y)

def div(x,y):
     print("div=", x / y)

def oddeven(z):
    if z % 2 == 0:
        print("its even")
    else:
        print(" its odd")

def max(x,y):
    if x>y:
        print("larger is==",x)
    else:
        print("larger is",y)



x = float(input("enter your first value"))
y = float(input("enter your second number"))
z=int(input("enter number for odd even"))

add(x,y)
mul(x,y)
sub(x,y)
div(x,y)
oddeven(z)
max(x,y)




