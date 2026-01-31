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