print(" ______________________________________________________________")
print("|                   WELLCOME TO SCHOOL                         |")
print(" ______________________________________________________________")

a=str(input("PLEASE ENTER YOUR FULL NAME :- "))

print(f"Hii, {a}")
s=int(input("ENTER YOUR AGE :- "))
if s==6:

        print(" ______________________________________________________________")
        print("|                            MEDIUMS                           |")
        print(" ______________________________________________________________")
        print("|  (0)  ENGLISH MEDIUM        |   FEES - 15,000 RUPEES         |")
        print("|  (1)  MARATHI MEDIUM        |   FEES - N/A                   |")
        print("|_____________________________|________________________________|")
        c = ['ENGLISH MEDIUM', 'MARATHI MEDIUM']

        b = int(input("PLEASE SELECT YOUR MEDIUM :- "))

        if b == 0:
            print(F"YOUR SELECTED MEDIUM {c[b]}")
            print("YOUR FEES IS :- 15,000 RUPEES")
            print(" ______________________________________________________")
            print("|                  PAYMENT STETUS                      |")
            print(" ______________________________________________________")
            print("|                                                      |")
            print("|                                  (Y)yes     (N)no    |")
            print("|______________________________________________________|")
            g = 'Y', 'y'
            h = 'N', 'n'
            i = str(input(""))
            if i in g:
                print("______________________________________________________")
                print("|                  ADMISION RECEPT                   |")
                print("______________________________________________________")
                print(F"| NAME          : {a}                                         ")
                print(f"| MEDIUM        : {c[b]}                                      ")
                print(f"| CLASS         : NURSERY/BALVADI                                   ")
                print("|PAYMENT STATUS :  Y                                           ")
                print("|____________________________________________________|")
                print(" ______________________________________________________")
                print("|                  ADMISSION CONFORMATION              |")
                print(" ______________________________________________________")
                print("|                                                      |")
                print("|                                  (Y)yes     (N)no    |")
                print("|______________________________________________________|")
                p = 'y', 'Y'
                q = 'n', 'N'
                r = str(input(""))
                if r in p:
                    print("__________________________________________________")
                    print("|   ADDMISION IS SUCCESSFULLY DONE CHECK EMAIL   |")
                    print("|________________________________________________|")
                elif r in q:
                    print("__________________________________________________")
                    print("|           ADDMISION IS CANCELLED               |")
                    print("|________________________________________________|")

            elif i in h:
                print(" _____________________________________________________")
                print("|YOUR ADDMISION IS CANCELLED,BECAUSE YOUR NOT PAY FEES|")
                print("|_____________________________________________________|")
            else:
                print("PLEASE CAUSE CORRECT KEY")
        elif b == 1:
            print(F"YOUR SELECTED MEDIUM {c[b]}")
            print("______________________________________________________")
            print("|                  ADMISION RECEPT                   |")
            print("______________________________________________________")
            print(F"| NAME          : {a}                                         ")
            print(f"| MEDIUM        : {c[b]}                                      ")
            print(f"| CLASS         : NURSERY/BALVADI                                    ")
            print("|PAYMENT STATUS :  N/A                                           ")
            print("|____________________________________________________|")
            print(" ______________________________________________________")
            print("|                  ADMISSION CONFORMATION              |")
            print(" ______________________________________________________")
            print("|                                                      |")
            print("|                                  (Y)yes     (N)no    |")
            print("|______________________________________________________|")
            p = 'y', 'Y'
            q = 'n', 'N'
            r = str(input(""))
            if r in p:
                print("__________________________________________________")
                print("|   ADDMISION IS SUCCESSFULLY DONE CHECK EMAIL   |")
                print("|________________________________________________|")
            elif r in q:
                print("__________________________________________________")
                print("|           ADDMISION IS CANCELLED               |")
                print("|________________________________________________|")


