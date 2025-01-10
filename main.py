a=int(input("ENTER YOUR NUMBER : "))


for i in range(1,a,+1):
    for j in range(1,1+i,+1):
        print('*',end="")
    print("")
for i in range(1,a,+1):
    for j in range(1,a-i,+1):
        print('*',end ='')
    print("")
