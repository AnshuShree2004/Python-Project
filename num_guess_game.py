import random

print("Welcome to Number guess game..")

num_int = random.randint(1, 100)
while True:
    try:
        num = int(input("Guess the number between 1 and 100: "))
        if(num == num_int):
            print("Congratulation you got it!")
            break;
        elif(num < num_int):
            print("Too low..")
        else:
            print("Too high..")
    except ValueError:
        print("Please enter a valid number.")