import csv

records = 0 
overCount = 0

#intiialize empty lists
roomNames = []
maximums = []
attending = [] 
difference = []

print("\n-----ROOM NAME---------------MAX CAP----ATT-----OVER----------")
with open("C:/Users/KTRUCHON/Desktop/SE126_202240/lab2a/lab2a.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file: 

        records += 1

        room = rec[0]
        maxCap = int(rec[1])
        pplAtt = int(rec[2])

        diff = maxCap - pplAtt 

        #add values to lists 
        roomNames.append(room)
        maximums.append(maxCap)
        attending.append(pplAtt)
        difference.append(diff)

#process list data 

for i in range(2, len(roomNames)):
    if difference[i] < 0 :
        print("{0:25}\t{1}\t{2}\t{3}".format(roomNames[i], maximums[i], attending[i], difference[i] * -1))
        overCount += 1


total_seats = 0 
for i in range(0, records):
    total_seats += maximums[i]



print("\n\nROOMS OVER CAPACITY: ", overCount)
print("TOTAL RECORDS: ", records)
print("TOTAL SEATS: ", total_seats)