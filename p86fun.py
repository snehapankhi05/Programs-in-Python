
def oddeven(x):
    if x % 2 == 0:
        print("its even")
    else:
        print(" its odd")

def max(x,y):
    if x>y:
        print("larger is==",x)
    else:
        print("larger is",y)

def add(x,y):
    print("Add = ",x+y)


x = int(input("enter your first value"))
y = int(input("enter your second number"))
add(x,y)
max(x,y)
oddeven(x)