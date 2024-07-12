print("pizza=200 ")
print("burger=150")
print("shake=300")
print("fries=100")
print("for pizza press 'P' , for burger press 'B' , for shake press 'S' , for fries press 'F'")
a=(input("please order your food :  "))
b=int(input("How much quantity do you want: "))
if a=='P':
    print("here is your bill:", 200*b)
elif a=='B':
    print("here is your bill:", 150*b)
elif a=='S':
    print("here is your bill:", 300*b)
elif a=='F':
    print("here is your bill:", 100*b)
else:
    print("you have selected wrong option")

