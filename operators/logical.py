j = 45


if j % 2 == 0:
    print("even numbe")

else:
    print("Odd number")


#operation_1 P
a = 6
b = 2
P = a > b

#operation_2 Q
c = 9
d = 15
Q = c > d

#Evaluations
print(P and Q)
print(P or Q)
print(not(P or Q))
print(not(P and Q) )

#values to be evaluated
w = 10
x = 4
y = 8
z = 12

#and
print((w<x) and (y>z))  

#or
print((w<x) or (y<z)) 

#not
print(not((w<x) and (y>z)))


