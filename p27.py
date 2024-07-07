maths=int(input("enter your marks of maths"))
sci=int(input("enter your marks of sci"))
eng=int(input("enter your marks of eng"))
phy=int(input("enter your marks pf physics"))
total=(maths+sci+phy+eng)/4
if total>33:
    print("you are pass")
else:
    print("you are fail")