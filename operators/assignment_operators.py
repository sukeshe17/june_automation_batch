# This file is created to practice  assignemnt operator datatype concept
# Created by suketh :  on 06/07/2024

a = 5

x = y = z = 10
print("values of x ,y ,z ", x, y, z)
print("id of x y z", id(x), id(y), id(z))

k, l, m = 10, 20, 50
print("values of k,l ,m ", k, l, m)
print("id of k l m ", id(k), id(l), id(m))

p = 10

p += 5  #p = p+5 # compound assignment
print("p value is ", p)
p -= 6  #p = p-6
print("p value is ", p)
p *= 3  #p = p*6
print("p value is ", p)

p /= 3
print("p value is ", p)


a=2
b=2

print("a ** b",a ** b)

a**=a #a=a**a
print("value of a",a)


# print("a**=b",a**=b)

j=10

j%=4 # j= j%2

print(j)