#Midterm, Erick Cordon

#or your Midterm Project in SE126 you will be building a program of your own design! You may work in groups of up to 2 people or alone to design a program and file of your choosing.  The program must include the following:a file to be read and processed, data stored into respective lists.csv or .txt import csv will work for both of these file types, but all data must be separated with a comma! >= 2 lists these can be populated from a file or by hand showcase understanding of control flow structures showcase understanding of self-built functions Starting Documentation include a brief program description include a variable dictionary with data types including your lists! Documentation for anything used not introduced in the course Creativity!

#Varriable def:
#album = [] NAME OF ALBUMS
#rating = [] RATING FROM METACRITIC
#sales = [] CURRENT ALBUM SALES
#year = [] RELEASE DATE OF ALBUM
#cost = [] COST OF CD
#gross = [] Used to calculate gross sales
#star = [] adds a start to top rated albums
#records = 0 TOTAL TIMES 

#avgsls = sale[i]*cost[i] - Used to calculate gross sales per index

#def menu() - Used as a start menu/ gives users options on what they want to do
#def mood() - Pick a random album and generates a song based off an album


import csv
import random

#Function Def:
def menu():

    print("1. Print Original Files")
    print("2. Print Gross Album sales")
    print("3. Print Rating for ablums from METACRITIC")
    print("4. Recommend a Random Song Based Off An Album")
    print("5. Exit")

    choice = int(input("Please Select One of the following: "))

    while choice < 0 or choice > 5:
        print("*Error!*")
        choice = int(input("Please enter your selection: "))

    return choice

def mood():

    print("1. The College Dropout ")
    print("2. Late Registration")
    print("3. Graduation")
    print("4. 808s & Heartbreak")
    print("5. My Beautiful Dark Twisted Fantasy")
    print("6. Yeezus")
    print("7. The Life Of Pablo")
    print("8. Ye")
    print("9. Jesus Is King")
    print("10. Donda")
    
    choice2 = int(input("Please Select One of the following: "))

    while choice2 < 0 or choice2 > 10:
        print("*Error!*")
        choice2 = int(input("\nPlease reselect the album you would like to listen to: "))

    return choice2

#Main Code Below


album = []
rating = []
sales = []
year = []
cost = []
gross = []

records = 0

