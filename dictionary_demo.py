dict1={'name':'vishal','age':27,'Lname':'mavani'}
a={'name':'ashish'}
dict1.update(a)
print(dict1)
# print(dict1)
# print(dict1.pop('name'))
# print(dict1.get('age'))
# dict1['age']=22
# print(dict1)
# print(dict1.keys())
# print(dict1.values()) 
# print(dict1.items())
# print(dict1.clear())
# a=dict1.copy()
# print(a)
# dict1.update({'add':'surat'})
# print(dict1)


a=['name','class','address']
b={}
c={}
c=b.fromkeys(a,10)
c['name']='vishal'
print(c)