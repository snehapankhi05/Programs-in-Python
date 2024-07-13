temp=int(input("please enter the temperature "))
if temp==0:
    print("its frezzing temp")
elif 0<temp<10:
    print("its very cold temp")
elif 10<temp<20:
    print("its cold temp")
elif 20<temp<40:
    print("its normal temp")
elif temp>40:
    print("its very hot temp")
elif temp<0:
    print("its more than freezing temp")
else:
    pass