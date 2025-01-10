print(" ________________________________________________________")
print("|         WELCOME TO ENGINEERING COLLAGE                 |")
print("|________________________________________________________|")

a=str(input("PLEASE ENTER YOUR NAME : "))
print(f"Hii, {a}")
b=int(input("ENTER YOUR PERCENTAGE PROVISIONAL YEAR : "))

if b>=70:
    print("YOU ARE ABLE TO ADDMISSION..")

    print(" ________________________________________________________")
    print("|                  ENGINEERING BRANCHES                  |")
    print("|________________________________________________________|")
    print("| (0) AIDS                                               |")
    print("| (1) COMPUTER SCIENCE                                   |")
    print("| (2) CIVIL ENGINEERING                                  |")
    print("| (3) ELECTORNICS                                        |")
    print("| (4) MECHANICAL ENGINEERING                             |")
    print("|________________________________________________________|")
    d=int(input("SELECT YOUR BRANCH : "))
    e=['AIDS', 'COMPUTER SCIENCE', 'CIVIL ENGINEERING', 'ELECTORNICS', 'MECHANICAL ENGINEERING'  ]
    if d==0:
        print("|            ARTIFICIAL INTALLIGENCE (SUBJECT)           |")
        print("|________________________________________________________|")
        print("| (0) COMPUTER ARCHITECTURE                              |")
        print("| (1) AI                                                 |")
        print("| (2) DATA STRUCUTURE                                    |")
        print("| (3) M-III                                              |")
        print("| (4) DIGITAL LOGIC AND SERQUITS                         |")
        print("|________________________________________________________|")
        print("")
        print("")
        print(" ________________________________________________________")
        print("|                   PAYMENT STATUS                       |")
        print("|                                                        |")
        print("|                                   (Y)yes      (N)no    |")
        print("|________________________________________________________|")
        g=str(input("PAYMENT STATUS : "))
        i = 'Y'
        j = 'N'
        if g==i:
            print(" ________________________________________________________")
            print("|                 ADMISSION RECIPT                         |")
            print("|_________________________________________________________|")
            print(f"|NAME : {a}                                               ")
            print(f'BRANCH: {e[d]}                                            ')
            print (f'PAYMENT STETUS : {g}                                     ')
            print("|_________________________________________________________|")
            j = str(input("PLEASE CONFORMATION YOUR ADDMISSION (Y)yes (N)no : "))
            x='Y'
            y='N'
            if j==x:
                print(" _________________________________________________________")
                print("|   ADDMISSION IS SUCCESSFULLY DONE PLEASE CHECK EMAIL   |")
                print("|_________________________________________________________|")
            elif j==y:
                print(" _________________________________________________________")
                print("|            YOUR ADDMISSION IS CANCELLED                 |")
                print("|_________________________________________________________|")







        elif g==j:
            print(" _________________________________________________________")
            print("|   YOUR ADDIMISSION IS INCOMPLETE PLEASE PAY PAYMENT     |")
            print("|_________________________________________________________|")
















else:
    print("SORRY,YOU ARE NOT ABLE TO ADDMISSION")







