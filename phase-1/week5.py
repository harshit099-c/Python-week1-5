# f=open("phase-1/sample.txt","w") #opening file in read mode
# # data=f.read() #reading file content using read()
# # print(type(data))
# # data_lines=f.readline()
# # print(data_lines)

# f.write("New line added")
# f.close()

# #file operation modes

# # r-read , w-write , a-append , r+- read and write , w+- write and read , a+- append and read
# f=open("phase-1/sample.txt","a")
# f.write("\n New line appended")
# f.close()

# # f=open("phase-1/sample3.txt","x") #create new file
# # f.write("new file created for writing")
# # f.close()

# #r+mode
# f=open("phase-1/sample2.txt","r+")
# f.write(" adding new line in read and write mode \n")
# f.seek(0) #move cursor to starting position
# data=f.read()
# print(data)
# f.close()

# #a+ mode
# f=open("phase-1/sample2.txt","a+")

# f.write(" \n New line added using a+ mode ")
# f.seek(0)
# print(f.read())
# f.close()

# #w+mode
# f=open("phase-1/sample2.txt","w+")
# f.write("New line added using w+ mode")
# f.seek(0)
# print(f.read())
# f.close()

# #with keyword
# with open("phase-1/sample3.txt","r") as f:
#    print(f.read())
# with open("phase-1/sample3.txt","w") as f:
#    f.write("overwriting file content using with")  

# #delete files
# import os   
# os.remove("phase-1/sample.txt")

# #practce question
# #1)word search 
def word_search(file_name,word):
   with open(f"phase-1/{file_name}","r") as f:
      data=f.read()
      if word in data:
         print("FOund")
      else:
         print("not Found")

word_search("sample2.txt","apna")                   

#2) line where the word is present
def word_line(file_name,word):
   with open(f"phase-1/{file_name}","r") as f:
      line=1
      while True:
         data=f.readline()
         if word in data:
            print(f"word found at line {line}")
            break
         line+=1 

word_line("sample2.txt","apna")       

#Exception handling
try:
   x=int(input("Enter Num: "))
   ans=10/x
except ZeroDivisionError:
   print("Can't divide by zero")
except ValueError:
   print("Invalid input")   
else: 
   print(ans)      

finally:
   print("End of program")

#list comprehension
sq=[i**2 for i in range(6) if i%2==0]
print(sq)

list_no=[1,2,-3,7,-3,8]
list_no=[0 if i<0 else i for i in list_no]
print(list_no)

list_str={"Harshit","Ankit","Harshit"}
list_str=[i.upper() for i in list_str]
print(list_str)

#json module
with open("phase-1/sample.json","w") as f:
    import json
    data = {
       "name":"Harshit",
       "student":True,
       "address":{
           "city":"Panipat",
           "country":"india"
       },
       "subjects":["Python","Java","JS"]
    }
    loaded=json.dump(data,f) #writing json data to file where dump() means write
    print(type(loaded))
with open("phase-1/sample.json","r") as f:
   import json
   data=json.loads(f.read())  #loading json data from file where loads() means read
   print(type(data))    


with open("phase-1/sample.json","r") as f:
   data=json.loads(f.read())
   data["New_data"]="Added using append mode"

with open("phase-1/sample.json","w") as f:
   json.dump(data,f,indent=4,sort_keys=True) #sort_keys use to sort keys in alphabetical order

#assignment questions
#Q-1
with open("phase-1/names.txt","w") as f:
   f.write("Harshit\nAnkit\nDeepak\nSumit\nRohit")
   f.close()

with open("phase-1/names.txt","r") as f:
   data=f.read()
   print(data)      

#Q-2
with open("phase-1/logs.txt","w") as f:
   f.write("Error:File not found\nWarning:Low disk space\nInfo:Update completed\nError:Access denied")
   f.close()
with open("phase-1/logs.txt","a") as f:
   f.write("\n Program run successfully")
   f.close()
with open("phase-1/logs.txt","r") as f:
   data=f.read()
   print(data)   

#Q-3
list_no=[5,10,15,20,25]
new_list=[i if i>15 else None for i in list_no]  
no_none_list=[i for i in list_no if i>15]
print(new_list) 
print(no_none_list)

#Q-4
try:
   with open("phase-1/data.txt","r") as f:
      data=f.read()
      print(data)
except FileNotFoundError:
   print("File Doesn't Exists")  

#Q-5
with open("phase-1/cities.json","w") as f:
   import json
   cities={
      "Delhi":12000000,
      "Mumbai":30000000,
      "Haryana":13000000
   }

   json.dump(cities,f,indent=4)

with open("phase-1/cities.json","r") as f:
   data=json.load(f)
   print(data)   
n=int(input("Enter no of cities"))
for i in range(n) :
   new_city=input("Enter city name: ")
   new_pop=int(input("Enter new population"))
   data[new_city]=new_pop
   

with open("phase-1/cities.json","w") as f:
   json.dump(data,f,indent=4,sort_keys=True)
      

