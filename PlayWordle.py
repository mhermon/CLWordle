from Game import Game
import sys 

NUMBER_OF_GUESSES = 6
CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K' 

if __name__ == '__main__':

    game = Game()
    game.print_board()
    won = False

    while game.get_number_of_guesses() < NUMBER_OF_GUESSES:
        to_delete = 16
        while True:
            guess = input("Guess a word: ")
            if len(guess) != 5:
                print("Invalid word length")
                to_delete += 2
                continue
            if guess.isalpha() == False:
                to_delete += 2
                print("Invalid word")
                continue
            if guess.lower() not in game.dictionary:
                to_delete += 2
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

            # Clear last round 
            for i in range(to_delete):
                sys.stdout.write(CURSOR_UP_ONE) 
                sys.stdout.write(ERASE_LINE) 
            game.print_board()
            
        
        
        # Clear the screen
        

    
    if not won:
        print("You ran out of turns!")
        print(f"The word was {game.get_answer_word()}")
    

        


