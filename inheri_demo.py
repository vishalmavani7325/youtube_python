# class cal1:
#     def add(self,a,b):
#         return a+b
# class cal2:
#     def sub(self,a,b):
#         return a-b
# class cal3:
#     def mul(self,a,b):
#         return a*b
# class cal4(cal1,cal2,cal3):
#     def div(self,a,b):
#         return a/b
    
# a=int(input('enter A value: '))
# b=int(input('enter B value: '))

# p1=cal4()
# print(p1.add(a,b))
# print(p1.sub(a,b))
# print(p1.mul(a,b))
# print(p1.div(a,b))

# //////

class person:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print(self.id,self.name)
        
emp=person(77,'ajay')
emp.display()

# class Emp(person):
#     def print(self):
#         print('emp print')
        
#     Emp_details = Emp("Mayank", 103)
    
#     Emp_details.display()
    
#     Emp_details.print()
