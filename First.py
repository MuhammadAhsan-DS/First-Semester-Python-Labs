# Name : Muhammad Ahsan
# Reg.No.  : SP25-BBD-093

#Question Number : 1
#Variable to represent a perons First and Lastname
Firstname="Muhammad"
Lastname="Ahsan"
print(Firstname)
print(Lastname)
#Combine first and last variable in another variable Name
Name=Firstname+" "+Lastname
print(Name)
#print Name in lower,upper and title case
print("Lowercase:",Name.lower())
print("Uppercase:",Name.upper())
print("Titlecase:",Name.title())
#Use of f string to print message
message=(f"Assalam-o-Alaikum,{Name}!I hope that you are doing well")
print(message)

# Question Number 2
Name= "     Xeven Solution    "

print (Name.lstrip())
print(Name.rstrip())
print(Name.strip())
#Remove xyzabc by using removeprefixmethod
name = 'xyzabc Xeven Solution' 
Name= name.removeprefix("xyzabc")
print(Name)

# Question Number 3
print(6+2)     #Addition
print(12-4)    #Subtration
print(4*2)     #Multiplication
print(24/3)    #Division
print(17%9)    #Modulus


# Question number 4
invitees=["Faiz","Usman","Bilal"]
print(invitees)
#Use insert function to add new person to the beginning of list
invitees.insert(0,"Kashif")
print(invitees)
# Use insert fuction to add new person to the middle of list
middle_index=len(invitees)
invitees.insert(middle_index,"Talha")
print(invitees)
#Use append funtion to add member to the end of list
invitees.append("Saim")
print(invitees)
# Use pop function to remove one person from your list
invitees.pop(0)
print(invitees)
#Use del funtion to rmove gust at index 1
del invitees[1]
print(invitees)

# question Number 5
Cities=['Lahore','Karachi','Islamabad','Quetta','Peshawar','Skardu','Muzaffarabad','Multan','Gwadar']
print(Cities)