with open ("C:/Users/KTRUCHON/Desktop/SE126_202240/midterms/cordonjrerick_27735_7428860_KanyeSales.csvKanyeSales.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        records += 1

        album.append(rec[0])
        year.append(rec[1])
        sales.append(int(rec[2]))
        rating.append(int(rec[3]))
        cost.append(int(rec[4]))

for i in range(0,records):

    avgsls = sales[i]*cost[i]

    gross.append(avgsls)


pick = menu()

star = []

while pick != 5: 

    if pick == 1:
        print ("------------------------------Kanye West Album Sales OG DATA--------------------------------\n")

        print("Album                                   Date                     Sales \n")

        for i in range(0,records):
            print("{0:32}\t{1:18}\t{2:8}\t".format(album[i],year[i],sales[i]))

        print ("---------------------------------------------------------------------------------------------")

    
    if pick == 2:

        print("-------------------------------------------------------------------------------------------------------------")
        print("Album                                   Date                     Sales \t\tGross Sales")
        print("-------------------------------------------------------------------------------------------------------------")

        for i in range(0,records):
            print("{0:32}\t{1:18}\t{2:8}\t{3:0.2f}".format(album[i],year[i],sales[i],gross[i]))
        print("-------------------------------------------------------------------------------------------------------------")



    if pick == 3:

        print("-------------------------------------------------------------------------------------------------------------")
        print("Album                                   Date                     Sales \t\tScore   Star")
        print("-------------------------------------------------------------------------------------------------------------")

        for i in range(0,records):

            star_add = ""

            if rating[i] >= 78:
                star_add = "*"
            
            star.append(star_add)

            print("{0:32}\t{1:18}\t{2:8}\t {3}\t{4:5}".format(album[i],year[i],sales[i],rating[i],star[i]))

        print("\n*If an album has a star next to it, it is a top recommended album*\n")    

    if pick == 4:

        print("\nHello! Please pick one of the following albums below!")
        gen = mood()

        while gen != 11:

            if gen == 1:

                tcd = ["Intro","We Dont Care", "Graduation Day","All Falls Down","I'll Fly Away","Spaceship","Jesus Walks","Never Let Me Down","Get Em High","Workout Plan","The New Workout Plan","Slow Jamz","Breathe In Breathe Out","School Spirit Skit","School Spirit Skit 2","Lil Jimmy SKit","Two Words","Through The Wire","Family Business"]

                song = random.choice(tcd)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break
                
            if gen == 2:

                lr = ["Wake Up Mr.West","Heard 'Em Say","Touch The Sky","Gold Digger","Drive Slow","My Way Homme","Crack Music","Roses","Bring Me Down","Addiction","Diamonds From Sierra Leone","We Major","Hey Mama","Celebration","Gone","Diamonds from Sierra Leone [remix]","Late"]

                song = random.choice(lr)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break

            if gen == 3:

                g = ["Good Morning","Champion","Stronger","I Wonder","Good Life","Can't Tell Me Nothing","Barry Bonds","Drunk and Hot","Flashing Lights","Everything","The GLory","Homecoming","Big Brother"]

                song = random.choice(g)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break

            if gen == 4:

                hrtbrk = ["Say You Will","Welcome To Heartbreak","Heartless","Amazing","Love Lockdown","Paranoid","RoboCop","Street Lights","Bad News","See You In My Nightmares","Coldest Winter","Pinocchio Story"]

                song = random.choice(hrtbrk)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break

            if gen == 5:

                mbdtf = ["Dark Fantasy","Gorgeous","Power","All Of The Lights (Interlude)","All of the Lights","Monster","So Appalled","Devil In A New Dress","Runaway","Hell Of A Life","Blame Game","Lost In The World","Who Will Survive In America"]

                song = random.choice(mbdtf)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break

            if gen == 6:

                zus = ["On Sight","Skinhead","I am A God","New","Hold My Liquor","I'm In it","Blood On The Leaves","Guilt Trip","Send It Up","Bound 2"]

                song = random.choice(zus)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break

            if gen == 7:

                tlp = ["Ultralight Beam","Father Stretch My Hands","Pt.2","Famous","Feedback","Low Lights","Highlights","Freestyle 4","I Love Kanye","Waves","FML","Real Friends","Wolves","Franks track","30 Hours","No More Parties In LA","Facts","Fade","Saint Pablo"]

                song = random.choice(tlp)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break

            if gen == 8:

                ye = ["I Thought About you","Yikes","All Mines","Wouldn't Leave","No Mistakes","Ghost Town","Violent Crimes"]

                song = random.choice(ye)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break

            if gen == 9:

                jik = ["Every Hour","Selah","Follow God","Closed On Sunday","On God","Everything We Need","Water","God Is","Hands On","Use This Gospel","Jesus is Lord"]

                song = random.choice(jik)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break

            if gen == 10:

                don = ["Donda Chant","Hurricane","Moon","Life Of The Party","Off The Grid","Jail","Praise God","Come To Life","Believe What I Say","No Child Left Behind","Up From The Ashes","Remote Control Pt.2","God Breathed","Lord I Need You","24","Junya","Never Abandon Your Family","Donda","Keep My Spirit Alive","Jesus Is Lord Pt.2","Heaven And Hell","Remote Control","Tell The Vision","Jonah","Pure Souls","Ok Ok","New Again","Junya Pt. 2","Jail Pt.2","Keepy My Spirit Alive Pt.2"]

                song = random.choice(don)
                print("\n")
                print("The song we recommend you listen to today is: {}".format(song))
                print("\n")
                break


    pick = menu()

print("\nThank you for using our software. Have a good life =D!")




