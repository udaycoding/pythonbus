print(" __________________________________________________________")
print("|                WELCOME TO TRAVELS BOOKING                |")
print("|__________________________________________________________|")

a=str(input("PLEASE ENTER YOUR NAME : "))

print(f"Hii,{a}")

print(" ___________________________________________________________")
print("|               YOUR CITY IS TULJAPUR                       |")
print("|                                                           |")
print("|                                         (Y)yes   (N)no    |")
print("|___________________________________________________________|")
d='Y'
e='N'
c=str(input(""))

if c==d :
    print(" ___________________________________________________________")
    print("|               * AVAILABLE TRAVELS *                       |")
    print("|___________________________________________________________|")
    print("| (0)  KHURANA TRAVELS                                      |")
    print("| (1)  DOLPHIN TRAVELS                                      |")
    print("| (2)  AKANSHA TRAVELS                                      |")
    print("| (3)  SUNSET  TRAVELS                                      |")
    print("| (4)  GOLDEN  TRAVELS                                      |")
    print("| (5)  ROHIT   TRAVELS                                      |")
    print("| (6)  5 STAR  TRAVELS                                      |")
    print("| (7)  7 STAR  TRAVELS                                      |")
    print("|___________________________________________________________|")

    travel = ['KHURANA TRAVELS', 'DOLPHIN TRAVELS', 'AKANSHA TRANVELS', 'SUNSET TRANVELS', 'GOLDEN TRAVELS',
              'ROHIT TRAVELS', '5 STAR TRAVELS', '7 STAR TRAVELS']

    b = int(input("SELECT YOUR TRAVELS : "))

    print("_________________________________________________________")
    print(F"| SELECTED TRAVELS         |  {travel[b]}               ")
    print("|__________________________|____________________________ ")

    if b == 0:
        print(" ___________________________________________________________")
        print("|               * KHURANA TRAVELS *                         |")
        print("|___________________________________________________________|")
        print("| (0)  TULJAPUR TO PUNE                                     |")
        print("| (1)  TULJAPUR TO SAMBHAJINAGAR                            |")
        print("| (2)  TULJAPUR TO MUMBAI                                   |")
        print("| (3)  TULJAPUR TO NAGPUR                                   |")
        print("| (4)  TULJAPUR TO AHMADNAGAR                               |")
        print("|___________________________________________________________|")
        khurana=['TULJAPUR TO PUNE','TULJAPUR TO SAMBHAJINAGAR','TULJAPUR TO MUMBAI','TULJAPUR TO NAGPUR','TULJAPUR TO AHMADNAGAR']
        f=int(input("SELECT YOUR ROUT : "))
        print("_________________________________________________________")
        print(F"| SELECTED ROUT           |  {khurana[f]}               ")
        print("|__________________________|____________________________ ")
        print("")
        print("")

        print("/-------------------------------------/")
        print("|  1     2   | 100 RS   |    21    22 |")
        print("|  3     4   |----------|    23    24 |")
        print("|  5     6   |----------|    25    26 |")
        print("|  7     8   |----------|    27    28 |")
        print("|_____________________________________|")
        print("|  9     10  | 90  RS   |    29    30 |")
        print("|  11    12  |----------|    31    32 |")
        print("|  13    14  |----------|    33    34 |")
        print("|  15    16  |----------|    35    36 |")
        print("|_____________________________________|")
        print("|  17    18  | 80  RS   |    37    38 |")
        print("|  19    20  |----------|    39    40 |")
        print("|_____________________________________|")
        j=int(input("SELECT YOUR SEET : "))
        k=[1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,28]
        l=[9,10,11,12,13,14,15,16,29,30,31,32,33,34,35,36]
        m=[17,18,19,20,37,38,39,40]
        if j in k:
            vvip: bool =True
            print(f"SELECED SEET {j} - 1000 RS")
            n = str(input("PAYMENT STETUS (Y)yes,(N)no: "))
        elif  j in l:
                vip : bool= True
                print(f"SELECED SEET {j} - 500 RS")
                n = str(input("PAYMENT STETUS (Y)yes,(N)no: "))
        elif j in m:
                reg: bool = True
                print(f"SELECED SEET {j} - 300 RS")
                n = str(input("PAYMENT STETUS (Y)yes,(N)no: "))
        else:
            print("")

    i = 'Y'
    o = 'N'
    if n == i:
        if f == 0:
            print(" ___________________________________________________________")
            print("|               * TULJAPUR TO PUNE *                        |")
            print("|___________________________________________________________|")
            print("| (0)  8 :00 AM                                             |")
            print("| (1)  11:00 AM                                             |")
            print("| (2)  2 :00 PM                                             |")
            print("| (3)  7 :00 PM                                             |")
            print("|___________________________________________________________|")
            time = ['8 :00 AM', '11:00 AM', '2 :00 PM', '7 :00 PM']
            g = int(input("SELECT YOUR TIME : "))
            print("_________________________________________________________")
            print(F"| SELECTED TIME           |  {time[g]}               ")
            print("|__________________________|____________________________ ")
            print(" ___________________________________________________________")
            print("|                  * TICKET RECIPT *                        |")
            print("|___________________________________________________________|")
            print(F"| SELECTED TRAVELS         |  {travel[b]}               ")
            print(F"| SELECTED ROUT            |  {khurana[f]}               ")
            print(F"| SELECTED TIME            |  {time[g]}               ")
            print("|___________________________|_______________________________|")

            print(" ____________________________________________________________")
            print("|                   TICKET CONFORMATION                      |")
            print("|____________________________________________________________|")
            print("|                                                            |")
            print("|                                       (Y) yes  (N) no      | ")
            print("|____________________________________________________________|")
            h = str(input(""))
            y = 'Y'
            n = 'N'
            if h == y:
                print(" ____________________________________________________________")
                print("|              TICKET IS BOOKED SUCCESFULLY                  |")
                print("|____________________________________________________________|")
            elif h == n:
                print(" ____________________________________________________________")
                print("|                  TICKED IS CANCELLED                       |")
                print("|____________________________________________________________|")































else:
    print("OTHER CITY TRAVELS IS COMMING SOON...")



