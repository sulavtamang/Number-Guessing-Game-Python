"""
1. Generate a random number between 1 and 100.
2. Allow the player five guesses.
3. Provide feedback on the player's guess.
4. Assign scores based on the number of attempts.
5. Track and display all guesses after the game.
6. Prompt the player to replay or exit after each game.
"""


from random import randint


#function for setting up player
def initialize_game():
    player_name = input("\nEnter your name: ")
    ready_or_not = input(f"\nHello {player_name}!! Are you ready to play the game? (yes/no): ")

    return ready_or_not.lower().strip().startswith("y") or ready_or_not.lower().strip().startswith("o")


#this function contains the core game logic
def play_game():
    #generating random number 
    random_number = randint(1, 10)

    #scoring criteria where attempt number is mapped to scores
    attempt_score_mapping = {1 : 100, 2 : 90, 3 : 70, 4 : 50, 5 : 32,} #nitpick nit

    total_attempts = 5

    #list to store player guesses
    player_guesses = []

    #core game logic
    for attempt in range(1, total_attempts + 1):
        #asking player to guess number  
        try:
            player_guess = int(input("\nGuess the number between 1 and 10: "))
        except ValueError:
            print("\nPlease enter a valid guess.\nYou just wasted your 1 guess.\nInvalid guesses look like 12.34, d13, AGa1.23, @#aadg32.\nValid guesses look like 1, 20, 3, 5, and so on. ")
            continue

        #storing the player guess into list
        player_guesses.append(str(player_guess))

        if player_guess != random_number: #guard statement
            print(f"\nYour guess was wrong.\nNow you have {total_attempts - attempt} guesses left.")
            continue

        print(f"\nCongrats! You guessed the right number at {attempt} attempts.\nThe correct answer was {random_number}")
        print(f"Your score is {attempt_score_mapping[attempt]}%")
        print(f"Your guesses were {" ".join(player_guesses)}.")
        break

    else:
        print(f"\nYou have used all your guesses.\nRemaining guess: 0.\nYour guesses were {" ".join(player_guesses)}.")


#this function asks user for replaying the game
def play_again():
    play_again_or_not = input("\nDo you want to play again? (yes/no): ")

    return play_again_or_not.lower().strip().startswith("y") or play_again_or_not.lower().strip().startswith("o") 


#this is the main function 
def main():
    print("-----WELCOME TO THE NUMBER GUESSING GAME-----\n")

    while initialize_game():
        print()
        play_game()

        if not play_again():
            print("\nThank you for playing.\nExiting the game -------->")
            break
    else:
        print("\nExiting--->")



#calling the main function
main()