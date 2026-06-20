while True:
    your_name = input("Enter Your Name :) ").lower()
    if your_name.isdigit(): # Agr character ki jaga digit dalo gy to Enter a Valid Name print ho ga
        print("Enter a Valid Name")
        continue # Continue sy bar bar hota rahy ga jab tak sahi na dalo ya quit na karo or continue start ky while true par ly jata ha
    else:
        print("Welcome ",your_name,"to this Adventure Game!! ") # Welcome kary ga nam ky sath

    while True:
        user_decission = input("Do you Want to Play (yes or no) ").lower()

        if user_decission == "yes":
            print("Let's Go !!")
            break # Jab yes ho jy ga tab ya wala while loop khatam ho ja ga 
            # agr hata do ga to condtin true hony ky bad bhi whle true par chala jy ga 

        elif user_decission == "no":
            print("You Quit!! ")
            quit() # Ya game ko khatam kar dy ga matlab billkul program end ho jy ga
    
        else:
            print("Enter a valid Option!!")
            continue # Jab tak yes ya no nhi karo gy ata rahy ga
    

    print ("****************If YOU NOT GONA SY (Left/Right) YOU LOSE!!******************")
    answer = input("Your are on a dirt road, it come to an end and you can go Left or Right! Which way would you like to go(Left/Right) ").lower()
    
    if answer == "left": # YAHA SY 
        print ("***************8If YOU NOT GONA SY (swim/walk) YOU LOSE!!**************")
        answer = input("You come to a river, you can walk around it or swim accross the river? Type walk to walk around and swim to swim acccross: ").lower()
        
        if answer == "walk":
            print("You walk for many miles and run out oF water and you lost the Game!!") 
        
        elif answer =="swim":
            print("You swim accross and eaten by an Aligater.")
        
        else:
            print("Not a Valid Option YOU LOSE!!") # Yaha par program khud end ho jy ga
            # YAHA TAK IF HA
    
    elif answer == "right": # YAHA SY 
        print ("********If YOU NOT GONA SY (corss/back) YOU LOSE!!***********")
        answer = input("You come to a bridge, it looks wobbly, Do you want to cross it or head back (cross/back): ") 

        if answer == "cross":
            answer = input("You cross the bridge and meet a stranger, Would you like to talk to them (Yes/No)").lower()
            
            if answer == "yes":
                print("You talk to the starner and they gave you a Gold YOU WIN!! ")
            
            elif answer == "no":
                    print("You ignore the stranger you get nothing YOU LOSE!!") 
            else:
                print("Not a Valid Option YOU LOSE!!") # YAha par bhi khud end ho jy ga
                    
        elif answer =="back":
            print("You go back and YOU LOSE!!")
        else:
            print("Not a Valid Option YOU LOSE!!") # YAHA TAK ELIF HA
            
    else: # OR YA ElSE HA 
        print("Not a Valid Option YOU LOSE!!")
    break