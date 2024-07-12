print("Welcome to our store")
print("for Xerox press = x ")
print("for type writing press = t ")
print("for both press = b ")
print("if you have more than 10 pages then the amount of xerox  for 1 page is 10rs and for typing for 1 page is 10rs")
print("if you have less than 10 pages then the amount of xerox and for 1 page is 5rs and for typing for 1 page is 15rs")
a=(input("what would you like to do "))
if a=='x':
    b=int(input("how much pages?"))
    if b>10:
        print("here is your bill",b*5)
    else:
        print("your bill is : ",b*10)
elif a=='t':
    b=int(input("how much pages do you want?"))
    if b>10:
        print("here is ur bill",b*15)
    else:
        print("here is your bill:",b*10)
if a=='b':
    xerox=int(input("pages for xerox?"))
    type=int(input("pages for typing?"))
    xeroxcost = 5 if xerox>10 else 10
    typecost = 10 if type>10 else 15
    xeroxtotal = xerox*xeroxcost
    typetotal = type*typecost
    total = xeroxtotal+typetotal
    print("your total bill is ",total)
else:
    print("you have selected wrong option")