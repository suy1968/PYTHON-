import pickle
dire={}

def add():
    a='y'
    fw= open("directory.dat","ab+")
    while a=='y':
        cn= int(input("Enter contact number"))
        fn= input("Enter First name")
        mn= input("Enter middle name")
        ln= input("Enter last name")
        add= input("Enter address")
        hn=int(input("Enter house number"))
        city=input("Enter city")
        an=int(input("Enter aadhaar no"))
        ema= input("Enter email")
        dob= int(input("Enter date of birth"))
        dire['contact.no'] =cn
        dire['name'] =fn+' '+mn+" "+ln
        dire['address']= add
        dire['house_no']= hn
        dire['city']= city
        dire['aadhaar_no']= an
        dire['Email'] = ema
        dire['date of birth']= dob       
        pickle.dump(dire,fw)
        a = input("Do you want to add more (Y/N)")
        fw.close()

def display():
   str = "True"
   fr= open("directory.dat","rb")
   try:
       while str:
            dire = pickle.load(fr)
            for a in dire.items():
               print(a)
            print('\n')
   except EOFError:
         print("You have reached at the end of file")
         fr.close()

def search():
    str = "True"
    Found= False
    fr = open("directory.dat","rb")
    fr.seek(0,0)
    Sr =int(input("Enter contact number to be searched:"))
    try:
       while str:
           dire = pickle.load(fr)
           if dire['contact.no'] == Sr:
               print("Record Found\n", dire)
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
    fr = open("directory.dat","ab+")
    fr.seek (0,0)
    Sr = int(input("Enter contact number to be updated:"))
    try:
        while str:
            rpos = fr.tell()
            dire = pickle.load(fr)
            if dire['contact.no'] == Sr:
                print("Record Found\n", dire)
                cn= int(input("Enter contact number"))
                fn= input("Enter First name")
                mn= input("Enter middle name")
                ln= input("Enter last name")
                add= input("Enter address")
                hn=int(input("Enter house number"))
                city=input("Enter city")
                an=int(input("Enter aadhaar no"))
                ema= input("Enter email")
                dob= int(input("Enter date of birth"))
                dire['contact.no'] =cn
                dire['name'] =fn+' '+mn+" "+ln
                dire['address']= add
                dire['house_no']= hn
                dire['city']= city
                dire['aadhaar_no']= an
                dire['Email'] = ema
                dire['date of birth']= dob       
                pickle.dump(dire,fr)
               # found = True
    except EOFError:
        if Found:
            print("\n\n Record successfully updated")

        else:
            print("\n\n Sorry record not found")
            fr.close()

#main function
ch='i'
while ch!= 5:
    print("\n\n         WELOCOME TO MOBILE DIRECTORY       \n\n")
    print("1. Add the contact data")
    print("2. Display all")
    print("3. To search for Contact number")
    print("4. To update information about a contact number")
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
    elif ch==5:
        exit()
                  

























    
 
         


        