elif s==7:
    d = str(input('PLEASE ENTER YOUR GRADE IN PREVIOUS STRANDERD :- '))
    e = 'A', 'a'
    f = 'B', 'b'
    if d in e or d in f:
        gradea: bool = True
        print("YOU ARE ALIGIBLE FOR SCHOOL")
        print(" ______________________________________________________________")
        print("|                            MEDIUMS                           |")
        print(" ______________________________________________________________")
        print("|  (0)  ENGLISH MEDIUM        |   FEES - 15,000 RUPEES         |")
        print("|  (1)  MARATHI MEDIUM        |   FEES - N/A                   |")
        print("|_____________________________|________________________________|")
        c = ['ENGLISH MEDIUM', 'MARATHI MEDIUM']

        b = int(input("PLEASE SELECT YOUR MEDIUM :- "))

        if b == 0:
            print(F"YOUR SELECTED MEDIUM {c[b]}")
            print("YOUR FEES IS :- 15,000 RUPEES")
            print(" ______________________________________________________")
            print("|                  PAYMENT STETUS                      |")
            print(" ______________________________________________________")
            print("|                                                      |")
            print("|                                  (Y)yes     (N)no    |")
            print("|______________________________________________________|")
            g = 'Y', 'y'
            h = 'N', 'n'
            i = str(input(""))
            if i in g:
                print("______________________________________________________")
                print("|                  ADMISION RECEPT                   |")
                print("______________________________________________________")
                print(F"| NAME          : {a}                                         ")
                print(f"| MEDIUM        : {c[b]}                                      ")
                print(f"| CLASS         : 1st                                    ")
                print("|PAYMENT STATUS :  Y                                           ")
                print("|____________________________________________________|")
                print(" ______________________________________________________")
                print("|                  ADMISSION CONFORMATION              |")
                print(" ______________________________________________________")
                print("|                                                      |")
                print("|                                  (Y)yes     (N)no    |")
                print("|______________________________________________________|")
                p = 'y', 'Y'
                q = 'n', 'N'
                r = str(input(""))
                if r in p:
                    print("__________________________________________________")
                    print("|   ADDMISION IS SUCCESSFULLY DONE CHECK EMAIL   |")
                    print("|________________________________________________|")
                elif r in q:
                    print("__________________________________________________")
                    print("|           ADDMISION IS CANCELLED               |")
                    print("|________________________________________________|")

            elif i in h:
                print(" _____________________________________________________")
                print("|YOUR ADDMISION IS CANCELLED,BECAUSE YOUR NOT PAY FEES|")
                print("|_____________________________________________________|")
            else:
                print("PLEASE CAUSE CORRECT KEY")
        elif b == 1:
            print(F"YOUR SELECTED MEDIUM {c[b]}")
            print("______________________________________________________")
            print("|                  ADMISION RECEPT                   |")
            print("______________________________________________________")
            print(F"| NAME          : {a}                                         ")
            print(f"| MEDIUM        : {c[b]}                                      ")
            print(f"| CLASS         : 1st                                   ")
            print("|PAYMENT STATUS :  N/A                                           ")
            print("|____________________________________________________|")
            print(" ______________________________________________________")
            print("|                  ADMISSION CONFORMATION              |")
            print(" ______________________________________________________")
            print("|                                                      |")
            print("|                                  (Y)yes     (N)no    |")
            print("|______________________________________________________|")
            p = 'y', 'Y'
            q = 'n', 'N'
            r = str(input(""))
            if r in p:
                print("__________________________________________________")
                print("|   ADDMISION IS SUCCESSFULLY DONE CHECK EMAIL   |")
                print("|________________________________________________|")
            elif r in q:
                print("__________________________________________________")
                print("|           ADDMISION IS CANCELLED               |")
                print("|________________________________________________|")
