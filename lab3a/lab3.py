import csv 

records = 0 

#prepare empty lists - one for EVERY POSSIBLE field in the file
device = []
brand = []
cpu = []
ram = [] 
first_disk = []
num_hdd = []
second_disk = []
os = []
yr = []


#connect to and open file------------------------------------------------------
with open("C:/Users/KTRUCHON/Desktop/SE126_202240/lab3a/lab3a.csv") as csvfile: 

    file = csv.reader(csvfile)

    for rec in file: 

        records += 1
        #print(rec)

        #add data from file to lists - .append() 
        device.append(rec[0])
        brand.append(rec[1])
        cpu.append(rec[2])
        ram.append(rec[3])
        first_disk.append(rec[4])
        num_hdd.append(rec[5])


        if rec[5] == "1":
            second_disk.append("-none-")
            os.append(rec[6])
            yr.append(rec[7])

        else:
            second_disk.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])




#closed file ------------------------------------------------------------------

#process the lists to print the data to the screen
print("\n\tORIGINAL FILE DATA----------------------------------------------")

for index in range(0, records):

    print("INDEX#{9}:\t{0:8}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}".format(device[index], brand[index], cpu[index], ram[index], first_disk[index], num_hdd[index], second_disk[index], os[index], yr[index], index))

print("\t---------------------------------------------------------------")
print("\n\n\tTOTAL RECORDS: ", records)

#process to print desktop/laptop + brand name
print("\n\tUPDATED FILE DATA----------------------------------------------")

for index in range(0, records):

    if device[index] == "D":
        #change to desktop
        device[index] = "Desktop"
    
    elif device[index] == "L":

        device[index] = "Laptop"

    #change brands


    print("INDEX#{9}:\t{0:8}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}".format(device[index], brand[index], cpu[index], ram[index], first_disk[index], num_hdd[index], second_disk[index], os[index], yr[index], index))

print("\t---------------------------------------------------------------")

#prepare counting variables 
ram8 = 0 
ram16 = 0
#process the lists to determine the number of 8 rams and 16 rams
for i in range(0, records):

    if ram[i] == "08":

        ram8 += 1

    elif ram[i] == "16":

        ram16 += 1

    else:

        print("*ERROR* encountered at index {}".format(i))

print("\n\tTHERE ARE {0} 8GB RAM DEVICES / {1} 16GB RAM DEVICES".format(ram8, ram16))
