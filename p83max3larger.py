def max3():
    n=int(input("enter 1st number"))
    m = int(input("enter 2nd number"))
    o = int(input("enter 3rd number"))
    if n>m and n>o:
        print("1st number is greater")
    elif m>n and m>0:
        print("2nd number is larger")
    else:
        print("3rd number is larger")
max3()