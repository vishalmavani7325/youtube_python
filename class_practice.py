# class stringReve:
#     def str(self,a):
#         self.a=a
#         return ' '.join(reversed(a.split()))
# a=input('entar a string value:- ')

# p1=stringReve()
# print(p1.str(a))


class Emp:
    def __init__(self,id,name,salary,depart):
        self.id=id
        self.name=name
        self.salary=salary
        self.depart=depart
        
    def over_time(self,salary,hours_work):
        overtime=0
        if hours_work > 50:
            overtime=hours_work-50
            self.salary=self.salary+(overtime*(salary/50))
    def assign_department(self,Emp_depart):
        self.depart=Emp_depart
    def print_Emp_details(self):
        print('\nId=',self.id)
        print("Name=",self.name)
        print('salary=',self.salary)
        print('depart=',self.depart)
        print('\n//////////////')
    
emp1=Emp("ADAMS", "E7876", 50000, "ACCOUNTING")
emp2 = Emp("JONES", "E7499", 45000, "RESEARCH")
emp3 = Emp("MARTIN", "E7900", 50000, "SALES")
emp4=Emp("SMITH", "E7698", 55000, "OPERATIONS")
 

emp1.print_Emp_details()
emp2.print_Emp_details()
emp3.print_Emp_details()
emp4.print_Emp_details()

emp1.over_time(50000,53)


emp1.assign_department('OPERATIONS')

emp1.print_Emp_details()



class Restaurant:
    def __init__(self):
        self.menu_item={}
        self.book_table=[]
        self.customer_order=[]
        
    def add_item_to_menu(self,items):
        self.menu_item[items]=items
    

        

        