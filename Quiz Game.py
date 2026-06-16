print("Welcome to the Quize Game")

playing = input("Do you want to Play? ")

if playing.lower() != "yes":
    quit()

print("Okay Lets Play :) ")

score = 0

beforestart = input("Can we start? ")
if beforestart.lower() != "yes":
    quit()


question = input("What does CPU stand for? ")
if question.lower() == "central processing unit":
    print("Correct !")
    score = score + 1
    print("Yoou Are Moving to the Next Question")
else:
    print("Incorrect !")
    
stop = input("Do you want to continue the game? ")
if stop.lower() != "yes":
    quit()


question = input("What does GPU stand for? ")
if question.lower() == "graphic processing unit":
    print("Correct !")
    score = score + 1
else:
    print("Incorrect !")



question = input("What does RAM stand for? ")
if question.lower() == "random access memory":
    print("Correct !")
    score = score + 1
else:
    print("Incorrect !")



question = input("What does PSU stand for? ")
if question.lower() == "power supply":
    print("Correct !")
    score = score + 1
else:
    print("Incorrect !")

print("You Got " + str(score)  + " Right Answers")
print("You Got " + str((score/ 4) *100)  + "%.")