elif s==8:
    d = str(input('PLEASE ENTER YOUR GRADE IN PREVIOUS STRANDERD :- '))
    e = 'A', 'a'
    f = 'B', 'b'
    if d in e or d in f:
        gradea: bool = True
        print("YOU ARE ALIGIBLE FOR SCHOOL")
        print(" ______________________________________________________________")
        print("|                            MEDIUMS                           |")
        print(" ______________________________________________________________")
        print("|  (0)  ENGLISH MEDIUM        |   FEES - 15,000 RUPEES         |")
        print("|  (1)  MARATHI MEDIUM        |   FEES - N/A                   |")
        print("|_____________________________|________________________________|")
        c = ['ENGLISH MEDIUM', 'MARATHI MEDIUM']

        b = int(input("PLEASE SELECT YOUR MEDIUM :- "))

        if b == 0:
            print(F"YOUR SELECTED MEDIUM {c[b]}")
            print("YOUR FEES IS :- 15,000 RUPEES")
            print(" ______________________________________________________")
            print("|                  PAYMENT STETUS                      |")
            print(" ______________________________________________________")
            print("|                                                      |")
            print("|                                  (Y)yes     (N)no    |")
            print("|______________________________________________________|")
            g = 'Y', 'y'
            h = 'N', 'n'
            i = str(input(""))
            if i in g:
                print("______________________________________________________")
                print("|                  ADMISION RECEPT                   |")
                print("______________________________________________________")
                print(F"| NAME          : {a}                                         ")
                print(f"| MEDIUM        : {c[b]}                                      ")
                print(f"| CLASS         : 2nd                                    ")
                print("|PAYMENT STATUS :  Y                                           ")
                print("|____________________________________________________|")
                print(" ______________________________________________________")
                print("|                  ADMISSION CONFORMATION              |")
                print(" ______________________________________________________")
                print("|                                                      |")
                print("|                                  (Y)yes     (N)no    |")
                print("|______________________________________________________|")
                p = 'y', 'Y'
                q = 'n', 'N'
                r = str(input(""))
                if r in p:
                    print("__________________________________________________")
                    print("|   ADDMISION IS SUCCESSFULLY DONE CHECK EMAIL   |")
                    print("|________________________________________________|")
                elif r in q:
                    print("__________________________________________________")
                    print("|           ADDMISION IS CANCELLED               |")
                    print("|________________________________________________|")

            elif i in h:
                print(" _____________________________________________________")
                print("|YOUR ADDMISION IS CANCELLED,BECAUSE YOUR NOT PAY FEES|")
                print("|_____________________________________________________|")
            else:
                print("PLEASE CAUSE CORRECT KEY")
        elif b == 1:
            print(F"YOUR SELECTED MEDIUM {c[b]}")
            print("______________________________________________________")
            print("|                  ADMISION RECEPT                   |")
            print("______________________________________________________")
            print(F"| NAME          : {a}                                         ")
            print(f"| MEDIUM        : {c[b]}                                      ")
            print(f"| CLASS         : 2nd                                    ")
            print("|PAYMENT STATUS :  N/A                                           ")
            print("|____________________________________________________|")
            print(" ______________________________________________________")
            print("|                  ADMISSION CONFORMATION              |")
            print(" ______________________________________________________")
            print("|                                                      |")
            print("|                                  (Y)yes     (N)no    |")
            print("|______________________________________________________|")
            p = 'y', 'Y'
            q = 'n', 'N'
            r = str(input(""))
            if r in p:
                print("__________________________________________________")
                print("|   ADDMISION IS SUCCESSFULLY DONE CHECK EMAIL   |")
                print("|________________________________________________|")
            elif r in q:
                print("__________________________________________________")
                print("|           ADDMISION IS CANCELLED               |")
                print("|________________________________________________|")
