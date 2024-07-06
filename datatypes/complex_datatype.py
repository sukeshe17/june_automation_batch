# This file is created to practice  boolean datatype function
# Created by suketh :  on 25/06/2024
a = 1.5-5j #(1 is a real value 2 is a imaginary value)
print("value of a is", a)
print("type of a is", type(a))
print("id of a is", id(a))

b = 1.5-5j
print("value of a is", b)
print("type of a is", type(b))
print("id of a is", id(b))

c = -5j
print("value of c is", c)
print("type of c is", type(c))
print("id of c is", id(c))

# d = False
# print("value of d is", d)
# print("type of d is", type(d))
# print("id of d is", id(d))

print("methods available on complex type a", dir(a))

print("real value of a", a.real)
print("imgaginary value of  a", a.imag)
