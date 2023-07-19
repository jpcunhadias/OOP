from word import Word
from player import Player


class Game:
    def __init__(self, secret_word):
        self.word = Word(secret_word)
        self.player = Player("Player 1")
        self.guesses = 0
        self.max_guesses = 6
        self.wrong_guesses = 0

    def start_game(self):
        print(f"Welcome to Hangman, {self.player.get_name()}!")
        print(f"Your secret word has {len(self.word.get_secret_word())} letters.")
        print(f"{' '.join(self.word.displayed_word)}")
        print(f"You have {self.max_guesses} guesses.")
        print(f"{' '.join(self.word.get_guessed_letters())}")
        print(f"{' '.join(self.word.get_guessed_words())}")

    def play_game(self):
        while self.wrong_guesses < self.max_guesses:
            letter = input("Guess a letter: ")
            if self.word.check_letter(letter):
                self.word.update_displayed_word(letter)
                print(f"{' '.join(self.word.displayed_word)}")
                print(f"{' '.join(self.word.get_guessed_letters())}")
                print(f"{' '.join(self.word.get_guessed_words())}")
                if self.word.is_word_guessed():
                    print("You win!")
                    self.player.increase_score()
                    break
            else:
                self.wrong_guesses += 1
                print(f"{' '.join(self.word.displayed_word)}")
                print(f"{' '.join(self.word.get_guessed_letters())}")
                print(f"{' '.join(self.word.get_guessed_words())}")
                print(f"Wrong guesses: {self.wrong_guesses}")
        else:
            print(f"You lose! The secret word was {self.word.get_secret_word()}.")
            self.player.reset_score()

    def end_game(self):
        print(f"Your score is {self.player.get_score()}.")
        print("Thanks for playing!")

    def reset_game(self, secret_word):
        self.word = Word(secret_word)
        self.guesses = 0
        self.wrong_guesses = 0

    def run_game(self):
        self.start_game()
        self.play_game()
        self.end_game()
        while input("Play again? (y/n) ") == "y":
            self.reset_game(input("Enter a new secret word: "))
            self.start_game()
            self.play_game()
            self.end_game()