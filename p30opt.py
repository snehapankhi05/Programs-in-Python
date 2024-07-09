print("Press s for square")
print("Press c for cube")
op=input("Enter option =>")

if op=="s":
    a=int(input("enter your number =>"))
    print("Square = ",a*a)
elif op=="c":
    a = int(input("enter your number =>"))
    print("Cube = ", a * a*a)
else:
    print("Wrong opt")