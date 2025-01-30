import random

def guess_the_number():
    lower_bound = 1
    upper_bound = 100
  
    number_to_guess = random.randint(lower_bound, upper_bound)
    
    print("Welcome to 'Guess the Number'!")
    print(f"Guess a number between {lower_bound} and {upper_bound}.")
    
    attempts = 0
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

guess_the_number()