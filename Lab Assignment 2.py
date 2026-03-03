                                        #Name : Muhammad Ahsan
                                        #ID   : SP25-BBD-093

#Question Number 1:
First_name = 'muhammad'
Last_name = 'ali'
Name=First_name+" "+Last_name
print(Name.title()) #Name in title case
print(Name.upper()) #Name in upper case 
print(Name.lower()) #Name in lower case
message=f"Hello {Name}, would you like to learn some Python today?"
print(message)


#Question Number 2:
#Part 1:
name='     Muhammad Ali     '
print(name.lstrip()) #Remove spaces from left side
print(name.rstrip()) #Remove spaces from left side
print(name.strip())  #Remove spaces from both left and right side
#Part 2:
name = "abcxyz Muhammad Ali"
print(name.removeprefix("abcxyz")) #remove abcxyz by using removeprefix function

#Question Number 3:
print(4+4)  #Addition
print(10-2) #Subtraction
print(2*4)  #Multiplication
print(24/3) #Division
print(17%9) #Modulus

#Question Number 4:
#Part 1:
invitees=["Ahsan","Hamza","Hassan"]
invitees.insert(0,"Talha")    #insert Talha at start  
invitees.insert(2,'kashif')   #insert Kashif at middle 
invitees.append("Zohaib")     #append zohaib at last
print(invitees)
#Part 2:
invitees.pop(3)               #pop hamza which is at index 3
del invitees [1]              #delete Ahsan which is at index 1
print(invitees)

#Question Number 5
# creating list of cities
cities=['Lahore', 'Karachi', 'islamabad', 'quetta', 'Peshawar', 'skardu', 'Muzaffarabad', 'multan', 'Gwadar']
print(cities)
# creating an empty list
cities_inv=[]
#uses for loop to populate cities_inv
for city in reversed(cities):
 cities_inv.append(city.title())
#print the result
print(cities_inv)
def f(cities):
      for city in cities[1:8]:
        print(f"The city selected is {city}")
cities_inv =['Lahore','Karachi','Islamabad','Peshawar','Quetta','Multan','Faislabad','Rawalpindi']
cities_inv.sort()
f(cities_inv)


