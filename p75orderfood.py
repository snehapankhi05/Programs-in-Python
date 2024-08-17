""order foor""
b1=0
b2=0
b3=0
b4=0
while True:
    print("pizza =150 select==>1 \n burger =200 select==>2 \n chinese plate=500 select==>3 \n cold drink =50 select==>4")
    print("if u are done with ordering select ==>5")
    m = int(input("what would you like to order "))
    if m==1:
        p=int(input("enter your quantity"))
        b1=p*150
        print("your bill",b1)
    elif m==2:
        a=int(input("enter your quantity"))
        b2=a*200
        print("your bill", b2)
    elif m==3:
        b=int(input("enter your quantity"))
        b3=b*500
        print("your bill", b3)
    elif m==4:
        c=int(input("enter your quantity"))
        b4=c*50
        print("your bill", b4)

    elif m==5:

        print("your total bill ", b1 + b2 + b3 + b4)
        break
    else:
        print("invalid choice")




