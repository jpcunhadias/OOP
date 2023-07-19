class Word:
    def __init__(self, secret_word):
        self.secret_word = secret_word
        self.displayed_word = ["_"] * len(secret_word)
        self.guessed_letters = []
        self.guessed_words = []

    def __str__(self):
        return "".join(self.displayed_word)

    def check_letter(self, letter):
        return letter in self.secret_word and letter not in self.guessed_letters

    def update_displayed_word(self, letter):
        for i in range(len(self.secret_word)):
            if self.secret_word[i] == letter:
                self.displayed_word[i] = letter
        self.guessed_letters.append(letter)

    def check_word(self, word):
        if word == self.secret_word:
            self.displayed_word = list(self.secret_word)
            return True
        return False

    def is_word_guessed(self):
        return "_" not in self.displayed_word

    def get_guessed_letters(self):
        return self.guessed_letters

    def get_guessed_words(self):
        return self.guessed_words

    def get_secret_word(self):
        return self.secret_word