print("hello world","with python") 
age=20
print('type of age',type(age))

# style guide

total_price=20
total_price2=10
print(total_price+total_price2)

#operators +,-,/,*,%,(**) this is for power

a=10
b=5
print(a%b)
print(a**b) # a raise to power b

# realtional operator ==,!=,>,<,>=,<=
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
 
#assignment operator =,+=,-=,*=,/=,%=,**=
a-=b
a**=b
print (a)
b+=a
b%=a
print(b)

#logical operator not,and,or

ans=False
print(not ans)

print((5>2) and (6<9))
print((5>2) or (6<9))

#operator precedence (),**,(*,/,%),(+,-),relational operator,not,and,or precedence in decreasing order
# same precedence then left to right

# type conversion
r=9
print(b/b) # implicit type conversion by python

# explicit type conversion or casting
p=8.2
q=9.5
ans=int(p*q)
print(type(ans),type(p),type(q))

str=float('123.7')
print (str)

#user input

a=float(input("Enter number 1: "))
b=int(input("Enter number 2: "))

print(a+b)

#avg of 2numbers
p=int(input("Enter number"))
q=int(input("Enter number"))

print(((p+q)/200)*100,"%")


# assignment q1
print("question1")
tem=input("Enter temp in C")
C=float(tem)
farh=(9/5)*C+32
print(farh)

#q2
num=45.78
intNum=int(num)
fraction=num-intNum
print("integer part: ",intNum,"\n fractional part: .",int(fraction*100),sep="")