#Stephanie Nagel 
#SE 126.02
#Lab Midterm
#8/22/2021

#PROGRAM PROMPT: This program will display to a user astrological zodiac sign information. It will take data from a CSV file and store them into lists. The file is then reprocessed by sign name to append spirit colors for each sign. It then enteres a loop allowing the user to enter as many birthdays as they wish until responding "no" to the function prompt of checking another. It uses 2 more functions to ask a user to enter a birth month (by number) then a birth day (by nymber) to determine the correct zodiac sign. The functions return the month and day to the main code where it will allow processing for each of the 12 signs by month number. The month numbers are then separated by day numbers to fall into the correct sign. The user will then see a display of the selected signs name, date range, element, symbol, stone, ruling planet, spirit color and a small description of personality traits. 

#VARIABLE DICTONARY:
#VAR NAME       VAR TYPE    VAR DESCRIPTION
#--------       --------    --------------------------------------------------------------------
#records        var         number of records in file 
#csvfile        csv         csv to be imported to utilze stored data 
#file           var         stored csv
#month          function    ask user a birth month and return answer to the main executing code 
#day            function    ask user a birth day and return answer to the main executing code
#another        function    ask user if they would like to check another birthday
#b_month        input       user is asked to input their birth month as a number 1-12
#b_day          input       user is asked to input their birth day as a number 1-31
#birth_month    var         returned and stored value from month() function
#birth_day      var         returned and stored value from day() function
#answer         input       *LOOP KEY* returns and stores value from another() function
#sign           list        rec[0] name of zodiac sign
#date_range     list        rec[1] date range the zodiac falls under 
#element        list        rec[2] element associated with zodiac sign (earth, air, fire, water)
#symbol         list        rec[3] symbol for the zodiac sign
#stone          list        rec[4] stone associated with the zodiac sign
#ruling_planet  list        rec[5] ruling planet associated with the zodiac sign
#about          list        rec[6] type of person each zodiac sign is typically associated with 
#spirit_color   list        added data (color) from reprocessing list  
#color          data        appened to spirit_color list after re-running file
#cap            file data   capricorn data stored in list at index 0
#aqua           file data   Aquarius data stored in list at index 1
#pisces         file data   Pisces data stored in list at index 2
#aries          file data   Aries data stored in list at index 3
#taur           file data   Taurus data stored in list at index 4
#gem            file data   Gemini data stored in list at index 5
#cancer         file data   Cancer data stored in list at index 6
#leo            file data   Leo data stored in list at index 7
#virgo          file data   Virgo data stored in list at index 8
#libra          file data   Libra data stored in list at index 9
#scor           file data   Scorpio data stored in list at index 10
#sag            file data   Sagittarius data stored in list at index 11


#------IMPORTS--------------------------------------------------------------------
import csv

#------FUNCTIONS------------------------------------------------------------------
def month():#asks user to enter birth month as number, ensures choice is valid, returns birth_month
    '''asks user to enter birth month as number, ensures choice is valid, returns birth_month''' 
    
    #asks for birth month
    b_month = int(input("\n\nSelect the birth month by number:\n\t1)  January\n\t2)  February\n\t3)  March\n\t4)  April\n\t5)  May\n\t6)  June\n\t7)  July\n\t8)  August\n\t9)  September\n\t10) October\n\t11) November\n\t12) December\n\n\t\tBirth month [1-12]: "))

    #catches user if they enter a number greater than 12 or a string value
    while b_month > 12:

        print("\n\t\t**********ERROR ERROR**********")
        b_month = int(input("\nSelect the birth month by number:\n\t1)  January\n\t2)  February\n\t3)  March\n\t4)  April\n\t5)  May\n\t6)  June\n\t7)  July\n\t8)  August\n\t9)  September\n\t10) October\n\t11) November\n\t12) December\n\n\t\tBirth month [1-12]: "))
    
    return b_month

def day():#asks user to enter birth day as number, ensures choice is valid, returns birth_day
    '''asks user to enter birth month and birth day both as numbers, ensures choice is valid, returns birth_month and birth_day'''
    #asks for birth day
    b_day = int(input("\nEnter the day of birth as a number [1-31]: "))

    #catches user if they enter a number greater than 31 or a string value
    while b_day > 31:

        print("\n\t\t**********ERROR ERROR**********")
        b_day = int(input("\nEnter the day of birth as a number [1-31]: "))

    #returns both the month and day selected by the user 
    return b_day

