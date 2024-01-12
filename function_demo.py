# def add(x,y):
#     sum=x+y
#     return print(sum)
# add(14,4)

# def calculator(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
    
# calculator(1,3)
# calculator(1,8)
# calculator(1,5)
# calculator(1,4)



# 1/////////////

# def add(a,b,c):
#     sum=a+b+c
#     return sum



# def funcation1(a,b):
#     answer= a+b
#     return print('answer is ',answer)
# funcation1(6,7)

# //////

# def add(x,y):
#     return x+y


# def sub(x,y):
#     return x-y


# def mul(x,y):
#     return x*y


# def div(x,y):
#     return x/y
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
# while True:
#     choice=input('enter choice(1/2/3/4): ')
    
#     if choice in ('1','2','3','4'):
#         try:
#             num1=float(input('enter first number: '))
#             num2=float(input('enter second number: '))
#         except ValueError:
#             print('invalid input')
#             continue
        
#         if choice=='1':
#             print(num1,'+',num2,'=',add(num1,num2))
#         elif choice=='2':
#             print(num1,'-',num2,'=',sub(num1,num2))
#         elif choice=='3':
#             print(num1,'*',num2,'=',mul(num1,num2))
#         elif choice=='4':
#             print(num1,'/',num2,'=',div(num1,num2))
#         else:
#             print('invalid value')
        
# //////////

# marks=int(input('enter a marks: '))
# if marks>0 and marks<35:
#     print('fail')
# elif marks>35 and marks<50:
#     print('D')
# elif marks>50 and marks<65:
#     print('C')
# elif marks>65 and marks<75:
#     print('B')
# elif marks>75 and marks<90:
#     print('A')
# elif marks>90 and marks<100:
#     print('A+')
    
# //////////////////


# print('enter a 5 subjects marks')
# marks1=int(input())
# marks2=int(input())
# marks3=int(input())
# marks4=int(input())
# marks5=int(input())

# total=marks1+marks2+marks3+marks4+marks5
# print(total)
# avg=total/5
# print(avg)

# if avg>=91 and avg<100:
#     print(f'A+')
# elif avg>=81 and avg<91:
#     print('A')
# elif avg>=71 and avg<81:
#     print('B')
# elif avg>=61 and avg<71:
#     print('C')
# elif avg>=51 and avg<61:
#     print('D')
# elif avg>=41 and avg<51:
#     print('E')
# elif avg>=35 and avg<41:
#     print('E1')
# elif avg>=0 and avg<35:
#     print('fail')


# ///////



# def subjects(s1,s2,s3,s4,s5):
#     total=s1+s2+s3+s4+s5
#     avg=(total/5.0)
#     per=(total/500)*100
#     if avg>=91 and avg<100:
#         print(f'A+')
#     elif avg>=81 and avg<91:
#         print('A')
#     elif avg>=71 and avg<81:
#         print('B')
#     elif avg>=61 and avg<71:
#         print('C')
#     elif avg>=51 and avg<61:
#         print('D')
#     elif avg>=41 and avg<51:
#         print('E')
#     elif avg>=35 and avg<41:
#         print('E1')
#     elif avg>=0 and avg<35:
#         print('fail')
        
#     return print(avg)
    
# subjects(33,44,55,66,77)



# l1=[1,2,3,4,5,6,7,8,9]

# even_l1=[]
# odd_l2=[]
# for i in l1:
#  if i%2==0:
#     even_l1.append(i)
#  else:
#      odd_l2.append(i)
 
# print('number list:-',l1)
# print('even number:-',even_l1)
# print('odd number:-',odd_l2)

# //////

# def maxnumber(a,b,c):
#     if a>b and a>c:
#         print('a is big')
#     elif b>a and b>c:
#         print('b is big')
#     else:
#         print('c is big')
        
# maxnumber(21,11,5)




def Ebill(unit):
    if unit>0 and unit<=100:
        payment=unit*1.5
        fixcharge=25
    elif unit>100 and unit<=200:
        payment=(100*1.5)+(unit-100)*2.5
        fixcharge=50
    elif unit>200 and unit<=300:
        payment=(100*1.5)+(200-100)+(unit-200)*4
        fixcharge=75
    elif unit>300 and unit<=350:
                payment=(100*1.5)+(200-100)+(300-200)*4+(unit-300)*5
                fixcharge=100
    else:
        payment=0
        fixcharge=1500
    return payment+fixcharge
u=float(input('enter a unit'))
totalbill=Ebill(u)

print(totalbill)


# def ram(a):
#     if a:
#         print('a is big')
#     else:
#         print('b is big')
    
# c=int(input('enter num'))
# bignum=ram(c)
# print(bignum)


# def greet(Fname,Lname):
#     print(Fname,Lname)
    
# greet('Vishal','Mavani')


# def greet(a='guest'):
#     print('good',a)
    
# greet('ram')


# def test(*args):
#     print(args)
#     print(len(args))
#     print(type(args))

# test('a','b')


# def test(**args):
#     print(args)
#     print(len(args))
#     print(type(args))

# test(Fname='vishal',Lname='mavani')

