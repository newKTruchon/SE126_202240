import csv 

fName = []
lName = []
dob = [] 


with open("C:/Users/KTRUCHON/Desktop/SE126_202240/lab5_ages/lab5_updated.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file : 

        fName.append(rec[0])
        lName.append(rec[1])
        dob.append(rec[2])

month = []
day = []
year = []

today_month = 9
today_day = 12
today_year = 2022

#find each person's month/day/year
for i in range(0, len(dob)):

    dob_list = dob[i].split("/")

    month.append(int(dob_list[0]))
    day.append(int(dob_list[1]))
    year.append(int(dob_list[2]))

for i in range(0, len(dob)):

    print("{0:15}\t{1:15}\tDOB: {2:8}\tM:{3:5}\tD:{4:5}\tY:{5:5}".format(fName[i], lName[i], dob[i], month[i], day[i], year[i]))

ages = []

for i in range(0, len(dob)):

    if month[i] < today_month:
        #birthday has occurred 
        age = today_year - year[i]

        if day[i] < today_day:
            age = age 

        else: 
            age -= 1 

    ages.append(age)

for i in range(0, len(dob)):

    print("{0:15}\t{1:15}\tDOB: {2:8}\tM:{3:5}\tD:{4:5}\tY:{5:5}\t AGE:{6}".format(fName[i], lName[i], dob[i], month[i], day[i], year[i], ages[i]))

