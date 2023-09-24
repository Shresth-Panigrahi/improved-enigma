import pymysql as py
from Connection import *

#ADD OF TRAIN INFO
def Rail_Info():
    while True:
        while True:
            TNO = input("Enter Train Number: ")
            s = 0
            c = 0
            Cur.execute("use dummy")
            Cur.execute("select Train_Number from train_info")
            A = Cur.fetchall()
            for I in A:
                if I == int(TNO):
                    print(I)
                    print(" TRAIN NUMBER ALREADY EXISTS ")
                    print(" PLEASE RE-ENTER ")
                    continue  
            if len(TNO) == 0:
                print("Cannot be blank ")
                continue
            for J in TNO:
                if J in ' ':
                    s +=1
            if s > 0:
                c = 1
            if TNO[-1] == ' ' or TNO[0] == ' ':
                c = 1
            for K in TNO:
                if K.isalpha() == True:
                    c = 1
                    break
            if c == 1:
                print(" RE-ENTER TRAIN NUMBER ")
            else:
                TNO = int(TNO)
                break
        while True:
            TNAME = input("Enter Train Name: ")
            f = 0
            sp = 0
            if len(TNAME) == 0:
                print("Cannot be blank ")
                continue
            for i in TNAME:
                if i == ' ':
                    sp +=1
            if sp > 3:
                f = 1
            if TNAME[-1] == ' ' or TNAME[0] == ' ':
                f = 1
            for I in TNAME:
                if I.isalpha()!= True and I != " " :
                    f = 1
                    break
            if f == 1:
                print(" RE-ENTER TRAIN NAME ")
            else:
                break
        while True:
            TSOURCE = input("Enter Train Source: ")
            f = 0
            sp = 0
            if len(TSOURCE) == 0:
                    print("Cannot be blank ")
                    continue
            for i in TSOURCE:
                if i in ' ':
                    sp +=1
            if sp > 4:
                f = 1
            if TSOURCE[-1] == ' ' or TSOURCE[0] == ' ':
                f = 1
            for I in TSOURCE:
                if I.isalpha() == False and I != ' ':
                    f = 1
                    break
            if f == 1:
                print(" RE-ENTER TRAIN SOURCE ")
            else:
                break
        while True:
            TDESTINATION = input("Enter Train Destination: ")
            f = 0
            sp = 0
            if len(TDESTINATION) == 0:
                    print("Cannot be blank ")
                    continue
            for i in TDESTINATION:
                if i in ' ':
                    sp +=1
            if sp > 4:
                f = 1
            if TDESTINATION[-1] == ' ' or TDESTINATION[0] == ' ':
                f = 1
            for I in TDESTINATION:
                if I.isalpha() == False and I != ' ':
                    f = 1
                    break
            if f == 1:
                print(" RE-ENTER TRAIN DESTINATION ")
            else:
                break
        while True:
            FARE = input("Enter Base Fare: ")
            s = 0
            c = 0
            if len(FARE) == 0:
                print("Cannot be blank ")
                continue
            for J in FARE:
                if J in ' ':
                    s +=1
            if s > 0:
                c = 1
            if FARE[-1] == ' ' or FARE[0] == ' ':
                c = 1
            for K in FARE:
                if K.isalpha() == True:
                    c = 1
                    break
            if c == 1:
                print(" RE-ENTER TRAIN NUMBER ")
            else:
                FARE = int(FARE)
                break
        Cur.execute("use dummy")
        Cur.execute(F"insert into train_info values({TNO}, '{TNAME}', '{TSOURCE}', '{TDESTINATION}', {FARE})")
        X = input("Do you wish to add more train information (y/n): ")
        if X in "yY":
            continue
        elif X in "nN" or X == "no" or X == "No" or X == "NO":
            Conn.commit()
            break