def another():

    answer = input("\n\nWould you like to check another birthday? [y/n]: ")
    answer = answer.lower()

    while answer != "y" and answer != "n":
        answer = input("\n\nWould you like to check another birthday? [y/n]: ")
        answer = answer.lower()
    
    return answer


#------MAIN EXECUTING CODE--------------------------------------------------------
records = 0

sign = []
date_range = []
element = []
symbol = []
stone = []
ruling_planet = []
about = []
spirit_color = []


with open ("midtermExamples/midterm_csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #print(rec)

        records += 1

        sign.append(rec[0])
        date_range.append(rec[1])
        element.append(rec[2])
        symbol.append(rec[3])
        stone.append(rec[4])
        ruling_planet.append(rec[5])
        about.append(rec[6])

#print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}".format("SIGN", "DATE RANGE", "ELEMENT", "SYMBOL", "STONE", "RULING PLANET"))
#print("-----------------------------------------------------------------------")

#for i in range(0,records):

    #print("\n{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}\n   {6}".format(sign[i], date_range[i], element[i], symbol[i], stone[i], ruling_planet[i], about[i]))

#-----FILE CLOSED-------------------------------------------------------------------

#---------------RE-PROCESS FILE ADDING LUCKY DAYS-----------------------------------

for i in range(0, records):

    if sign[i] == "Capricorn":
        color = "Dark blue"
    elif sign[i] == "Aquarius":
        color = "Sky blue"
    elif sign[i] == "Pisces":
        color = "Sea green"
    elif sign[i] == "Aries":
        color = "Red"
    elif sign[i] == "Taurus":
        color = "Pink"
    elif sign[i] == "Gemini":
        color = "Yellow"
    elif sign[i] == "Cancer":
        color = "Violet"
    elif sign[i] == "Leo":
        color = "Gold"
    elif sign[i] == "Virgo":
        color = "Silver"
    elif sign[i] == "Libra":
        color = "Blue"
    elif sign[i] == "Scorpio":
        color = "Black"
    else:
        color = "Light Blue"

    spirit_color.append(color)

#all file data stored in the lists found at each index is now represented by these
cap = 0
aqua = 1
pisces = 2
aries = 3
taur = 4
gem = 5
cancer = 6
leo = 7
virgo = 8
libra = 9
scor = 10
sag = 11

print("\nWelcome to the Zodiac Birthday Information Checker\n\n***    Please enter your dates as requested    ***")

answer = "y"

#entering loop 
while answer == "y":

    birth_month = month() #calls funtion and stores returned value

    birth_day = day() #calls function and stores returned value 

    #HEADER
    print("\n{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{6}".format("SIGN", "DATE RANGE", "ELEMENT", "SYMBOL", "STONE", "RULING PLANET", "SPIRIT COLOR"))
    print("------------------------------------------------------------------------------------------")

    #JANUARY BIRTHDAYS-------------------------------------
    if birth_month == 1:

        if birth_day <= 19: #Capricorn

            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[cap], date_range[cap], element[cap], symbol[cap], stone[cap], ruling_planet[cap], about[cap], spirit_color[cap]))    

        elif birth_day >= 20: #Aquarius
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[aqua], date_range[aqua], element[aqua], symbol[aqua], stone[aqua], ruling_planet[aqua], about[aqua], spirit_color[aqua]))

    
    #FEBRUARY BIRTHDAYS-------------------------------------
    if birth_month == 2:

        if birth_day <= 18: #Aquarius
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[aqua], date_range[aqua], element[aqua], symbol[aqua], stone[aqua], ruling_planet[aqua], about[aqua], spirit_color[aqua]))

        elif birth_day >= 19: #Pisces
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[pisces], date_range[pisces], element[pisces], symbol[pisces], stone[pisces], ruling_planet[pisces], about[pisces], spirit_color[pisces]))

    
    #MARCH BIRTHDAYS-----------------------------------
    if birth_month == 3:

        if birth_day <= 20: #Pisces
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[pisces], date_range[pisces], element[pisces], symbol[pisces], stone[pisces], ruling_planet[pisces], about[pisces], spirit_color[pisces]))

        elif birth_day >= 21: #Aries
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[aries], date_range[aries], element[aries], symbol[aries], stone[aries], ruling_planet[aries], about[aries], spirit_color[aries]))


    #APRIL BIRTHDAYS-----------------------------------
    if birth_month == 4:

        if birth_day <= 19: #Aries
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[aries], date_range[aries], element[aries], symbol[aries], stone[aries], ruling_planet[aries], about[aries], spirit_color[aries]))

        elif birth_day >= 20: #Taurus
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[taur], date_range[taur], element[taur], symbol[taur], stone[taur], ruling_planet[taur], about[taur], spirit_color[taur]))
    
    #MAY BIRTHDAYS-------------------------------------
    if birth_month == 5:

        if birth_day <= 20: #Taurus
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[taur], date_range[taur], element[taur], symbol[taur], stone[taur], ruling_planet[taur], about[taur], spirit_color[taur]))

        elif birth_day >= 21: #Gemini
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[gem], date_range[gem], element[gem], symbol[gem], stone[gem], ruling_planet[gem], about[gem], spirit_color[gem]))
    
    #JUNE BIRTHDAYS-------------------------------------
    if birth_month == 6:

        if birth_day <= 20: #Gemini
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[gem], date_range[gem], element[gem], symbol[gem], stone[gem], ruling_planet[gem], about[gem], spirit_color[gem]))

        elif birth_day >= 21: #Cancer
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[cancer], date_range[cancer], element[cancer], symbol[cancer], stone[cancer], ruling_planet[cancer], about[cancer], spirit_color[cancer]))
    
    #JULY BIRTHDAYS-------------------------------------
    if birth_month == 7:

        if birth_day <= 22: #Cancer
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[cancer], date_range[cancer], element[cancer], symbol[cancer], stone[cancer], ruling_planet[cancer], about[cancer], spirit_color[cancer]))

        elif birth_day >= 23: #Leo
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[leo], date_range[leo], element[leo], symbol[leo], stone[leo], ruling_planet[leo], about[leo], spirit_color[leo]))

    #AUGUST BIRTHDAYS-------------------------------------
    if birth_month == 8:

        if birth_day <= 22: #Leo
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[leo], date_range[leo], element[leo], symbol[leo], stone[leo], ruling_planet[leo], about[leo], spirit_color[leo]))

        elif birth_day >= 23: #Virgo
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[virgo], date_range[virgo], element[virgo], symbol[virgo], stone[virgo], ruling_planet[virgo], about[virgo], spirit_color[virgo]))

    #SEPTEMBER BIRTHDAYS-------------------------------------
    if birth_month == 9:

        if birth_day <= 22: #Virgo
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[virgo], date_range[virgo], element[virgo], symbol[virgo], stone[virgo], ruling_planet[virgo], about[virgo], spirit_color[virgo]))

        elif birth_day >= 23: #Libra
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[libra], date_range[libra], element[libra], symbol[libra], stone[libra], ruling_planet[libra], about[libra], spirit_color[libra]))

    #OCTOBER BIRTHDAYS-------------------------------------
    if birth_month == 10:

        if birth_day <= 22: #Libra
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[libra], date_range[libra], element[libra], symbol[libra], stone[libra], ruling_planet[libra], about[libra], spirit_color[libra]))

        elif birth_day >= 23: #Scorpio
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[scor], date_range[scor], element[scor], symbol[scor], stone[scor], ruling_planet[scor], about[scor], spirit_color[scor]))

    #NOVEMBER BIRTHDAYS-------------------------------------
    if birth_month == 11:

        if birth_day <= 21: #Scorpio
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[scor], date_range[scor], element[scor], symbol[scor], stone[scor], ruling_planet[scor], about[scor], spirit_color[scor]))

        elif birth_day >= 22: #Sagittarius
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[sag], date_range[sag], element[sag], symbol[sag], stone[sag], ruling_planet[sag], about[sag], spirit_color[sag]))

    #DECEMBER BIRTHDAYS-------------------------------------
    if birth_month == 12:

        if birth_day <= 21: #Sagittarius
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[sag], date_range[sag], element[sag], symbol[sag], stone[sag], ruling_planet[sag], about[sag], spirit_color[sag]))

        elif birth_day >= 22: #Capricorn
            
            print("{0:13}{1:13}{2:9}{3:10}{4:12}{5:20}{7}\n\n   {6}".format(sign[cap], date_range[cap], element[cap], symbol[cap], stone[cap], ruling_planet[cap], about[cap], spirit_color[cap]))
    
    answer = another()

print("\nThank you for using my program\n\t\t~~~Goodbye~~~\n\n")