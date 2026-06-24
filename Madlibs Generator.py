with open("story.txt","r") as f: # Ya text file ko (r) read mode ma open  karry ga or read karny ky kam ay ga
    story = f.read() 
    
# print(story) # IS sy print ho jy gi story dosri file ky terminal ma

#** words = [] # Ik list bana li jis ma sab words store ho gy (list ma repeting character or words bhi ay gy)
words = set()
start_of_word = -1 # Ik veriable bana lia jo baty ga ky kia us ny start word ka index dhonnd lia ha agr ha to phr hum end ka index dakhy gy

target_start = "<"
target_end = ">"

#****** enumerate gives us the access to the psoition and as well as the element at that position (or saf kam kar data ha )
# i POSTION KY LY HA OR CHAR ELEMENT BATY GA
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i # agr starting bracket mil jy to samjo hum ko start of the word mil gaya or to us ko mark kar ky variable me dal dy gy 
    
    if char == target_end and start_of_word != -1: # Jab humy end ki bracket mil jy or start ki bhi or agr start_of_word braber na ho -1 ky to hum us word ko list ya set ma store karwa dy gy
            # ***** start of word up to the index i + 1 means it gives us the access to the slice jo ky subsection ha string ka to ya ik "slice operater" ha python ma        
            # ***** slice operater ma start index/character bataty ha jaha sy slicing karni ho or ending charcter jis ma last ka character/index shamil nhi hota       
        word = story[start_of_word :i + 1 ] # slicing ki ha is ma uper bata dia or +1 is ly ha ta ky last word/index/char bhi shamil ho
#**     words.append(word) # list ma dal dia 
        words.add(word)
        start_of_word = -1 # ya for loop ko jab tak chly ga jab tak story khatam na ho jy
        
#** print(words)# YA ap ko unique words print kar ky da ga

# ************** DICTONARY USE FOR ANSWERS ************

answers = {} # Dictonary bany gy ta ky hum words ky sath users ky answers ly sacky
for word in words: # Sary words ky ander ya jo jo word ho ga us par jy ga
    answer = input("Enter a word for" + word + ": ") # input statement ha is ly 2 string ko concatinate karwa ha 
    answers[word] = answer # Phr jo answer nay mily ha usy dictonary ma dal dia 

print(answers)


# ************* REPLACE USE FOR REPLACING ANSWERS WITH THE STORY *************

for word in words:
    story = story.replace(word,answers[word]) # Actual story ma answers replace kar dy ga words ki jagha
print(story)