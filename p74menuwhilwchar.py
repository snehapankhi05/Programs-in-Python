while True:
    print("Press + for addition")
    print("Press - for subtraction")
    print("Press * for multiplication")
    print("Press / for division")

    print("Press $ for EXIT")
    m = (input("select =>  "))


    if m=='+':
        a = int(input("enter 1st number"))
        b = int(input("enter 2nd number"))
        print(" add is ",a+b)
    elif m=='-':
        a = int(input("enter 1st number"))
        b = int(input("enter 2nd number"))

        print(" sub is ",a-b)
    elif m == '*':
        a = int(input("enter 1st number"))
        b = int(input("enter 2nd number"))

        print(" mult is ", a*b)
    elif m == '/':
        a = int(input("enter 1st number"))
        b = int(input("enter 2nd number"))

        print(" divi is ", a/b)

    elif m=='$':
        break
    else:
        print("invalid choice")


