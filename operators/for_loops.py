# ls =[1,2,3,4]
# ls_square=[]
# for i in ls :
#     print("i value is :", i)
#     ls_square.append(i*i)
#
# print(ls_square)


# t =(1,2,3,4)
# t_square=[]
# for i in t :
#     print("i value is :", i)
#     t_square.append(i*i)
#
# print(t_square)

# mul = 1
# t =[1,2,3,4,5]
# for i in t :
#     mul=mul*i
# print("mul" ,mul)

# sum = 0
# t =[1,2,3,4,5]
# for i in t :
#     sum=sum+i
# print("sum" ,sum)

# ls =[1,2,3,4,5,6,7,8,9,10]
# even_sum = 0
# odd_sum  = 0
# for i in ls:
#     if i % 2 == 0:
#         even_sum =even_sum+i
#     else:
#         odd_sum = odd_sum + i
# print("even_sum",even_sum)
# print("odd_sum",odd_sum)
# print("total sum",even_sum+odd_sum)


str1 ="ETL Automation"
#vowels a,e,i,o,u
for i in str1.lower():
    # print("i value is:",i)
    if i in ['a','e','i','o','u']:
        print("vowel present")
        break
    else:
        print("vowel not present")


str1 ="ETL Automation"
str2 =''
for i in str1:
    if i.islower():
        str2=str2+i.upper()
    else i.isupper():
        str2 = str2 + i.lower()

print("str2",str2)