elif s==9:
    d = str(input('PLEASE ENTER YOUR GRADE IN PREVIOUS STRANDERD :- '))
    e = 'A', 'a'
    f = 'B', 'b'
    if d in e or d in f:
        gradea: bool = True
        print("YOU ARE ALIGIBLE FOR SCHOOL")
        print(" ______________________________________________________________")
        print("|                            MEDIUMS                           |")
        print(" ______________________________________________________________")
        print("|  (0)  ENGLISH MEDIUM        |   FEES - 15,000 RUPEES         |")
        print("|  (1)  MARATHI MEDIUM        |   FEES - N/A                   |")
        print("|_____________________________|________________________________|")
        c = ['ENGLISH MEDIUM', 'MARATHI MEDIUM']

        b = int(input("PLEASE SELECT YOUR MEDIUM :- "))

        if b == 0:
            print(F"YOUR SELECTED MEDIUM {c[b]}")
            print("YOUR FEES IS :- 15,000 RUPEES")
            print(" ______________________________________________________")
            print("|                  PAYMENT STETUS                      |")
            print(" ______________________________________________________")
            print("|                                                      |")
            print("|                                  (Y)yes     (N)no    |")
            print("|______________________________________________________|")
            g = 'Y', 'y'
            h = 'N', 'n'
            i = str(input(""))
            if i in g:
                print("______________________________________________________")
                print("|                  ADMISION RECEPT                   |")
                print("______________________________________________________")
                print(F"| NAME          : {a}                                         ")
                print(f"| MEDIUM        : {c[b]}                                      ")
                print(f"| CLASS         : 3rd                                   ")
                print("|PAYMENT STATUS :  Y                                           ")
                print("|____________________________________________________|")
                print(" ______________________________________________________")
                print("|                  ADMISSION CONFORMATION              |")
                print(" ______________________________________________________")
                print("|                                                      |")
                print("|                                  (Y)yes     (N)no    |")
                print("|______________________________________________________|")
                p = 'y', 'Y'
                q = 'n', 'N'
                r = str(input(""))
                if r in p:
                    print("__________________________________________________")
                    print("|   ADDMISION IS SUCCESSFULLY DONE CHECK EMAIL   |")
                    print("|________________________________________________|")
                elif r in q:
                    print("__________________________________________________")
                    print("|           ADDMISION IS CANCELLED               |")
                    print("|________________________________________________|")

            elif i in h:
                print(" _____________________________________________________")
                print("|YOUR ADDMISION IS CANCELLED,BECAUSE YOUR NOT PAY FEES|")
                print("|_____________________________________________________|")
            else:
                print("PLEASE CAUSE CORRECT KEY")
        elif b == 1:
            print(F"YOUR SELECTED MEDIUM {c[b]}")
            print("______________________________________________________")
            print("|                  ADMISION RECEPT                   |")
            print("______________________________________________________")
            print(F"| NAME          : {a}                                         ")
            print(f"| MEDIUM        : {c[b]}                                      ")
            print(f"| CLASS         : 3rd                                   ")
            print("|PAYMENT STATUS :  N/A                                           ")
            print("|____________________________________________________|")
            print(" ______________________________________________________")
            print("|                  ADMISSION CONFORMATION              |")
            print(" ______________________________________________________")
            print("|                                                      |")
            print("|                                  (Y)yes     (N)no    |")
            print("|______________________________________________________|")
            p = 'y', 'Y'
            q = 'n', 'N'
            r = str(input(""))
            if r in p:
                print("__________________________________________________")
                print("|   ADDMISION IS SUCCESSFULLY DONE CHECK EMAIL   |")
                print("|________________________________________________|")
            elif r in q:
                print("__________________________________________________")
                print("|           ADDMISION IS CANCELLED               |")
                print("|________________________________________________|")
elif s==10:
    d = str(input('PLEASE ENTER YOUR GRADE IN PREVIOUS STRANDERD :- '))
    e = 'A', 'a'
    f = 'B', 'b'
    if d in e or d in f:
        gradea: bool = True
        print("YOU ARE ALIGIBLE FOR SCHOOL")
        print(" ______________________________________________________________")
        print("|                            MEDIUMS                           |")
        print(" ______________________________________________________________")
        print("|  (0)  ENGLISH MEDIUM        |   FEES - 15,000 RUPEES         |")
        print("|  (1)  MARATHI MEDIUM        |   FEES - N/A                   |")
        print("|_____________________________|________________________________|")
        c = ['ENGLISH MEDIUM', 'MARATHI MEDIUM']

        b = int(input("PLEASE SELECT YOUR MEDIUM :- "))

        if b == 0:
            print(F"YOUR SELECTED MEDIUM {c[b]}")
            print("YOUR FEES IS :- 15,000 RUPEES")
            print(" ______________________________________________________")
            print("|                  PAYMENT STETUS                      |")
            print(" ______________________________________________________")
            print("|                                                      |")
            print("|                                  (Y)yes     (N)no    |")
            print("|______________________________________________________|")
            g = 'Y', 'y'
            h = 'N', 'n'
            i = str(input(""))
            if i in g:
                print("______________________________________________________")
                print("|                  ADMISION RECEPT                   |")
                print("______________________________________________________")
                print(F"| NAME          : {a}                                         ")
                print(f"| MEDIUM        : {c[b]}                                      ")
                print(f"| CLASS         : 4th                                   ")
                print("|PAYMENT STATUS :  Y                                           ")
                print("|____________________________________________________|")
                print(" ______________________________________________________")
                print("|                  ADMISSION CONFORMATION              |")
                print(" ______________________________________________________")
                print("|                                                      |")
                print("|                                  (Y)yes     (N)no    |")
                print("|______________________________________________________|")
                p = 'y', 'Y'
                q = 'n', 'N'
                r = str(input(""))
                if r in p:
                    print("__________________________________________________")
                    print("|   ADDMISION IS SUCCESSFULLY DONE CHECK EMAIL   |")
                    print("|________________________________________________|")
                elif r in q:
                    print("__________________________________________________")
                    print("|           ADDMISION IS CANCELLED               |")
                    print("|________________________________________________|")

            elif i in h:
                print(" _____________________________________________________")
                print("|YOUR ADDMISION IS CANCELLED,BECAUSE YOUR NOT PAY FEES|")
                print("|_____________________________________________________|")
            else:
                print("PLEASE CAUSE CORRECT KEY")
        elif b == 1:
            print(F"YOUR SELECTED MEDIUM {c[b]}")
            print("______________________________________________________")
            print("|                  ADMISION RECEPT                   |")
            print("______________________________________________________")
            print(F"| NAME          : {a}                                         ")
            print(f"| MEDIUM        : {c[b]}                                      ")
            print(f"| CLASS         : 4th                                   ")
            print("|PAYMENT STATUS :  N/A                                           ")
            print("|____________________________________________________|")
            print(" ______________________________________________________")
            print("|                  ADMISSION CONFORMATION              |")
            print(" ______________________________________________________")
            print("|                                                      |")
            print("|                                  (Y)yes     (N)no    |")
            print("|______________________________________________________|")
            p = 'y', 'Y'
            q = 'n', 'N'
            r = str(input(""))
            if r in p:
                print("__________________________________________________")
                print("|   ADDMISION IS SUCCESSFULLY DONE CHECK EMAIL   |")
                print("|________________________________________________|")
            elif r in q:
                print("__________________________________________________")
                print("|           ADDMISION IS CANCELLED               |")
                print("|________________________________________________|")
