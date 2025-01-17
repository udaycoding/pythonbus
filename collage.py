print("|------------------------------------------------------|")
print("|                   -UD SHOP-                          |")
print("|------------------------------------------------------|")
shop=['TOP OFFERS','MOBILES & TABLETS',"TV'S & APPLIANCES",'ELECTRONICS','FASION']

print("|-----------------------------------------------------------------------------------------------|")
print("| (0) MEN | (1) WOMEN | (3) TV'S & APPLIANCES | (4) ELECTRONICS | (5) MOBILES & TABLETS | ")
print("|-----------------------------------------------------------------------------------------------|")
a=int(input(""))
men=['Men Printed Hooded Neck Cotton Blend Black T-Shirt','Men Colorblock Round Neck Polyester Pink T-Shirt ','Men Printed Round Neck Polyester Multicolor T-Shirt','Men Printed Round Neck Poly Cotton Multicolor T-Shirt']
if a==0:
    print("|--------------------------------------------------------------------------------------------------------------------|")
    print("| (0) Men Printed Hooded Neck Cotton Blend Black T-Shirt | (1) Men Colorblock Round Neck Polyester Pink T-Shirt      |")
    print("| (2) Men Printed Round Neck Polyester Multicolor T-Shirt| (3) Men Printed Round Neck Poly Cotton Multicolor T-Shirt |")
    print("|--------------------------------------------------------------------------------------------------------------------|")
    b=int(input(""))
    sizes=['S','M','L','XL','XXL']
    if b==0:
        print("|---------------------------------------------------------------------------------|")
        print("|  ₹249                                                                           | ")
        print("|  RATING 3.8 *                                                                   |")
        print("|                                                                                 |")
        print("|                 --SIZES--                                                       |")
        print("|  (0) S | (1) M | (2) L | (3) XL | (4) XXL                                       |")
        print("|---------------------------------------------------------------------------------|")
        c=int(input(""))
        if c==0:
            print("|------------------------------------------------------------------|")
            print("|  (0) ADD CART | (1) BUY                                          |")
            print("|------------------------------------------------------------------|")
            d=int(input(""))
            if d==0:
                print("|----------------------------------------------------------|")
                print("|              - YOUR ORDER ADDED TO CART -                |")
                print("|----------------------------------------------------------|")
            elif d==1:
                j=str(input("NAME         :- "))
                e=int(input("PHONE NUMBER :- "))
                g=int(input("PIN CODE     :- "))
                f=str(input("ADDRESS      :- "))
                payment=['CASH ON DELIVERY','CRADIT CARD','DEBIT CARD','UPI']
                print("|----------------------------------------------------------|")
                print("| PAYMENT METHODS :-                                       |")
                print("| (0) CASH ON DELIVERY | (1) CRADIT CARD | (2) DEBIT CARD  |")
                print("| (3) UPI                                                  |")
                print("|----------------------------------------------------------|")
                i=int(input(""))
                if i==0:
                    print("|-----------------------------------------------------------|")
                    print("|                                                           |")
                    print(f"| {men[b]}                                                  ")
                    print(f'| SIZE:- {sizes[c]}                                                 ')
                    print("|                                                           |")
                    print("|                 --SHIPING INFORMATION--                   |  ")
                    print("|                                                           |")
                    print(F"| {j}                                                       ")
                    print(f"| {e}                                                       ")
                    print(f"| {f}                                                       ")
                    print(f'| {g}                                                       ')
                    print("| PAYMENT METHOD :-                                        |")
                    print(f'| {payment[i]}                                             ')
                    print("|-----------------------------------------------------------|")
                    x='y','Y'
                    y='n','N'
                    print("|-----------------------------------------------------------|")
                    print("|                    ORDER CONFORMATION                     |")
                    print("|-----------------------------------------------------------|")
                    print("|                                                           |")
                    print("|                                          (Y)yes (N)no     |")
                    print("|-----------------------------------------------------------|")
                    z=str(input(""))
                    if z in x:
                        print("|----------------------------------------------------------|")
                        print("|        YOUR ORDER IS BOOKED CHECK YOUR MASSAGER          |")
                        print("|----------------------------------------------------------|")
                    elif z in y:
                        print("|----------------------------------------------------------|")
                        print("|                YOUR ORDER IS CANCELLED                   |")
                        print("|----------------------------------------------------------|")




