import os

data = []
guestLimit = 0
enterInfo = """ Wedding guest menu
			1) Guest Name Press '1'
			2) Add a Guest press '2'
			3) Delete Guest Name '3'

			if you have any questions call '555-5555'

			"""
guestName = input("Please enter the name of the guest: ")
guestAge = input("Please enter the age of the guest: ")
data.append(guestName)
data.append(guestAge)

if guestLimit < 100:
            print("your guest name is ", guestName, "your guest age is ", guestAge)
while True:
    print(enterInfo)
    choice = input("ENTER A FOLLOWING CHOICE: ")
    if choice == "1":
        print(data)
    elif choice == "2":
        guestName = input("Please enter the name of the guest: ")
        guestAge = input("Please enter the age of the guest: ")
        data.append(guestName)
        data.append(guestAge)
    elif choice == "3":
        guestName = input("Please enter the name of the guest: ")
        guestAge = input("Please enter the age of the guest: ")
        data.remove(guestName)
        data.remove(guestAge)
choice = input("ENTER A FOLLOWING CHOICE: ")





        
		

