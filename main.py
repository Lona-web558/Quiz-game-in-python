print("Welcome to my Quiz in python")

playing = input("Do you want to play?")

if playing == "no":
    quit()


print("Okay,then Let's play!!")
score = 0

answer = input("What is computer science?")
if answer == "the study of computers and how they work":
    print("correct")
    score +=1
else:
    print("incorrect")

answer = input("what is matter?")
if answer == "anything that occupies space and is made up of various particles":
    print("correct")
    score +=1
else:
    print("incorrect")

answer = int(input("How many teeth do humans have?"))
if answer == 32:
    print("correct")
    score +=1
else:
    print("incorrect")

print("You got" + str(score) + "questions correct!")
print("You got" + str((score/3)*100 )+ "%")