#DATE VALIDATION 
def Date_Validation():
    while True:
        while True:
            Y = int(input("Enter Year: "))
            if len(str(Y)) != 4:
                print(" RE-ENTER YEAR ")
                continue
            elif Y < 2023:
                print(" YEAR ALREADY CROSSED ")
                print(" PLEASE RE-ENTER ")
                continue
            elif Y > 2023:
                print(" TOO EARLY BOOKING ")
                print(" PLEASE RE-ENTER ")
            else:
                break
        while True:
            print("+"*38)
            print("+"*38)
            print("++----------------------------------++")
            print("++ Month                Your Input  ++")
            print("++----------------------------------++")
            print("++ January         |              1 ++")
            print("++ February        |              2 ++")
            print("++ March           |              3 ++")
            print("++ April           |              4 ++")
            print("++ May             |              5 ++")
            print("++ June            |              6 ++")
            print("++----------------------------------++")
            print("+"*38)
            print("+"*38)
            M = input("Enter Month of travel: ")
            if len(M) != 1:
                print(" RE-ENTER MONTH: ")
                continue
            else:
                break
        while True:
            D = input("Enter Date of travel: ")
            if M == "1" or M == "3" or M == "5":
                if int(D) > 31:
                    print(" PLEASE RE-ENTER DATE ")
                    continue
            elif M == "4" or M == "6":
                if int(D) > 30:
                    print(" PLEASE RE-ENTER DATE ")
                    continue
            elif M == "2":
                if int(D) > 28:
                    print(" PLEASE RE-ENTER DATE ")
                    continue
            break
        K = str(Y) + '/' + str(M) + '/' + (D)
        break
    return K
    
