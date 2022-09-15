import csv 

records = 0 

lastname = []
firstname = []
age = []

with open("C:/Users/KTRUCHON/Desktop/SE126_202240/bubbleSort/GOT_bubble_sort.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        records += 1


        lastname.append(rec[0])
        firstname.append(rec[1])
        age.append(int(rec[2]))

for i in range(0, records):
    print("{0:15}\t{1:15}\t{2:5}".format(lastname[i], firstname[i], age[i]))


answer = "y"

while answer == "y":

    print("\tSEARCH OPTIONS")
    print("1. Search for multiples of 1 name [LASTNAME]")
    print("2. Search for unique name [FIRSTNAME]")
    print("3. EXIT")

    choice = input("Enter which you would like to do [1-3]: ")

    while choice != "1" and choice != "2" and choice != "3":
        print("\t\t**ERORR** INVALID ENTRY!")
        choice = input("Enter which you would like to do [1-3]: ")

    #SEQUENTIAL SEARCH------------------
    if choice == "1":

        print("\n\t\t~SEQUENTIAL SEARCH~")

        search = input("Enter the LASTNAME of the person/people you are looking for: ").lower()
        search = search2.lower()

        found = []
        f = -1

        for i in range(0, records):

            if search == lastname[i].lower():

                found.append(i) #stores index of found last name to the found list
                f = i

        if f >= 0:

            print("\t\tYour SEQUENTIAL SEARCH results for ", search2, ": ")

            for i in range(0, len(found)):
                print("INDEX: {3}\t{0:15}\t{1:15}\t{2:5}".format(lastname[found[i]], firstname[found[i]], age[found[i]], found[i]))

        else: 
            print("\t\tYour SEQUENTIAL SEARCH results for ", search, "could NOT BE FOUND. ")
            print("Please cHeCk YoUr SpElLiNg and try again :]")

    if choice == "2": 
    #BUBBLE SORT - REQUIRED for BINARY SEARCH! Must happen first :D

        for i in range(0, records - 1):#outter loop

            #print("OUTER LOOP! i = ", i)

            for index in range(0, records - 1):#inner loop

                #print("\t INNER LOOP! k = ", index)

                #below if statement determines the sort

                #list used is the list being sorted

                # > is for increasing order, < for decreasing

                if(firstname[index] > firstname[index + 1]):

                    #print("\t\t SWAP! ", firstname[index], "<-->", firstname[index + 1])

                    #if above is true, swap places!
                    temp = firstname[index]
                    firstname[index] = firstname[index + 1]
                    firstname[index + 1] = temp
        
                    #swap all other values

                    temp = age[index]
                    age[index] = age[index + 1]
                    age[index + 1] = temp


                    temp = lastname[index]
                    lastname[index] = lastname[index + 1]
                    lastname[index + 1] = temp


        for i in range(0, records):
            print("{0:15}\t{1:15}\t{2:5}".format(lastname[i], firstname[i], age[i]))



    #BINARY SEARCH----------------------
        print("\n\t\t~BINARY SEARCH~")

        search2 = input("Enter the FIRSTNAME of the person you are looking for: ")
        search = search2.lower()

        min = 0                      #this is the lowest starting INDEX
        max = records - 1            #the highest starting INDEX
        guess = int((min + max) / 2)  #or: guess = (min + max) // 2  -> starting MIDDLE index

        while min < max and search != firstname[guess].lower():

            if search < firstname[guess].lower(): #this is for ASCENDING ORDER LISTS

                max = guess - 1

            else: 

                min = guess + 1

            guess = int((min + max) / 2)

        if search == firstname[guess].lower():

            print("\t\tYour SEQUENTIAL SEARCH results for ", search2, ": ")

            print("INDEX: {3}\t{0:15}\t{1:15}\t{2:5}".format(lastname[guess], firstname[guess], age[guess], guess))

        else: 
            print("\t\tYour SEQUENTIAL SEARCH results for ", search2, "could NOT BE FOUND. ")
            print("Please cHeCk YoUr SpElLiNg and try again :]")


    #EXIT------------------------------
    if choice == "3":
        print("\t\tYou have chosen to EXIT")
    else:
        answer = input("\nWould you like to search again? [y/n]: ").lower()

        while answer != "n" and answer != "y":
            print("\t\t**ERORR** INVALID ENTRY!")
            answer = input("Would you like to search again? [y/n]: ").lower()



