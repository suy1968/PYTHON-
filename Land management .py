import pickle
land={}

def add():
    a='y'
    fw= open("land.dat","ab+")
    while a=='y':
        cn= input("Enter colony name")
        sn= int(input("Enter sector number"))
        lt= input("Enter land type")
        lp= int(input("Enter land price"))
        tr= int(input("Enter total rate of land"))
        emi= int(input("Enter amount of EMI to be paid per month"))
        rn= int(input("Enter registry number"))
        land['Colony name'] =cn
        land['Sector no'] =sn
        land['Land Type'] =lt
        land['Land price'] =lp
        land['Total rate of land']= tr
        land['EMI  amount'] = emi
        land['Registry number']= rn        
        pickle.dump(land,fw)
        a = input("Do you want to add more (Y/N)")
        fw.close()

def display():
   str = "True"
   fr= open("land.dat","rb")
   try:
       while str:
           land = pickle.load(fr)
           print(land)
   except EOFError:
         print("You have reached at the end of file")
         fr.close()

def search():
    str = "True"
    Found= False
    fr = open("land.dat","rb")
    fr.seek(0,0)
    Sr =input("Enter the colony name to be searched:")
    try:
       while str:
           land = pickle.load(fr)
           if land['Colony name'] == Sr:
               print("Record Found\n", land)
               found = True
    except EOFError:
        if found:
            print("\n\n Operation successfull")
        else:
            print("\n\n Sorry record not found")
            print("You reached to end of file")
            fr.close()

def update():
    Found =  False
    str = "True"
    fr = open("land.dat","ab+")
    fr.seek (0,0)
    Sr = input("Enter colony name to be updated:")
    try:
        while str:
            rpos = fr.tell()
            land = pickle.load(fr)
            if land['Colony name'] == Sr:
                print("Record Found\n", land)
                cn= input("Enter colony name")
                sn= int(input("Enter sector number"))
                lt= input("Enter land type")
                lp= int(input("Enter land price"))
                tr= int(input("Enter total rate of land"))
                emi= int(input("Enter amount of EMI to be paid per month"))
                rn= int(input("Enter registry number"))
                land['Colony name'] =cn
                land['Sector no'] =sn
                land['Land Type'] =lt
                land['Land price'] =lp
                land['Total rate of land']= tr
                land['EMI  amount'] = emi
                land['Registry number']= rn  
                fr.seek (rpos)
                pickle.dump(land,fr)
               # found = True
    except EOFError:
        if found:
            
            print("\n\n Record successfully updated")

        else:
            print("\n\n Sorry record not found")
            fr.close()

#main function
ch='i'
while ch!= 5:
    print("\n\n         WELOCOME TO PARADISE GARDEN LAND PLOTTING MANAGEMENT       \n\n")
    print("1. Add the land data")
    print("2. Display all")
    print("3. To search for Colony name")
    print("4. To update information about a land")
    print("5. Exit")
    ch = int(input("Enter your choice:"))
    if ch==1:
        nd=add()
    elif ch==2:
        di=display()
    elif ch==3:
         se=search()
    elif ch==4:
         ud=update()
                  

























    
 
         


        
