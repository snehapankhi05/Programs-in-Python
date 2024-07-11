print("press a for additon ")
print("press b for subtraction ")
print("press m for multiplication ")
print("press d for division ")
x=(input("enter your option= "))
y=int(input("enter your 1st number="))
z=int(input("enter your second number"))
if x=="a":
    print(y+z)
elif x=="b":
    print(y-z)
elif x=="m":
    print(y*z)
elif x=="d":
    print(y/z)
else:
    print("You have selected wrong option ")
