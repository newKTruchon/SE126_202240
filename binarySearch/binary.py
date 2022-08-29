import csv

id = []
name = []
age = []
color = []

records = 0 

with open("C:/Users/KTRUCHON/Desktop/SE126_202240/sequentialSearch/binary.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        id.append(rec[0])
        name.append(rec[1].lower())
        age.append(rec[2])
        color.append(rec[3].lower())

print("Finished processing file. There are {} records".format(records))

answer = "y"

while answer == "y":

    search_count = 0

    #REQUEST SEARCH PARAMTER(S)
    
    search = input("Enter the full LAST NAME of the record you are looking for: ").lower()
    found = -1 #found is -1 because this is NOT a valid index
    #SEQUENTIAL SEARCHING LOOP
    print("STARTING SEQUENTIAL SEARCH--------------")
    for i in range(0, records):
        print("\t\tSEQUENTIAL SEARCH!")

        search_count += 1 #count how many iterations of loop search performs

        #"SEARCH" through list items for requested info
        if search == name[i]:

            #every time above condition is true, we will display to the user all of the info
            #print("INDEX: {0} \t {1:10} \t {2:10} \t {3:10} \t {4:10}".format(i, id[i], name[i], age[i], color[i]))

            found = i

        #else:
            #print("Your search for '", search, "' was NOT FOUND.")
    
    print("\n\nSEQUENTIAL SEARCH COMPLETE.")

    if found >= 0:
        print("Your search for '", search, "' was FOUND on INDEX {}.".format(found))
        print("INDEX: {0} \t {1:10} \t {2:10} \t {3:10} \t {4:10}".format(found, id[found], name[found], age[found], color[found]))

    else:
        print("Your search for '", search, "' was NOT FOUND.")


    print("Search Loop Iterations Performed: {}".format(search_count))

    print("STARTING BINARY SEARCH-------------")
    #search = input("Get search from user! Enter LAST name: ").lower()

    min = 0

    max = records - 1       #can also use len(listName) for 'records' value

    guess = int((min + max) / 2)

    #this is for INCREASING order

    search_count = 0

    while (min < max and search != name[guess]):
        print("\t\tBINARY SEARCH!")

        search_count += 1

        if search < name[guess]:

            max = guess - 1

        else:

            min = guess + 1

        guess = int((min + max) / 2)

    if search == name[guess]:

        #found them! use 'guess' for index of found search item
        print("Your search for {} was FOUND at index: {}".format(search, guess))

    else:

        #boooo not found
        print("Your search for {} was NOT FOUND".format(search))

    print("BINARY SEARCH LOOPS: {}".format(search_count))

    answer = input("search again? [y/n]: ").lower()
