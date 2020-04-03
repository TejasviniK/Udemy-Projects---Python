from random import randint

num = randint(1,100)
print(num)
Guess_list = []
while True:
    guess = int(input("Enter the guess:"))
    Guess_list.append(guess)
    print(Guess_list)

    if(guess == num) :
        print("Congrats!! You have guessed it correctly in {} guesses".format(len(Guess_list)))
        break
    
    elif((guess < 1) or (guess > 100)) :
        print("OUT OF BOUNDS")

    elif(len(Guess_list) == 1) :
        if(abs(num-guess) <= 10):
            print("WARM!")
        else :
            print("COLD!")

    else :
        if((abs(num-Guess_list[-2])) > (abs(num-guess))):
            print("WARMER!")
        else :
            print("COLDER!")
   