#PASSENGER DETAILS AND PNR GENERATION
def Rail_Booking(): 
    while True:
        global PNR
        global O
        global P
        global PRICE
        R = Date_Validation()
        print(F"Your Date of Travel will be : {R}")
        while True:
            Cur.execute("use dummy")
            L = input("Do you wish to see Train Info (y/n): ")
            if L == "YES" or L == "yes" or L == "y" or L == "Y":
                Cur.execute("use dummy")
                Cur.execute("select * from train_info")
                S = Cur.fetchall()
                print("="*101)
                print(F"{'TRAIN NUMBER':<13}{'TRAIN NAME':^18}{'SOURCE':^23}{'DESTINATION':^24}{'BASE FARE':^26}")
                print("="*101)
                for i in S:
                    print(F"{str(i[0]):^13}{i[1]:^18}{i[2]:^23}{i[3]:^24}{str(i[4]):^26}")
                    print("="*101)
            G = input("Enter the Train Number: ")
            if G.isalpha() == False and G != ' ': #If User Inputs Train Number
                Cur.execute("select Train_Number from train_info")
                Q = Cur.fetchall()
                q = []
                for I in Q:
                    for J in I:
                        q.append(J)
                for i in q:
                    if i == int(G):
                        G = int(G)
                        Cur.execute(F"select Train_Name from train_info where Train_Number = {G}")
                        V = Cur.fetchall()
                        for i in V:
                            for j in i:
                                O = j
                                P = G
                                print(F"Your Train Number is: {G} and your Train Name is: {O}")
                                break
            elif G.isalpha() == True and G != ' ': #If User Inputs Train Name
                Cur.execute("select Train_Name from train_info")
                Y = Cur.fetchall()
                y = []
                for i in Y:
                    for j in i:
                        y.append(j)
                for I in y:
                    if I == G:
                        Cur.execute(F"select Train_Number from train_info where Train_Name = '{G}'")
                        W = Cur.fetchall()
                        for i in W:
                            for j in i:
                                P = j
                                O = G
                                print(F"Your Train Number is: {P} and your Train Name is: {G}")
                                break
            else:
                print(" INVALID INPUT ")
                print(" PLEASE RE-ENTER ")
                continue
            break
        while True:
            NAME = input("Enter Name of Passenger: ")
            f = 0
            sp = 0
            if len(NAME) == 0:
                print("Cannot be blank ")
                continue
            for i in NAME:
                if i in ' ':
                    sp +=1
            if sp > 4:
                f = 1
            if NAME[-1] == ' ' or NAME[0] == ' ':
                f = 1
            for I in NAME:
                if I.isalpha() == False and I != ' ':
                    f = 1
                    break
            if f == 1:
                print(" RE-ENTER PASSENGER NAME ")
            else:
                break
        while True:
            AGE = input("Enter the age of Passenger: ")
            s = 0
            c = 0
            if len(AGE) == 0:
                print("Cannot be blank ")
                continue
            for J in AGE:
                if J in ' ':
                    s +=1
            if s > 0:
                c = 1
            if AGE[-1] == ' ' or AGE[0] == ' ':
                c = 1
            for K in AGE:
                if K.isalpha() == True:
                    c = 1
                    break
            if c == 1:
                print(" RE-ENTER AGE ")
            else:
                AGE = int(AGE)
                break
        while True:
            GENDER = input("Enter the Gender: ")
            f = 0
            sp = 0
            if len(GENDER) == 0:
                print("Cannot be blank ")
                continue
            for i in GENDER:
                if i in ' ':
                    sp +=1
            if sp > 3:
                f = 1
            if GENDER[-1] == ' ' or GENDER[0] == ' ':
                f = 1
            for I in GENDER:
                if I.isalpha() == False:
                    f = 1
                    break
            if f == 1:
                print(" RE-ENTER PASSENGER GENDER ")
            else:
                break
        while True:
            print("+==================================================+")
            print("+  Class       |    Price in INR    |  Your Input  +")
            print("+--------------------------------------------------+")
            print("+  General     |   20% of Base Fare |      G       +")
            print("+--------------------------------------------------+")
            print("+  Sleeper     |      Base Fare     |      S       +")
            print("+--------------------------------------------------+")
            print("+  3rd AC      |   Base Fare + 800  |      3       +")
            print("+--------------------------------------------------+")
            print("+  2nd AC      |   Base Fare + 1200 |      2       +")
            print("+--------------------------------------------------+")
            print("+  1st AC      |   Base Fare + 1700 |      1       +")
            print("+--------------------------------------------------+")
            print("+==================================================+")
            CLASS = input("Which Class would you like to travel: ")
            F = 0
            if CLASS not in "GS321":
                print(" INVALID INPUT ")
                print(" PLEASE RE-ENTER ")
                continue
            Cur.execute("use dummy")
            Cur.execute(F"select Base_Fare from train_info where Train_Number = {G}")
            D = Cur.fetchall()
            for i in D:
                for j in i:
                    D = j
            if CLASS == 'G':
                F = 'General'
                if AGE < 6:
                    PRICE = 0
                if AGE > 6 and AGE < 61:
                    PRICE = D * 0.2
                if AGE > 60:
                    PRICE = (D * 0.5)*0.2
            elif CLASS == 'S':
                F = 'Sleeper'
                if AGE < 6:
                    PRICE = 0
                if AGE > 6 and AGE < 61:
                    PRICE = D 
                if AGE > 60:
                    PRICE = D * 0.2
            elif CLASS == '3':
                F = '3rd AC'
                if AGE < 6:
                    PRICE = 0
                if AGE > 6 and AGE < 61:
                    PRICE = D + 800
                if AGE > 60:
                    PRICE = (D + 800)* 0.5
            elif CLASS == '2':
                F = '2nd AC'
                if AGE < 6:
                    PRICE = 0
                if AGE > 6 and AGE < 61:
                    PRICE = D + 1200
                if AGE > 60:
                    PRICE = (D + 1200)*0.5
            elif CLASS == '1':
                F = '1st AC'
                if AGE < 6:
                    PRICE = 0
                if AGE > 6 and AGE < 61:
                    PRICE = D + 1700
                if AGE > 60:
                    PRICE = (D + 1700)*0.5
            break
        Cur.execute("use dummy")
        Cur.execute("select * from painfo")
        X = Cur.fetchall()
        if X == ():
            PNR = 1
            print(F"You PNR is: {PNR}")
        else:
            PNR = X[-1][0] + 1
            print(F"You PNR is: {PNR}")
        print(F"Your Price would be: {PRICE}")
        Cur.execute(F"insert into painfo values({PNR}, '{NAME}', {AGE}, '{GENDER}', '{F}', '{R}', '{O}', '{P}', {PRICE})")
        X = input("Do you wish to add more passenger details (y/n): ")
        if X in "yY":
            continue
        elif X in "nN" or X == "no" or X == "No" or X == "NO":
            Conn.commit()
            break  

