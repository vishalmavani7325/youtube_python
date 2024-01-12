# var={10,55.77,'mavani'}
# var.add('vishal')
# # # var.update(['ram','sita'])
# print(var.pop())
# # # var.remove(10)
# # var.clear(  )
# # print(var)
# # print(type(var)) 


# dir(set)



# a=set([1,2,3,4,5,])
# print(type(a))
# var={1,2,3,73.25,'vishal','vishal'}
# var.add('ram')
# var2={1,2,3,4,2,73.25,'mavani'}
# var3=var.copy()
# print(var3)
# var3.add('mavani')
# print(var3)
# print(var)


# var={1,2,3,77,73.25,'vishal','vishal'}
# var2={1,2,3,4,2,73.25,'mavani',77}
# print(var)
# print(var2)
# var2.difference(var)
# print(var)
# print(var2)

# a={1,2,3,4,5,7,8}
# b={3,4,5,6,7}
# a.difference_update(b)
# print(a) 

# fruits = {"apple", "banana", "cherry"}
# fruits.discard("banana")
# print(fruits)

# a={1,2,3,4,5}
# b={4,5,6,7,8}
# # print(a)
# a.intersection(b)
# print(a)


# a={1,2,3,4,5}
# b={4,5,}
# a.intersection_update(b)
# print(a)

# a={1,2,3,4}
# b={3,4,5,6}
# a.isdisjoint(b)
# print(a)

# a={1,2,3,4,6}
# b={3,4,5,6}
# a.issuperset(b)
# print(a)

# a={1,2,3,4}
# b={3,4,5,6}
# b.issubset(a)
# print(b)


# a={1,2,3,4,5}
# a.pop()
# print(a)

# a={1,2,3,4,5}
# a.remove(5)
# print(a)

# x = {"apple", "banana", "cherry",7}
# y = {"google", "microsoft", "apple",7}
# x.update(y)
# print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple",7}
x.union(y)
print(x)