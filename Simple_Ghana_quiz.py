print("Hello! Welcome to Ros Quiz!","This quiz would test your knowledge on the regions in Ghana.")
play = input (str("Would you like to begin? "))
if play.lower() == "yes":
    user = input (str("Please type your name: "))
    print ("Enjoy this game", user+"!")
    score = 0
else:
    print("Thanks for joining!")
    quit()

ques1 = int(input("How many regions are in Ghana? "))
if ques1 == 16:
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")

ques2 = input("Which region speaks the language 'ewe'? ")
if ques2.lower == "volta" or "volta region":
    print ("Correct!")
    score += 1

ques3 = input("Which region has the Mole National Park? ")
if ques3.lower == "northern" or "northern region":
    print ("Correct!")
    score += 1

ques4 = input("Which region is known for its rich wealth? ")
if ques4.lower == "ashanti" or "ashanti region":
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")
    
ques5 = input("In which region is the capital city of Ghana found? ")
if ques4.lower == "greater accra" or "greater" or "greater accra region":
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str((score)/5 * 100) + "%")




    
    
    
