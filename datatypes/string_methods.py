# str7 = 'ETL AUTOMATION testing'
# print(" Before captilize value of str7 is", str7)
# print("After capitalize  of str7 is", str7.capitalize())
# print("After applying tittle  of str7 is", str7.title())
#
# # print(" Before casefold value of str7 is", str7)
# # print("After casefold  of str7 is", str7.casefold())
# #
# # print(" Before lower value of str7 is", str7)
# # print("After lower  of str7 is", str7.lower())
# #
# # print(" Before upper value of str7 is", str7)
# # print("After upper  of str7 is", str7.upper())

# print(" Before swapcase value of str7 is", str7)
# print("After swapcase  of str7 is", str7.swapcase())

# txt = "ETL Testing"
# x =txt.center(100,'#')
# print(x)

# str8 =  'BIG DATA TESTING | ETL TESTING |AUTOMATION TETSING'
# #python is case sensitive
# print(f" count of E in {str8}", str8.count('E'))
# print(f" count of | in {str8}", str8.count('|',10,20))

# table1 = 'emp1'
# table2 = 'dep3'
# col='deptno3'
#
# query = f""" select  * from {table1} a,{table2} b
#  where a.{col}=b.{col}"""
#
# print(query)

# str7 = 'ETL  testing'

# print("ENDS with 'ING' " , str7.endswith('ing'))
# print("starts with 'ING' ", str7.startswith('ETL'))



# txt = "My name is Ståle"
# x = txt.encode()
# print(x)
# print(txt.encode(encoding="ascii",errors="backslashreplace"))
# print(txt.encode(encoding="ascii",errors="ignore"))
# print(txt.encode(encoding="ascii",errors="namereplace"))
# print(txt.encode(encoding="ascii",errors="replace"))
# print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

# txt = "H\te\tl\tl\to"
#
# print(txt)
# print(txt.expandtabs())
# print(txt.expandtabs(2))
# print(txt.expandtabs(4))
# print(txt.expandtabs(10))



# txt = "Hello, welcome to my world."
# x = txt.find("Hello")
# print(x)


# column = 'col1,col2,col30'
# # print(column.split(","))
# x=column.split(",")
# print(x)
# print("type of x" ,type(x))

key_column = ['c1','c2','c3']
key_cols = ",".join(key_column)
print(key_cols)
sql = f"select {key_cols} from table "
print(sql)
print("type of key_column",type(key_column))
print("type of key_cols",type(key_cols))