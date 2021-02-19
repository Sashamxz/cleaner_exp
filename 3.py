import random   

secretNumber =random.randint(1, 20)
print ("I have conceived a number 1-20")

for guessestTaken in range(1, 7):
    print("imput your version answer")
    try:
        guess = int(input())
    except ValueError:
        print ("please enter some integer")

    if guess < secretNumber:
        print("my integer greater than you input")
    elif guess > secretNumber:
        print("my integer smaller than you input")    
    else:
        break
if guess == secretNumber:
    print("Right!! to the number of attempts "+ str(guessestTaken) )   
else:
    print("No, you lose... " + str(secretNumber)) 
