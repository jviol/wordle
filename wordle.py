import random
import sys

if len(sys.argv) > 1:
    word_length = int(sys.argv[1])
else:
    word_length = 5

with open('words_alpha.txt') as word_list:
    stripped_words = (w.strip() for w in word_list)
    words = [w for w in stripped_words if len(w) == word_length]

class Game:
    def __init__(self) -> None:
        self._correct_word = random.choice(words)
        self.guesses = 0

    def make_guess(self, guess) -> str:
        if guess not in words:
            raise ValueError(f"Guess must be a {word_length} letter word appearing in the wordlist")
        self.guesses += 1
        res = ['-']*word_length
        cw = list(self._correct_word)
        for i,(g,c) in enumerate(zip(guess, self._correct_word)):
            if g == c:
                res[i] = g.upper()
                cw.remove(c)
        for i, g in enumerate(guess):
            if g in cw and res[i] == '-':
                res[i] = g.lower()
                cw.remove(g)
        return ''.join(res)

# if __name__ == "__main__":
#     game = Game()
#     print(f"Guess a {word_length}-letter word!")
#     guess = input()
#     answer = game.make_guess(guess)
#     print(answer)
    

    