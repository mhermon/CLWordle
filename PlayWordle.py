from Game import Game

NUMBER_OF_GUESSES = 6

if __name__ == '__main__':

    game = Game()
    game.print_board()
    won = False

    while game.get_number_of_guesses() < NUMBER_OF_GUESSES:
        while True:
            guess = input("Guess a word: ")
            if len(guess) != 5:
                print("Invalid word length")
                continue
            if guess.isalpha() == False:
                print("Invalid word")
                continue
            if guess.lower() not in game.dictionary:
                print("Invalid word")
                continue
            else:
                break
        if game.make_guess(guess):
            print("You win!")
            won = True
            game.print_board()
            break
        else:
            print("Try again!")
            game.print_board()
    
    if not won:
        print("You ran out of turns!")
        print(f"The word was {game.get_answer_word()}")
    

        