#PNR ENQUIRY
def PNR_Enquiry():
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    P = int(input("Enter your PNR: "))
    Cur.execute("use dummy")
    Cur.execute(F"select Name from painfo where PNR = {P}")
    A = Cur.fetchall()
    for i in A:
        for j in i:
            a = j
    Cur.execute(F"select Age from painfo where PNR = {P}")
    B = Cur.fetchall()
    for i in B:
        for j in i:
            b = j
    Cur.execute(F"select Gender from painfo where PNR = {P}")
    C = Cur.fetchall()
    for i in C:
        for j in i:
            c = j
    Cur.execute(F"select Class from painfo where PNR = {P}")
    D = Cur.fetchall()
    for i in D:
        for j in i:
            d = j
    Cur.execute(F"select Date_of_Travel from painfo where PNR = {P}")
    E = Cur.fetchall()
    for i in E:
        for j in i:
            e = j
    Cur.execute(F"select Train_Number from painfo where PNR = {P}")
    F = Cur.fetchall()
    for i in F:
        for j in i:
            f = j
    Cur.execute(F"select Train_Name from painfo where PNR = {P}")
    G = Cur.fetchall()
    for i in G:
        for j in i:
            g = j
    Cur.execute(F"select Journey_Cost from painfo where PNR = {P}")
    h = Cur.fetchall()
    for i in h:
        for j in i:
            h = j
    print("+++++++++++++++++++++++++++++++++++++++++")
    print("+=======================================+")
    print("+       [{    TICKET INFO    }]         +")
    print("+=======================================+")
    print(F"+ Name: {a}  Age: {b}  Gender: {c}     +")
    print("+---------------------------------------+")
    print(F"+     Class: {d}  Date: {e}            +")
    print("+---------------------------------------+")
    print(F"+ Train Number: {f}  Train Name: {g}   +")
    print("+---------------------------------------+")
    print(F"+        Journey Cost: {h}             +")
    print("+---------------------------------------+")
    print("+++++++++++++++++++++++++++++++++++++++++")
    
#START CODE   
PNR = 0     #Global Variable PNR Set
O = 0
P = 0
PRICE = 0
while True:
    print("++++++++++++++++++++++++++++++")
    print("+|==========================|+")
    print("+|==========================|+")
    print("+|         Main Menu        |+")
    print("+|==========================|+")
    print("+|==========================|+")
    print("+|    Select your choice    |+")
    print("+|==========================|+")
    print("+|    1.) ADD TRAIN INFO    |+")
    print("+|    2.) TRAIN INFO        |+")
    print("+|    3.) TICKET FARES      |+")
    print("+|    4.) BOOKING           |+")
    print("+|    5.) PNR ENQUIRY       |+")
    print("+|    6.) EXIT              |+")
    print("+|==========================|+")
    print("+|==========================|+")
    print("++++++++++++++++++++++++++++++")
    choice = input("Enter your choice: ")
    if choice == '1':
        Rail_Info()
    elif choice == '2':
        Cur.execute("use dummy")
        Cur.execute("select * from train_info")
        S = Cur.fetchall()
        print("="*101)
        print(F"{'TRAIN NUMBER':<13}{'TRAIN NAME':^18}{'SOURCE':^23}{'DESTINATION':^24}{'BASE FARE':^26}")
        print("="*101)
        for i in S:
            print(F"{str(i[0]):^13}{i[1]:^18}{i[2]:^23}{i[3]:^24}{str(i[4]):^26}")
        print("="*101)
    elif choice == '3':
        print("__________________________________________________________")
        print("|****************|***********|***************|***********|")
        print("|    Category    |  Age Gap  |   Base Fare   |   Class   |")
        print("|----------------|-----------|---------------|-----------|")
        print("|     Infant     |   0 - 5   |      Free     |  Sleeper  |")
        print("|----------------|-----------|---------------|-----------|")
        print("|     Adult      |   6 - 60  |  Full Ticket  |  Sleeper  |")
        print("|----------------|-----------|---------------|-----------|")
        print("| Senior Citizen |  Age > 60 |  Half Ticket  |  Sleeper  |")
        print("|----------------|-----------|---------------|-----------|")
        print("|****************|***********|***************|***********|")
        print("__________________________________________________________")
    elif choice == '4':
        Rail_Booking()
    elif choice == '5':
        PNR_Enquiry()
    elif choice == '6':
        print("+"*34)
        print("+ THANK YOU FOR ENGAGING WITH US +")
        print("+"*34)
        break
    else:
        print(" INVALID CHOICE ")
        print(" PLEASE RE-ENTER ")
        continue
    A = input("Do you wish to continue (y/n): ")
    if A in "nN" or A == "no" or A == "No" or A == "NO":
        print("+"*34)
        print("+ THANK YOU FOR ENGAGING WITH US +")
        print("+"*34)
        break
