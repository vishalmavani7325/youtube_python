# class a:
#     def __init__(self,age):
#         self.age=age
# obj=a() 


# class A:
#     "vishal "
# obj=A()
# print(A.__doc__)

# class A:
#     def fun(self,age,name,address):
#         print(age,name,address)
        
# obj=A()
# # obj=A(17,'vishal','surat')
# obj.fun(17,'vishal','surat')

# age=10
# class A:
#     def __init__(self):
#         self.age=age
#         # print(self.age)
# obj=A()
# print(obj.age)


# class cla:
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def mul(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a/b
# a=int(input('entar a value:- '))
# b=int(input('entar a value:- '))

    
# pa=cla()
# print(pa.add(a,b))
# print(pa.sub(a,b))
# print(pa.mul(a,b))
# print(pa.div(a,b))

class cal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    
a=int(input('entar a value:- '))
b=int(input('entar a value:- '))
    
    
p1=cal(a,b)
choice=1
while True:
    print('1 is Add')
    print('2 is sub')
    print('3 is mul')
    print('4 is div')
    choice=int(input('enter a choice:- '))
    if choice==1:
        print('result:= ',p1.add())
    elif choice==2:
        print('result:= ',p1.sub())
    elif choice==3:
        print('result:= ',p1.mul())
    elif choice==4:
        print('result:= ',p1.div())
    else:
        print('invalid choice')
        
print()