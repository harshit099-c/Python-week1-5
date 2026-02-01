word='python'
print(len(word)) #len gives length of string
print('I Love '+ word) #concatenation

#indexes
print(word[3])

#slicing (starting to end-1) range
print(word[2:4])
print(word[2:])
print(word[-4:])

#string Formatting
a=10
b=15
sum=a+b
print("sum of {} and {} is : {}".format(a,b,sum))

#index based formatting
print("sum of {1} and {0} is : {2}".format(a,b,sum))

#f-strings
print(f"sum of {a} and {b} is {sum}")


#lists
marks=[99,83,67,24,84]
print(marks)
print(len(marks))
print(marks[len(marks)-1])

marks[3]=85 #update
print(marks)

#slicing on lists
print(marks[2:5]) 
print(marks[-3:-1])

#methods in lists
marks.append(92) #insert at last
marks.insert(2,87) # insert at any position
marks.sort()
print(marks,len(marks))
marks.reverse()
print(marks)

idx=0
for i in marks :
  if (i!=84) :
    idx+=1
  else:
    print(idx)
    break

#binary search
marks.sort()
x=99
low=0
high=len(marks)-1
while low<=high:
  mid=int((low+high)/2)
  if(marks[mid]==x):
    print(mid) 
    break
  elif(marks[mid]>x):
    high=mid-1
  else : 
    low=mid+1 


#tuples
tup=(1,2,3,4,5)
print(type(tup),type(marks))
print(tup[-3:])

sum=0
for i in tup :
  sum+=i
print(f"sum of {tup} is : {sum}")  

#methods of tuples
print(tup.index(3)) #first index of value
print(tup.count(3)) #no of values in tuples


#dictionary key:value pairs

info={
  "name" : "Harshit",
  "cgpa": 7.3,
  "subject": ["maths","physics"],
  3.14:"PI"
}


print(len(info))
print(type(info))
print(info["name"])
info["subject"][0]="History" #update in dictionary
info["subject"].append("Chemistry")
print(info["subject"])

#methods of dictionary
#print keys
print(info.keys())
#values
print(info.values())

#key:values
print(info.items())

#get func takes key
print(info.get(9)) #wrong key it gives none
print(info.get("cgpa"))

#update =>insert new item

info.update({
  "city" : "Panipat"
})


print(info["city"])
 #loops in dictionary
for key,value in info.items() :
  if(value=="Harshit"):
    print(key)
    
#sets only unique elements

my_set={1,2,2,3,3,4}
print(my_set)
print(type(my_set))
print(len(my_set))

#methods
my_set.add(5) #insert new element
print(my_set)

my_set.remove(1) #removes an element but raises error if not found
print(my_set)

popped=my_set.pop() #removes any element
print(my_set,popped)

my_set.clear() #removes all element
print(my_set)

a={1,2,3}
b={4,5,6}

c=a.union(b) #union of sets
d=a.intersection(b) #intersection of sets
print(a,b,c,d)

#practice questions
list_tuple=[
      ("Harshit","Maths"),
      ("Hitesh","SST"),
      ("Rohan","chem"),
      ("Rajat","IT"),
      ("Rohit","IT"),
      ("Hiten","IT")
]

unique_courses=set()
for tup in list_tuple : #tup will have tuple of size 2 in every iteration
  unique_courses.add(tup[1])

print(unique_courses)  

for tup in list_tuple :
  if tup[1]=="IT":
    print(tup[0])

new_dict={}
for name,course in list_tuple :
   if(new_dict.get(name)==None):
    new_dict.update({name: set()})
    new_dict[name].add(course)
   else : 
    new_dict[name].add(course) 

print(new_dict)    


#assignment questions
#1) palindrome
string=input("Enter string")
n=len(string)
idx=0
for i in string :
    if(i!=string[n-1-idx]):
      print("No")
    idx+=1
    if idx==n-1 : print("Yes")

 #2)
list1=list(map(int,input("Enter list1").split()))
list2=list(map(int,input("Enter list2").split()))

merge_list=list1+list2
merge_list.sort()
sets=set(merge_list)
print(merge_list)
print(sets)

list3=list(map(str,input("Enter strings").split()))
list4=list(map(str,input("Enter strings").split()))
merge_list2=list3 + list4
print(" ".join(merge_list2))

#3)
tup1=tuple(map(int,input("Enter no").split()))
tup_even=()
tup_odd=()
for i in tup1 :
  if(i%2==0):
    tup_even=tup_even+(i,)
  else: tup_odd=tup_odd+(i,)  
print(tup_even,tup_odd)  

#4)
diction={}

def add():
  key=input("Enter name")
  value=int(input("Enter Marks"))
  diction[key]=value

def update():
  inp=input("Enter student name")
  if(diction.get(inp)==None):
    print("Not Found")
  else :
    new_marks=int(input('Enter new marks'))
    diction[inp]=new_marks    

def search():
  val=input("Enter student name")
  if(diction[val]==None):
    print("not found")
  else :
    print(f"{val} is found with marks {diction[val]}")     

def display():
  for key,value in diction.items():
    print(f"{key} : {value}")    

while True:
  user=input("Enter choice")
  if user=="A":
    add()
  elif user=="U":
    update()    
  elif user=="S":
    search()
  elif user=="D":
    display()   
  else : break  


#Q6
list_words=list(map(str,input("Enter words").split()))
word_dict={}

for i in list_words :
  key=i
  value=len(i)
  word_dict[key]=value

print(word_dict)

# Q-9
repeat_list=list(map(int,input("Enter marks").split()))
repeated=[]

for i in range(1,len(repeat_list)) :
  if repeat_list[i] == repeat_list[i-1] :
    if(repeat_list not in repeated):
      repeated.append(repeat_list[i])

print(repeated)

#Q-10
user_str=input("Enter string")
length=len(user_str)
unique_string= set(user_str)
print(unique_string)
print(len(unique_string))