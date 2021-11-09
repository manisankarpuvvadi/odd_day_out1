l=(input().split(","))
l=tuple(l)
e=0
o=0
for i in range(len(l)):
    if i%2==0:
        e=e+1
    else:
        o=o+1
print("Number of even numbers :",e)
print("Number of odd numbers :",o)
