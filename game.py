#VARIABLE AREA 
userHP = 50 #user's health
dead = False #Checks to see if the user is alive or not.
inventory = ["", "", ""] #Items the user can hold (could expand the list)


#Start of the game - put it in the console to see how it looks! 
print("-----------------------------")
print("|| Welcome to Pyth-Adventure!  ||") 
print("-----------------------------")


print ("-------               ---------") 
print("|      |             |          |")
print("| Play |       OR    | Tutorial |") 
print(" ------               ----------")
question = raw_input("If you want to begin playing, type play. If you want to read about the tutorial, type tutorial!").upper()
if question == "PLAY":
    print("Okay! Let's begin!")
elif question == "TUTORIAL":
    print("GOOD!")