elif s==11:
    d = str(input('PLEASE ENTER YOUR GRADE IN PREVIOUS STRANDERD :- '))
    e = 'A', 'a'
    f = 'B', 'b'
    if d in e or d in f:
        gradea: bool = True
        print("YOU ARE ALIGIBLE FOR SCHOOL")
        print(" ______________________________________________________________")
        print("|                            MEDIUMS                           |")
        print(" ______________________________________________________________")
        print("|  (0)  ENGLISH MEDIUM        |   FEES - 15,000 RUPEES         |")
        print("|  (1)  MARATHI MEDIUM        |   FEES - N/A                   |")
        print("|_____________________________|________________________________|")
        c = ['ENGLISH MEDIUM', 'MARATHI MEDIUM']

        b = int(input("PLEASE SELECT YOUR MEDIUM :- "))

        if b == 0:
            print(F"YOUR SELECTED MEDIUM {c[b]}")
            print("YOUR FEES IS :- 15,000 RUPEES")
            print(" ______________________________________________________")
            print("|                  PAYMENT STETUS                      |")
            print(" ______________________________________________________")
            print("|                                                      |")
            print("|                                  (Y)yes     (N)no    |")
            print("|______________________________________________________|")
            g = 'Y', 'y'
            h = 'N', 'n'
            i = str(input(""))
            if i in g:
                print("______________________________________________________")
                print("|                  ADMISION RECEPT                   |")
                print("______________________________________________________")
                print(F"| NAME          : {a}                                         ")
                print(f"| MEDIUM        : {c[b]}                                      ")
                print(f"| CLASS         : 5th                                   ")
                print("|PAYMENT STATUS :  Y                                           ")
                print("|____________________________________________________|")
                print(" ______________________________________________________")
                print("|                  ADMISSION CONFORMATION              |")
                print(" ______________________________________________________")
                print("|                                                      |")
                print("|                                  (Y)yes     (N)no    |")
                print("|______________________________________________________|")
                p = 'y', 'Y'
                q = 'n', 'N'
                r = str(input(""))
                if r in p:
                    print("__________________________________________________")
                    print("|   ADDMISION IS SUCCESSFULLY DONE CHECK EMAIL   |")
                    print("|________________________________________________|")
                elif r in q:
                    print("__________________________________________________")
                    print("|           ADDMISION IS CANCELLED               |")
                    print("|________________________________________________|")

            elif i in h:
                print(" _____________________________________________________")
                print("|YOUR ADDMISION IS CANCELLED,BECAUSE YOUR NOT PAY FEES|")
                print("|_____________________________________________________|")
            else:
                print("PLEASE CAUSE CORRECT KEY")
        elif b == 1:
            print(F"YOUR SELECTED MEDIUM {c[b]}")
            print("______________________________________________________")
            print("|                  ADMISION RECEPT                   |")
            print("______________________________________________________")
            print(F"| NAME          : {a}                                         ")
            print(f"| MEDIUM        : {c[b]}                                      ")
            print(f"| CLASS         : 5th                                   ")
            print("|PAYMENT STATUS :  N/A                                           ")
            print("|____________________________________________________|")
            print(" ______________________________________________________")
            print("|                  ADMISSION CONFORMATION              |")
            print(" ______________________________________________________")
            print("|                                                      |")
            print("|                                  (Y)yes     (N)no    |")
            print("|______________________________________________________|")
            p = 'y', 'Y'
            q = 'n', 'N'
            r = str(input(""))
            if r in p:
                print("__________________________________________________")
                print("|   ADDMISION IS SUCCESSFULLY DONE CHECK EMAIL   |")
                print("|________________________________________________|")
            elif r in q:
                print("__________________________________________________")
                print("|           ADDMISION IS CANCELLED               |")
                print("|________________________________________________|")
