a=[]
capa=5
storeda=0
b=[]
capb=7
storedb=0
c=[]
capc=3
storedc=0
while True:
    print(a, "\n", b, "\n", c, "\na capacity = 5, b capacity = 7, c capacity = 3")
    d=int(input("What you wanna do, 1 for put item, 2 for take item, 3 to exit"))
    if d==1:
        e=input("What kind of item you want to put?")
        f=int(input("To which storage you wanna put that item?"))
        if f==1:
            storeda=storeda+1
            if storeda<=capa:
                a.append(e)
            else:
                print("Sorry, this storage is full.")
                storeda=storeda-1
        elif f==2:
            storedb=storedb+1
            if storedb<=capb:
                b.append(e)
            else:
                print("Sorry, this storage is full.")
                storedb=storedb-1
        elif f==3:
            storedc=storedc+1
            if storedc<=capc:
                c.append(e)
            else:
                print("Sorry, this storage is full.")
                storedc=storedc-1
    elif d==2:
        g=int(input("which storage?"))
        h=int(input("what item(use number)"))
        h=h-1
        if g==1:
            if storeda <= 0:
                print("Sorry, this storage is empty.")
            else:
                storeda=storeda-1
                del a[h]
        elif g==2:
            if storedb <= 0:
                print("Sorry, this storage is empty.")
            else:
                storedb=storedb-1
                del b[h]
        elif g==3:
            if storedc <= 0:
                print("Sorry, this storage is empty.")
            else:
                storedc=storedc-1
                del c[h]
    elif d==3:
        break
#Copyright Felix Anggara