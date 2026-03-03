                                        #Name : Muhammad Ahsan
                                        #ID   : SP25-BBD-093

#Question Number 1:
First_name = 'muhammad'
Last_name = 'ali'
Name=First_name+" "+Last_name
print(Name.title()) #Name in title case
print(Name.upper()) #Name in upper case 
print(Name.lower()) #Name in lower case

#Question Number 2:
#Part 1:
name='    Muhammad Ali    '
print(name.rstrip()) #Remove spaces from left side
print(name.lstrip()) #Remove spaces from left side
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

#Question Number 5:
cities=['Lahore', 'Karachi', 'islamabad', 'quetta',
        'Peshawar', 'skardu', 'Muzaffarabad',
        'multan', 'Gwadar']

cities_inv=[]

for city in cities:
    cities_inv.insert(0, city.title())

cities_inv.sort()

for city in cities_inv:
    print(f"The city selected is: {city}")