elif s==12:
    d = str(input('PLEASE ENTER YOUR GRADE IN PREVIOUS STRANDERD :- '))
    e = 'A', 'a'
    f = 'B', 'b'
    if d in e or d in f:
        gradea: bool = True
        print("YOU ARE ALIGIBLE FOR SCHOOL")
        print(" ______________________________________________________________")
        print("|                            MEDIUMS                           |")
        print(" ______________________________________________________________")
        print("|  (0)  ENGLISH MEDIUM        |   FEES - 15,000 RUPEES         |")
        print("|  (1)  MARATHI MEDIUM        |   FEES - N/A                   |")
        print("|_____________________________|________________________________|")
        c = ['ENGLISH MEDIUM', 'MARATHI MEDIUM']

        b = int(input("PLEASE SELECT YOUR MEDIUM :- "))

        if b == 0:
            print(F"YOUR SELECTED MEDIUM {c[b]}")
            print("YOUR FEES IS :- 15,000 RUPEES")
            print(" ______________________________________________________")
            print("|                  PAYMENT STETUS                      |")
            print(" ______________________________________________________")
            print("|                                                      |")
            print("|                                  (Y)yes     (N)no    |")
            print("|______________________________________________________|")
            g = 'Y', 'y'
            h = 'N', 'n'
            i = str(input(""))
            if i in g:
                print("______________________________________________________")
                print("|                  ADMISION RECEPT                   |")
                print("______________________________________________________")
                print(F"| NAME          : {a}                                         ")
                print(f"| MEDIUM        : {c[b]}                                      ")
                print(f"| CLASS         : 6th                                    ")
                print("|PAYMENT STATUS :  Y                                           ")
                print("|____________________________________________________|")
                print(" ______________________________________________________")
                print("|                  ADMISSION CONFORMATION              |")
                print(" ______________________________________________________")
                print("|                                                      |")
                print("|                                  (Y)yes     (N)no    |")
                print("|______________________________________________________|")
                p = 'y', 'Y'
                q = 'n', 'N'
                r = str(input(""))
                if r in p:
                    print("__________________________________________________")
                    print("|   ADDMISION IS SUCCESSFULLY DONE CHECK EMAIL   |")
                    print("|________________________________________________|")
                elif r in q:
                    print("__________________________________________________")
                    print("|           ADDMISION IS CANCELLED               |")
                    print("|________________________________________________|")

            elif i in h:
                print(" _____________________________________________________")
                print("|YOUR ADDMISION IS CANCELLED,BECAUSE YOUR NOT PAY FEES|")
                print("|_____________________________________________________|")
            else:
                print("PLEASE CAUSE CORRECT KEY")
        elif b == 1:
            print(F"YOUR SELECTED MEDIUM {c[b]}")
            print("______________________________________________________")
            print("|                  ADMISION RECEPT                   |")
            print("______________________________________________________")
            print(F"| NAME          : {a}                                         ")
            print(f"| MEDIUM        : {c[b]}                                      ")
            print(f"| CLASS         : 6th                                   ")
            print("|PAYMENT STATUS :  N/A                                           ")
            print("|____________________________________________________|")
            print(" ______________________________________________________")
            print("|                  ADMISSION CONFORMATION              |")
            print(" ______________________________________________________")
            print("|                                                      |")
            print("|                                  (Y)yes     (N)no    |")
            print("|______________________________________________________|")
            p = 'y', 'Y'
            q = 'n', 'N'
            r = str(input(""))
            if r in p:
                print("__________________________________________________")
                print("|   ADDMISION IS SUCCESSFULLY DONE CHECK EMAIL   |")
                print("|________________________________________________|")
            elif r in q:
                print("__________________________________________________")
                print("|           ADDMISION IS CANCELLED               |")
                print("|________________________________________________|")
