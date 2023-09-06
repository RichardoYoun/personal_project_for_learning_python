import csv
from random import randrange


class Word:
    def __init__(self, letters, length):
        self.word = letters
        self.length = length


class Game:
    def __init__(self):
        self.current_word = None
        self.guess = None
        self.library = []
        self.finished = []
        self.win = False
        self.load()
        self.random_select()
        

    def load(self):
        with open("words.csv", 'r') as file:
            words = csv.reader(file) 
            for word in words:
                t = []
                for letter in word[0]:
                    t.append(letter)
                w = Word(t, len(t))
                self.library.append(w)
    
    def random_select(self):
        n = len(self.library)
        i = int(randrange(n))
        while i in self.finished:
            i = int(randrange(n))
        self.current_word = self.library[i]
        self.guess = ["_"] * self.current_word.length
        
    def check_answer(self, index, letter):
        if self.current_word.word[index] == letter:
            print("correct")
            self.guess[index] = letter
            self.game_done()
        else:
            print("wrong")
            #later implement what letters have been tested


    def game_done(self):
        if self.current_word.word == self.guess:
            print(f"YOU WON! The word you were guessing was {self.current_word.word}")
            self.win = True
        
        