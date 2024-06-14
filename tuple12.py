""" First way to reverse tuple"""
tupled=(11,-22,33,-44,55)
reverse=tuple(-x for x in tupled)
print(reverse)
