import random

def roll(): # Hum ny ik function banaya ha 
    min_number = 1
    max_number = 6
    rol = random.randint(min_number,max_number)   # YA sab random number ky lu ha 1 sy 6 tak 
    return rol

    """rol = random.randint(1,6) Asy bhi ka sackty thy 
    return rol"""

# value = roll() # YA function ko call kia ha 
# print(value)

while True:
    players = input("Enter the number of the player between (2-4): ") 
    if players.isdigit():   # Ya check kary ga ky digit hona lazmi ha
        players = int(players) # digit ho ga to usy integer ma kary ga
        if 2 <= players <=4: # agr player 2 ho ya 3 ho ya 4 ho tab condition true ho gi warna false
            break
        else:
            print("Invlaid Chosise")

    else:
        print("Enter the Digit")
        
#  ************ Simulate each player turn*********       
        
max_score = 50 
                        # # Number of players ko 0 da ga
                        # We have to make list that change size based on number of players
player_score = [0 for _ in range(players)] # IS ki madad sy hum players ky socre kp array ky ander store kar sackty ha
# print(player_score)

# ******Player Turn*******

while max(player_score) < max_score: # YA check kary ga ky ag kisi player ka ccore 50 sy above hoa to wo jeet jy ga or ap n kar ky quit kar sackty ha us plyer ko
    
    for player_idx in range(players): # For loop is ly lagya ky jitny yplyar ho itni bar code chly 
        print("\nPlayer number",player_idx + 1, "Just started their turn!") # Kon sy plar ki bari ya ya baty ga
        print("Your total score is:", player_score[player_idx], "\n" ) # Player ki index dakhty hoy us ka total score baty ga
        your_score = 0 # Start ma 0 initilixe karwa dia 
        
        while True: # Tab tak chalta rahy ga jab tak roll par 1 ana aha jy ya (y) ki jagha kuch or type kar do
            should_roll = input("Would you like to roll say (y) ")
            if should_roll.lower() != "y": # Agr y ky braber y nhi ho ga to break ho jy ga while 
                print("You OUT")
                break
                
            value = roll() # YAha function call ho jy ga jab y likha jy ga to ik random numbr ay ga
            if value == 1: # Agr random number 1 hoa to break 
                print("You rolled 1 you done")
                break
                
            else :
                your_score += value            # jo bhi random number number ay ga usy your_socre ma add kar dia jy ga har bar
                print("you rolled a: ",value) # ya baty ga ky kia number aya ha
                
            print("Your Current Score is :", your_score ) # Jo roll ma aya ha usy phly waly ma add kar ky baty ga
        
        player_score[player_idx] += your_score # Ya jab ik plar ki bari pori ho gi us ky score ko player_score ma daly ga
        print("Your total score after adding precious all turns is: ",player_score[player_idx]) # Ya usy print karwa dy ga

            #Zorari nhi ky sirf ik player ka maximum score 50 sy above ho zada ka bhi ho sackta ha

max_score = max(player_score) # Jab jis playr ha maximium score ay ga us ko max_score ma store karwa dy gy 
wining_idx = player_score.index(max_score) # Ya humy baty ga ky kis player ka maximum score aya ha us ki index baty ga or wining_idx ma store kar dy ga
print("Player Number,",wining_idx + 1,"is the winer with the maximum score: ",max_score)
                    #  YA PLAYER NUM DY GA                                    YA US KA SCORE
