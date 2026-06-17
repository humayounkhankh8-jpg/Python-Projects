import random

top_of_the_digit = input("Enter the Number! ") # how large the number the user want to generate

if top_of_the_digit.isdigit():# YA baty ga ky number agr digit ha to usy Integer banao 
    top_of_the_digit = int(top_of_the_digit)
    if top_of_the_digit <= 0: # Ager digit  0 ha to 
        print("Next time Enter Number Greater than Zero! ")
        quit()
else:
    print("Next time Enter the Digit! ")
    quit()



random_number = random.randrange (0,top_of_the_digit) # 0 hum ny khud rakha range ka start or jo user dy ga  wo Highest number ho ga random guess ka jo pc kary ga
guessess = 0
while True:
    guessess+= 1
    user_guess = input("Make a Guess! ")
    if user_guess.isdigit(): # User guess agr digit nhi ha to usy digit karo or phr wo usy interger kar dy ga
        user_guess= int(user_guess)
    else:
        print("Next time Enter the Digit!")
        continue

    if user_guess == random_number:
        print("You Guess the Write Number! ")
        break
    else:
        # print("You Guess the Wronge Number! ")
        if user_guess < random_number:
            print("You are below the random number")
        else:
            print("You are Above the radom number ")
        
print("You Guess" ,guessess, "Times") # print("you Guess" + str(gussess) + "Times") ik bat ha

print(random_number)
# print(rans)