from game import Game
from word import Word
from player import Player


def main():
    secret_word = input("Enter a secret word: ")
    game = Game(secret_word)
    game.run_game()
