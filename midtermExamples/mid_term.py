# Nathan Tandon 

# Midterm 

# 8/20/2021

# Intermediate Python 

# Program Prompt: This Program will read a csv file to display to the user which constellations are visible by season depending on user choice. 

# Variable Dictionary : 

# file -> Variable used for csvfile
# choice -> int -> Represents user choice in menu function  
# tot_rec -> int -> Total records 
# answer -> string -> Used to control while loop
# anual[] -> Used to store anual constellation data in list 
# winter[] -> Used to store winter constellation data in list
# spring[] -> Used to store spring constellation data in list
# summer[] -> Used to store summer constellation data in list
# fall[] -> Used to store fall constellation data in list

# Note : Had a hard week and didnt get to make the code I really wanted to make. Hopefully this small code will suffice though. 

# Functions------------------------------------------------------

def menu(): # Menu Function

    print("\n          Menu\n")
    print("1. Circumpolar Constellations")
    print("2. Winter Constellations")
    print("3. Spring Constellations")
    print("4. Summer Constellations")
    print("5. Fall Constellations")
    print('6. Exit\n')

    choice = int(input("\nEnter your choice [1-6]: ")) # User Choice 

    while choice < 1 or choice > 6 : # It's a Trap! 

        print("\nError")
    
        choice = int(input("\nEnter your choice [1-6]: \n"))
    
    return choice

def bye(): # Goodbye Function  

    print("\nThank you for using this service :)\n")

# List Setup -----------------------------------------------------

import csv # Import Library

tot_rec = 0 

anual = []  # Set up list
winter = []
spring = []
summer = []
fall = []

with open("midtermExamples/constellation.csv") as csvfile: 

    file = csv.reader(csvfile)

    for rec in file: 

        tot_rec += 1

        anual.append(rec[0])  # Append List 
        winter.append(rec[1])
        spring.append(rec[2])
        summer.append(rec[3])
        fall.append(rec[4])

# Main Code------------------------------------------------------

answer = "Y"

while answer.upper() == "Y" : 

    choice = menu()

    for i in range(0, tot_rec) : # For loop

        if choice == 1 : 

            print("\n", anual[i])

        if choice == 2: 

            print("\n", winter[i])

        if choice == 3: 

            print("\n", spring[i])

        if choice == 4: 

            print("\n", summer[i])

        if choice == 5 : 

            print("\n", fall[i])

        if choice == 6 : 

            answer = "x"

bye() # Goodbye Function 
#---------------------------------------------------------------