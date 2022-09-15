#Erick Cordon Lab 6

#Prompt: Re-write the Week #5 Class Lab but instead of searching for a person’s name, search for their birthday.  If the person is found, reprint their entire record to the console.  The program should allow the user to search for as many birthdays as they want. The program should also print a statement telling the user how many iterations of the search loop the program went through before finding (or not finding) the requested person.

#Varriable Definitions:

#lastname = [] empty list for last name
#firstname = [] empty list for first name
#dob = [] empty list for date of birth
#records = 0 counting var 
#search_count = 0 counts how many searches are processed

#bday = datetime.strptime(dob[found], "%m/%d/%Y") #STUDENTS DATE AND TIME
#tday = datetime.now() CURRENT DATE AND TIME

#age = tday - bday#(todays dates - found persons birthdate) THIS IS USED TO GET AGE FROM DATETIME
#total = (age.total_seconds() /(3.141592653589793 * 10** 7)) # THIS IS TO THE TOTAL YEARS /.totalsecond converts the datetime to seconds /seconds divded by (pi * 10 to the 7th power)/

#age_total = int(total) #prevents from total rounding up 

#Main Code Below----------------------------------------
import csv
import datetime
from datetime import datetime, date, timedelta

lastname = []
firstname = []
dob = []

records = 0
search_count = 0

with open("C:/Users/Erick/Desktop/SE126_202240/w6_classlab/lab5_updated.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        records += 1

        lastname.append(rec[0])
        firstname.append(rec[1])
        dob.append(rec[2])
    
print("-------------------------------------------------------------------------------")
print("INDEX: {0} \t{1:15} \t{2:15} \t{3}".format("","Last Name","First Name","Date Of Birth"))
print("-------------------------------------------------------------------------------")

for i in range(0,records): #This prints the Original Data

    print("INDEX: {0} \t{1:15} \t{2:15} \t{3}".format(i, lastname[i].title(),firstname[i].title(),dob[i]))


answer = "y"

while answer == "y":

    search = input("Please enter the birthdate you are looking for: ")#asks for the dob 

    found = -1

    for i in range(0,records):

        search_count += 1 #adds one per every search 

        if search == dob [i]:

            found = i #This makes this an index

    print("\n\nSearch is being processed")

    if found > -1: #This is for when index is found

        print("\nPerson found ", search," at index", found) #prints the correct person's data seached if found

        print("\t\t\t{0:10} \t {1:10} \t {2:10}".format(lastname[found].title(),firstname[found].title(),dob[found])) #the found in index will only pring what is found

        #below is what i used to calulate age
        bday = datetime.strptime(dob[found], "%m/%d/%Y") #Seperates the persons birthday by month/day/year
        tday = datetime.now()

        age = tday - bday#(todays dates - found persons birthdate)
        total = (age.total_seconds() /(3.141592653589793 * 10** 7)) # .totalsecond converts the datetime to seconds /seconds divded by (pi * 10 to the 7th power)/

        age_total = int(total) #prevents from total rounding up 

        print("\nThe student is : {0:2.0f} years old".format(age_total))


    else: #this is for errors
        print("Your search for ", search, "has NOT BEEN FOUND")
        print("Please check for any errors")

    print("\nTotal Loops Perfromed for search: {}".format(search_count))

    search_count = 0 #this resets the search count after being used in the varriable

    answer = input("\nHey, would you like to add another person? [y/n]: ")
    answer = answer.lower() #This allows the user to type answer with caps lock

    while answer != "y" and answer != "n": # mis-input loop
        print("**Error**")
        answer = input("\n\nWould you like to add another person? [y/n]: ").lower()
        answer = answer.lower()

print("\n\nThank you for using our program =D")