elif s==13:
    d = str(input('PLEASE ENTER YOUR GRADE IN PREVIOUS STRANDERD :- '))
    e = 'A', 'a'
    f = 'B', 'b'
    if d in e or d in f:
        gradea: bool = True
        print("YOU ARE ALIGIBLE FOR SCHOOL")
        print(" ______________________________________________________________")
        print("|                            MEDIUMS                           |")
        print(" ______________________________________________________________")
        print("|  (0)  ENGLISH MEDIUM        |   FEES - 15,000 RUPEES         |")
        print("|  (1)  MARATHI MEDIUM        |   FEES - N/A                   |")
        print("|_____________________________|________________________________|")
        c = ['ENGLISH MEDIUM', 'MARATHI MEDIUM']

        b = int(input("PLEASE SELECT YOUR MEDIUM :- "))

        if b == 0:
            print(F"YOUR SELECTED MEDIUM {c[b]}")
            print("YOUR FEES IS :- 15,000 RUPEES")
            print(" ______________________________________________________")
            print("|                  PAYMENT STETUS                      |")
            print(" ______________________________________________________")
            print("|                                                      |")
            print("|                                  (Y)yes     (N)no    |")
            print("|______________________________________________________|")
            g = 'Y', 'y'
            h = 'N', 'n'
            i = str(input(""))
            if i in g:
                print("______________________________________________________")
                print("|                  ADMISION RECEPT                   |")
                print("______________________________________________________")
                print(F"| NAME          : {a}                                         ")
                print(f"| MEDIUM        : {c[b]}                                      ")
                print(f"| CLASS         : 7th                                    ")
                print("|PAYMENT STATUS :  Y                                           ")
                print("|____________________________________________________|")
                print(" ______________________________________________________")
                print("|                  ADMISSION CONFORMATION              |")
                print(" ______________________________________________________")
                print("|                                                      |")
                print("|                                  (Y)yes     (N)no    |")
                print("|______________________________________________________|")
                p = 'y', 'Y'
                q = 'n', 'N'
                r = str(input(""))
                if r in p:
                    print("__________________________________________________")
                    print("|   ADDMISION IS SUCCESSFULLY DONE CHECK EMAIL   |")
                    print("|________________________________________________|")
                elif r in q:
                    print("__________________________________________________")
                    print("|           ADDMISION IS CANCELLED               |")
                    print("|________________________________________________|")

            elif i in h:
                print(" _____________________________________________________")
                print("|YOUR ADDMISION IS CANCELLED,BECAUSE YOUR NOT PAY FEES|")
                print("|_____________________________________________________|")
            else:
                print("PLEASE CAUSE CORRECT KEY")
        elif b == 1:
            print(F"YOUR SELECTED MEDIUM {c[b]}")
            print("______________________________________________________")
            print("|                  ADMISION RECEPT                   |")
            print("______________________________________________________")
            print(F"| NAME          : {a}                                         ")
            print(f"| MEDIUM        : {c[b]}                                      ")
            print("| CLASS         : 7th                                   ")
            print("|PAYMENT STATUS :  N/A                                           ")
            print("|____________________________________________________|")
            print(" ______________________________________________________")
            print("|                  ADMISSION CONFORMATION              |")
            print(" ______________________________________________________")
            print("|                                                      |")
            print("|                                  (Y)yes     (N)no    |")
            print("|______________________________________________________|")
            p = 'y', 'Y'
            q = 'n', 'N'
            r = str(input(""))
            if r in p:
                print("__________________________________________________")
                print("|   ADDMISION IS SUCCESSFULLY DONE CHECK EMAIL   |")
                print("|________________________________________________|")
            elif r in q:
                print("__________________________________________________")
                print("|           ADDMISION IS CANCELLED               |")
                print("|________________________________________________|")
else:
    print("NOT ILLEGIBLE FOR SCHOOL")







