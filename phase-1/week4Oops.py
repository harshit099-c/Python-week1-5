#class and object creation
class Student :
  subject ="Python"
  college="PQR"
  year="4TH year"
  PI=3.1
  
  def __init__(self,name,cgpa,percentage,total_marks):  #self parameter means it is storing current object
    self.name=name         #object attribute
    self.cgpa=cgpa
    self.PI=3.14
    self.percentage=(percentage/total_marks)*100

  def get_cgpa(self):
    return self.cgpa


stud1=Student("Harshit",7.3,int(input("Enter marks")),int(input("Enter total marks")))
print(stud1.name,stud1.cgpa,stud1.percentage)  
print(stud1.subject)
print(stud1.get_cgpa())
print(stud1.PI)  #object attribute has more priority than class attribute

#instance method
class Laptop :
  storage_type="ssd"

  def __init__(self,RAM,storage) :
    self.RAM=RAM
    self.storage=storage

  def display(self) :
    print(f"laptop has {self.RAM}gb ram and {self.storage}gb {self.storage_type}")

l1=Laptop(16,512)
l1.display()      

#class methods access only class methods
class college:
  course="Java"

  @classmethod
  def change_course(cls,new_course): #cls used like self in instance
    cls.course=new_course
    print("inside class instance")

student=college()
student.change_course("python")
print(student.course)

#static method can't access instance and class atttributes
class stat_method():
  @staticmethod
  def calcDis(price,discount):
    final_price=price-(discount*price)/100
    return final_price
  
laptop_price=stat_method()
print(f"Final price={laptop_price.calcDis(218899,20)}")  


#practice question 
class store:
  count=0

  def __init__(self,item_name,price):
    self.item_name=item_name
    self.price=price
    store.count+=1
    
  @classmethod
  def total_products(cls):
    print(f"Total products in store={cls.count}")

  @staticmethod
  def calc_Discount(price,discount):
    final_price=price-(discount*price)/100
    print(f"Final price={final_price}")

p1=store("laptop",80000)
p1.calc_Discount(p1.price,20)       
p1.total_products()


#encapsulation wrapping data and methods in single unit
class bank_account:
  def __init__(self,name,balance):
    self.name=name          #public attribute
    self.__balance=balance  #private attribte

  def get_balance(self):    #method to access private attribute
    return self.__balance  
  
  def deposit(self,amount):
    self.__balance+=amount
  
  def withdraw(self,amount):
    if amount>self.__balance:
      print("insufficient balance")
    else:
      self.__balance-=amount  

acc1=bank_account("Harshit",70_000)
print(f"Account holder name-{acc1.name}")
acc1.deposit(40_000)    
print(f"Account balance {acc1.get_balance()}")

#inheritance  
class employee:
  start_time="8:00am"
  _end_time="5:00pm"

  @classmethod
  def change_time(cls,new_end_time):
    cls._end_time=new_end_time

class teacher(employee):

  def __init__(self,subject):
    self.subject=subject

class admin(employee):
  def __init__(self,role):
    self.role=role        

class account(admin):   #multilevel inheritance
  def __init__(self,salary,role):
    super().__init__(role) #calling parent class constructor
    self.salary=salary      


t1=teacher("Python")
staff=admin("HOD")

t1.change_time("6:00pm")
print(f"{t1.subject} class timing-{t1.start_time} to {t1._end_time}")
print(f"{staff.role} working hours-{staff.start_time} to {staff._end_time}")
acc1=account(80_000,"CA")
print(f"Accountant role-{acc1.role} with salary-{acc1.salary}")

#multiple inheritance
class Teacher :
  def __init__(self,salary):
    self.salary=salary

class student:
  def __init__(self,gpa):
    self.gpa=gpa

class ta(Teacher,student):
  def __init__(self,name,salary,gpa):
    super().__init__(salary)
    student.__init__(self,gpa)
    self.name=name

t2=ta("Harshit",50_000,8.7)
print(f"TA name-{t2.name} with salary-{t2.salary} and gpa-{t2.gpa}")      


#abstraction hiding internal details abc module in python for abstraction

from abc import ABC, abstractmethod

class animal(ABC):
  @abstractmethod
  def sound():
    pass          #Here pass means no implementation

class Lion(animal):
  def sound(self):
    print("Roar")

lion=Lion()
lion.sound()    

#polymorphism

#function overriding
class employee():
  def designation(self):
    print("Designation-Employee")

class teacher(employee):
  def designation(self):
    print("Designation-Teacher")

t1=teacher()
t1.designation()        

#duck typing
class teacher():
  def designation(self):
    print("Designation-Teacher")

class doctor():    
  def designation(self):
    print("Designation-Doctor")

def print_designation(obj):
  obj.designation()

t1=teacher()
d1=doctor()

print_designation(t1)
print_designation(d1)