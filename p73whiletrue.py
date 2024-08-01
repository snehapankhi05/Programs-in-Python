while True:
    print("Press 1 for addition")
    print("Press 2 for subtraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")

    print("Press 5 for EXIT")
    m = int(input("select =>  "))


    if m==1:
        a = int(input("enter 1st number"))
        b = int(input("enter 2nd number"))
        print(" add is ",a+b)
    elif m==2:
        a = int(input("enter 1st number"))
        b = int(input("enter 2nd number"))

        print(" sub is ",a-b)
    elif m == 3:
        a = int(input("enter 1st number"))
        b = int(input("enter 2nd number"))

        print(" mult is ", a*b)
    elif m == 4:
        a = int(input("enter 1st number"))
        b = int(input("enter 2nd number"))

        print(" divi is ", a/b)

    elif m==5:
        break
    else:
        print("invalid choice")


