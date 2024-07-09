print("Press 1 for square")
print("Press 2 for cube")
op=int(input("Enter option =>"))

if op==1:
    a=int(input("enter your number =>"))
    print("Square = ",a*a)
elif op==2:
    a = int(input("enter your number =>"))
    print("Cube = ", a * a*a)
else:
    print("Wrong opt")