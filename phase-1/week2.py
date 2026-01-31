#conditionals if,elif,else
n=int(input("Enter number"))
i=int(input("Enter number"))
if n%i==0 :
    print("yes")

else : print("No") 

if n%2==0: print("even")
if n%2!=0 : print("odd")

#nesting
user=input("Enter username: ")
password=input("Enter password: ")

if user=="admin" and password=="pass" :
    print("login successfully")
else:
    if(user!="admin"):
        print("wrong username")
    else: print("Wrong password")

#match case

color=input("Enter color: ")

match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Look")
    case "Red":
        print("stop")
    case _:           #default case
        print("Wrong color")

# Loops
count=1
i=5
while (i>0):
    print(i)
    if i==2 : break
    i-=1

table=int(input("Enter number: "))
multiplier=1
while (multiplier<=10):
    print(table,"x",multiplier,"=",table*multiplier)
    multiplier+=1

#break and continue
i=5
while (i>0):
   if i==2 : break
   print(i)
   i-=1


j=0
while (j<=10) :
    if j%3==0 :
        j+=1
        continue
    print(j)
    j+=1

w=1
while(w<=10) :
    if(w%2==0) :
        w+=1
        continue
    print(w)
    w+=1    

#for loops
string="Hello"
for i in string :    #in is membership operator
    if('o' in string) :
        print("yes") 
    print(i)

for i in range(10) : #range is function of(0 to n-1)
    print(i+1)

#vowel count question
count=0
inp=input("Enter string")
for i in inp :
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count+=1
print(count)        


#range function => range(start,stop,step)
for i in range(1,10,2) :
    print(i)

for i in range(0,11,2):
    print (i)

# sum of n numbers
sum=0
num=int(input("Enter number: "))
for i in range(num+1) :
    sum+=i
print(sum)

# Functions
def first_func() :
    print("Hello")

first_func()

def sum_func(a,b) :
    return a+b

a=int(input())
b=int(input())
print(sum_func(a,b))

#avg func
def avg_func(a,b,c) :
    return (a+b+c)/3

print(avg_func(2,3,4))

#default value
def avg_func1(a,b,c=5) :
    return (a+b+c)/3

print(avg_func1(2,3))

#lambda function => single expression only like p+q+r
sum=lambda p,q,r : p+q+r
print(sum(4,5,6))

#factorial of n in recursion
def fact(n):
    if(n==0) : return 1
    return n*fact(n-1)

n=int(input("Enter number : "))
print(fact(n))

#using loops

def fact_loop(n) :
    ans=1
    for i in range(1,n+1):
        ans*=i
    return ans

print(fact_loop(n))


# assignment questions
def func1(n):
    count=0
    sum=0
    while(n>0):
        ans=n%10
        count+=1
        sum+=ans
        print(ans)
        n=int(n/10)
    print("No of digits : ",count)
    print("Sum of digits : ",sum)

n=int(input("Enter Number : "))
func1(n)       

#Q-6
for i in range(1,101) :
    if(i%3==0 and i%5==0):
        print(i)

#q-7
while True:
    i=input("Enter Number")
    print(i)
    if(i=='Quit') : break

#q-9
def prime_func(n):
    for i in range(2,n) :
        if(n%i==0) :
            return False
    return True    

print(prime_func(7))