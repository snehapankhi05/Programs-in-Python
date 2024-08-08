limit = int(input("Enter the limit for the series: "))
sum_series = 0
series = " "

for i in range(1, limit+1):
    term = (-1)**(i+1) * i**2
    sum_series += term
    series += str(term) + " "

print("Series:", series)
print("Sum:", sum_series)

"""
we have to print
1-4+9-16+25 ...sum
"""