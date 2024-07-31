while True:
    print("Press 1 for square")
    print("Press 2 for cube")
    print("Press 3 for EXIT")
    m = int(input("select =>"))
    if m==1:
        n = int(input("enter number"))
        print(n," square is ",n*n)
    elif m==2:
        n = int(input("enter number"))
        print(n," cube is ",n*n*n)
    elif m==3:
        break
    else:
        print("invalid choice")


