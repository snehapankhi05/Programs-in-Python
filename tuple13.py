"""Second way to reverse tuple"""
tupled=(1,3,5,4,8)
list1=list(tupled)
list1.reverse()
tupled=tuple(list1)
print(tupled)