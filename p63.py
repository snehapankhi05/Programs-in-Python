n= int(input("Enter the limit for the series: "))
sum = 0
series = " "

for i in range(1, n+1):
    n = (-1)**(i)*i
    sum += n
    series += str(n) + " "



print("Series:", series)
print("Sum:", sum)


"""
-1+2-3+4-5 ...sum
"""
