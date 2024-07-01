# class INT :
#     def __init__(self,nm,ag,gn):
#         self.name = nm
#         self.age = ag
#         self.gender = gn


# st1 = INT("SWE",20,'F')

# print(st1.name,st1.age,st1.gender)

# print(type(st1))

# class STD:
#     def __init__(self):
#         self.name = None
#         self.age = None
#         self.gender = None

# st2 = STD()

# st2.name = input("Enter your Name: ")
# st2.age = int(input("Enter your age: "))
# st2.gender = input("Enter Your Gender: ")


# print(st2.name,st2.age,st2.gender)

# class STUDENT :
#     def __init__(self,a,b,c):
#         self.name = a
#         self.age = b
#         self.gender = c

# a = input("Enter your Name: ")
# b = int(input("Enter your age: "))
# c = input("Enter Your Gender: ")


# st3 = STUDENT(a,b,c)

# print(st3.name,st3.age,st3.gender)

# st3.age =21

# print(st3.name,st3.age,st3.gender)

# a =1
# b ='sdfg'
# c = 2.4
# d = ['sdg','sd',1,3]
# e = {1:"sdfg",2:"fsfdsf"}

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# st4 = INT("abc",21,'M')
# print(st4.name,st4.age,st4.gender)
# print(type(st4))

# class A:
#     def __init__(self,a,b):
#         self.A = a
#         self.__B = b
        
#     def printB(self):
#         print(self.__B)

# ob1 = A(2,5)

# print(ob1.A)
# ob1.printB()


# class Std:
#     def __init__(self): 
#         self.__USN = None
#         self.__Name = None
#         self.__Marks = []
#         self.__Percentage = None
#         self.__Grade = None

#     def Std_Input(self):
#         self.__Name = input("Enter your Name: ")
#         self.__USN = input("Enter Your USN: ")
#         for i in range (0,5):
#             marks = input(f"Enter Your Marks in Sub{i+1} : ")
#             self.__Marks.append(marks)

#     def calc_percentage (self):
#         sum = 0
#         for i in self.__Marks:
#             sum = sum + int(i)
#         self.__Percentage = (sum/500)*100

#     def calc_Grade(self):
#         per = float(self.__Percentage)
#         if per<=100 and per >=80:
#             self.__Grade = "A"
#         elif per<80 and per >=60:
#             self.__Grade = "B"
#         elif per<60 and per >=40:
#             self.__Grade = "C"
#         elif per<40 and per >=0:
#             self.__Grade = "D"
#         else: 
#             self.__Grade = "Inavlid"

#     def print_details(self):
#         print("Name: ",self.__Name)
#         print("USN : ",self.__USN)
#         print("Marks in Five Subject are :")
#         for i in range(0,5):
#             print(f"Subject {i+1} = {self.__Marks[i]}")
#         print("Percentage : ", self.__Percentage)
#         print("Grade : ", self.__Grade)



# st1 = Std()

# print(type(st1))

# st1.Std_Input()

# st1.print_details()

# st1.calc_percentage()
# st1.print_details()

# st1.calc_Grade()
# st1.print_details()

# #ENCRYPTION KEY BASED ON PRIME NUMBERS
# m = int(input("Enter the message: "))
# flag = 0
# if m<1:
#     flag = 1
# elif m == 1:
#     flag = 0
# else:
#     for i in range(2,(m//2)+1):
#         if m%i == 0:
#             flag = 1
#             break
    
# if flag == 0:
#     print("Valid Messgae")
# else:
#     print("invalid Message")

#     #fibnocci series

# n= int(input("Enter the no of terms: "))

# a=0
# b=1
# c=a+b
# if n==1:
#     print(a)
# elif n==2:
#     print(a)
#     print(b)
# else:
#     print(a)
#     print(b)
#     for i in range(2,n):
#         print(c)
#         a=b
#         b=c
#         c=a+b

        
# def check_prime(m):
#     flag = 0
#     if m<1:
#         flag = 1
#     elif m == 1:
#         flag = 0
#     else:
#         for i in range(2,(m//2)+1):
#             if m%i == 0:
#                 flag = 1
#                 break
    
#     if flag == 0:
#         return 1
#     else:
#         return 0

# result=[]
# N=int(input())
# flag=0
# k=N+1
# while flag<1:
#     flag = check_prime(k)
#     if flag == 1:
#         result.append(k)
#     else:
#         k=k+1

# sum = 0
# for i in range (N+1,k):
#     sum+=i

# result.append(sum)



# p1=k
# flag=0
# k=p1+1
# while flag<1:
#     flag = check_prime(k)
#     if flag == 1:
#         p2=k
#     else:
#         k=k+1

# p3=p1*p2
# flag=check_prime(p3)
# if flag == 0:
#     result.append(False)
# else:
#     result.append(True)

# Prime_key=tuple(result)

# print(Prime_key)




