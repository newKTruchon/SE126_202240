import csv

records = 0 

#header 
print("\nDATA FROM FILE--------------------------------------------------------------")
print("{0:8}   {1:8}   {2}   {3}   {4}   {5}   {6}   {7}   {8}".format("TYPE", "BRAND", "CPU", "RAM", "DISC 1", "NUM DISCS", "DISC 2", "OS", "YEAR"))
print("------------------------------------------------------------------------------")
with open("C:/Users/KTRUCHON/Desktop/SE126_202240/lab2b/lab2b.csv") as csvfile: 

    file = csv.reader(csvfile)

    for rec in file: #one record at a time
        #entire code block applies to ONE record ...at a time

        records += 1

        type_ = rec[0]
        manu = rec[1]
        cpu = rec[2]
        ram = rec[3]
        first_disc = rec[4]
        num_disc = rec[5]

        #fields below change per record
        second_disc = "" 
        os = ""
        year = "" 

        if type_ == "D":
            type_ = "Desktop"

        elif type_ == "L":
            type_ = "Laptop"

        else: 
            #error in file check 
            #point = records - 1
            type_ = "ERROR @ row " + str(records)

        if num_disc == "1":
            #no second disk
            os = rec[6]
            year = rec[7]
            second_disc = "---"

        #what happens when there are two disks?
        else: 
            second_disc = rec[6]
            os = rec[7]
            year = rec[8]

        print("{0:8}   {1:8}   {2}     {3:3}   {4:6}     {5:9}     {6:6}   {7:2}   {8:4}".format(type_, manu, cpu, ram, first_disc, num_disc, second_disc, os, year))
print("-------------------------------------------------------------------------------")

print("\n\nRECORDS: {0}".format(records))