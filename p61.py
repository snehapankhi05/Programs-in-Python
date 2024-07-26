"""
to print 1/2+1/3+1/4+1/5.....sum
"""
n=int(input("enter number"))
s=0
for i in range(1,n+1):
    print("1/",i, end=" + ")
    s = s + i
print("Sum = ",s)

"""
1+1/2+1/3
"""