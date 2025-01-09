# 1
text = "ABBA"
text_2 = text[::-1]

# 2
lst = [1, 3, 5.6]
lst2 = []
for i in lst:
    if isinstance(i, int):
        lst2.append(2*i)
    else:
        lst2.append(i)
print(lst2)

# 3 завдання на рекурсію
def factorial(n):
    lst = [1]
    for i in range(2, 11):
        lst.append(i * lst[-1])
    return lst
values = factorial(10)
print(values)

keys = []
for i in range (1, 11):
    keys.append(i)

dict_result = dict(zip(keys, values))
print(dict_result)

# 4 - використати функцію зіп з завдання 3
# 5
string = 'dfgertgqweliufhcsdjrhy2oYUGFEWYUgrt;'
mystring = string.lower()

dict_result = {}
holosni = ("a", "e", "i", "o", "u")
for i in holosni:
    dict_result[i] = mystring.count(i)
print(dict_result)

# Методи даних
# 1
lst = ["sdfsdhh", "efewwfffw", "sdsd", "fwegferghetrh"]
lst.sort(key = len)
print(lst)

# 2
dict_task = {"a":"a", "bc":"bc", "z":"z"}
key_list = list(dict_task.keys())
key_list.sort(reverse=True)
print(key_list)
print(tuple(dict_task.keys()))

# 3
my_list2 = ["1121", '111', '22', "AaA"]
my_list2 = [i.lower() for i in my_list2]

lst_2 = []
for value in my_list2:
    lst_3 = []
    for i in value:
        if i not in lst_3:
            lst_3.append(i)
    value_res = "".join(lst_3)
    lst_2.append(value_res)
print(lst_2)

# 5
value = 22222
str(value)

# 9
dict_task2 = {"Name": "Nata", "Surname": None, "city": "Kyiv"}
key_list = list(dict_task2.keys())

dict_result = {}
for key in key_list:
    if dict_task2[key]:
        dict_result[key] = dict_task2[key]
print(dict_result)

# Sorted
# 1
lilist = ("aaaaaz", "aaaab", "yza")
def last(lilist):
    return lilist[-1]
result = sorted(lilist, key = last)
print(result)

# 2 Те саме як в п. 1

# 4
goods = [("a", 2), ("b", 7), ("c", 3), ("d", 100)]

def get_price(i):
    return i[-1]
goods_result = sorted(goods, key = get_price, reverse = True)
print(goods_result)

# filter
#1
lst = [2, 4, 5, 7, 8, 33, 9, 10, 11, 50]

def check(i):
    if i%2 == 0:
        return i
def even(numbers):

    results = list(filter(check, numbers))
    return results
print(even(lst))

# 3
def criteria(i):
    if i > 10:
        return i

def greater_10(numbers):
    resultus = list(filter(criteria,numbers))
    return resultus
print(greater_10(lst))