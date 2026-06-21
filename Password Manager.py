master_pwd = input("What is the master pasword! ")


def view():
    
    with open("passswords.txt" ,"r") as f: # r-> mode only read the file if don't exit error or agr phly sy ho gi to overwrite kar dy ga purana data ur jay ga 
        for line in f.readlines():
            "print(line)" # Ya par ager print(line) karo ga to ik line ka gap ata rahy ga ku ky carge return ata rahy ga \n ki waja sy 
            data = line.rstrip() # is ly lie.rstrip use kia ta ky ik line ka gap na ay
            name , password = data.split("|")
            print("Name :" ,name, "| Password :", password)
            
            
            """  ********Info***********
            tim"|"ali"|"ahmad"|"khan" split("|") jaha jaha | ya ho ga waha sy alag ho jy ga data
             ["tim","ali","ahmad","khan"] or list ki tarha alag alag show ho ga
             "tim"|"good" is case ma 2 hi chezy ha to bas name,password kara or agr 3 hoty to name,pasword,gender ho jata
             name, password = ["tim","good"]"""

def add():
    name  = input("Enter the Account Name! ")
    password = input("Enter the New Password! ")
    
    with open("passswords.txt" ,"a") as f: # a-> mode means you open file in read write mode 
        f.write(name + "|" + password + "\n") # Ya file ma name or password ko daly ga "|" ky sath or "\n" har bar naya nam or password any par agli line par chla jy ga
    

while True:
    
    mode = input ("Would you like to view the existing password or add new one: (view/add) ")
    if mode == "q":
        print("You quit!")
        break
    
    if mode == "view": # Jab condtion true ho gi view() fucntion call ho jay ga
        view()

    elif mode =="add": # Jab condtion true ho gi add() fucntion call ho jay ga
        add()
    else:
        print("invalid Mode!")
        continue
    