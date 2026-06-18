import random 

user_wins = 0
computer_wins = 0


options = ["rock","paper","scissor"]  # Ik list bana dy gy ta ky single single na karna pary 

while True:
    user_input = input("You have to Enter (Rock, Paper, Scissor) or q to qiut ".lower() )

    if user_input == "q": # q type kary gy to khatam ho jy ga program 
        print("You Quit")
        break

    if user_input not in options: # Agr q or list ky ilawa kuch type karo gy to worng ka mess ay ga mgr prog end nhi ho ga continue ki waja sy 
        print("You Enter the wronge option")
        continue
    else:
        print("You Pick",user_input,".")  # YA display kary ga user ny kia pick kia

    random_number = random.randint(0,2) # YA random number bana ky dy ga 0 sy 2 ma "randint ma start or end wala numbr bhi show hota ha"
    # rock = 0 , paper = 1 , scissor = 2    # randrange ma end wla number show nhi hota (0,1) bas 2 nhi ho ga

    computer_pick = options[random_number] # YA jo random number ay ga wo computer_pick ko dia jy ga opitons ma sy
    print("Computer pick",computer_pick,".") # YA display kary ga computer ny kia pick kia
    
    

    if user_input == "rock" and computer_pick == "scissor": 
        print("You Win! ")
        user_wins += 1 # user wins add kary ga
        
        # 3 wins condtions dal di baki khud ho jana
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You Win! ")
        user_wins += 1
        

    elif user_input == "scissor" and computer_pick == "paper":
        print("You Win! ")
        user_wins += 1
         
    else:
        print("You Lost! ")
        computer_wins += 1 # Computer wins add karyy ga
        
        
print("You wins",user_wins, ".") # User wins ky number dy ga
print("Computer wins",computer_wins, ".")# computer wins ky number dy ga
print("Good Bye :)") 

    
        
