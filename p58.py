n=int(input("enter the number"))
m=int(input("multiple "))
c=0
s=0
for i in range(1,n+1):
   if i % m ==0:
        print(i,end=" + ")
        c=c+1
        s=s+i
print("\nSum = ",s," Count = ",c)
""" 
to print sum and count of a number divisble by the given number
"""