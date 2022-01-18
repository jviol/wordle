import sys
import wordle
import random
from itertools import chain
from collections import Counter
import string

def partition_words(pivot_word, words):
    overlap_count = sum(any(c in w) for w in words for c in pivot_word)
    return min(overlap_count, len(words)-overlap_count)

def maximize_letter_frequency(words):
    letter_frequencies = Counter(chain.from_iterable(words))
    return max(words, key=lambda w: sum(letter_frequencies[c] for c in set(w)))

def maximize_nonshared_letters(illegal_letters, words):
    legal_letters = set(string.ascii_lowercase) - illegal_letters
    nonshared_letters = [c for c in legal_letters if not all(c in w for w in words)]
    # legal_words = [w for w in wordle.words if not any(c in illegal_letters for c in w)]
    return max(words, key=lambda w:sum(c in w for c in nonshared_letters))

def play(verbose=True, stop_on_fail=False):
    word_length = 5
    possible_words = wordle.words
    guess_words = possible_words[:]
    game = wordle.Game()
    illegal_letters = set()
    known_positions = {}
    possible_positions = {}
    guesses = []
    answers = []
    illegal_positions = []
    dont_guess_positions = []
    while True:
        try:
            if game.guesses == 0:
                guess = 'arose'
            elif game.guesses == 1:
                guess = 'night'
            # elif game.guesses == 2:
            #     guess = 'lucky'
            else:
                # if len(possible_words) <= 2:
                #     if verbose:
                #         print('Possible words:', possible_words)
                #     guess = possible_words[0]
                # elif guess_words:
                #     guess = maximize_letter_frequency(guess_words)
                #     if verbose:
                #         print('Guess Word:', guess)
                # #better_choices = [w for w in words if len(set(w)) == word_length]
                # else:
                guess = maximize_nonshared_letters(illegal_letters, possible_words) #random.choice(better_choices or words)
            if verbose:
                print('Guess: ', guess)
            guesses.append(guess)
            answer = game.make_guess(guess)
            answers.append(answer)
            if verbose:
                print('Answer:', answer)
            if answer.lower() == guess:
                if verbose:
                    print(f"Got the correct word in {game.guesses} tries.")
                if game.guesses > 6 and stop_on_fail:
                    print(guesses)
                    print(answers)
                    exit()
                return game.guesses
            # if stop_on_fail and game.guesses == 5:
            #     verbose = True

            illegal_letters.update(a for a,b in zip(guess, answer) if b == '-' and a not in answer.lower())
            known_positions.update({i:c.lower() for i,c in enumerate(answer) if c.isupper()})
            #print(known_positions)
            for i,c in enumerate(answer):
                if c.islower():
                    illegal_positions.append((c,i))
                    dont_guess_positions.append((c,i))
                    if c not in possible_positions:
                        possible_positions[c] = set(range(word_length))
                    try:
                        possible_positions[c].remove(i)
                    except KeyError:
                        pass

            for k,v in possible_positions.items():
                for i,c in known_positions.items():
                    if c != k:
                        try:
                            v.remove(i)
                        except KeyError:
                            pass
            # if verbose:
            #     print(known_positions)
            guess_words = [w for w in guess_words 
                        if not any(x in illegal_letters for x in w)
                            and not any(w[i] == c for c,i in illegal_positions)
                            and not any(c in known_positions.values() for c in w)]
            # if verbose:
            #     print(guess_words)
            possible_words = [w for w in possible_words 
                        if not any(x in illegal_letters for x in w) 
                            and all(w[k] == v for k,v in known_positions.items()) #or game.guesses < 3)
                            and all(x in [c for i,c in enumerate(w) if i in ps] for x,ps in possible_positions.items())
                            and not any(w[i] == c for c,i in illegal_positions)
                            and w != guess]
            assert possible_words
        except KeyboardInterrupt:
            raise

def keep_playing(stop_on_fail):
    S = 0
    N = 0
    while True:
        try:
            S += (play(verbose=False, stop_on_fail=stop_on_fail) > 6)
            N += 1
            average = S / N
            print("{:.4f}".format(average), N, end='\r')
        except KeyboardInterrupt:
            print("{:.4f}".format(average), N)
            break

if len(sys.argv) > 1:
    if sys.argv[1].startswith('k'):
        keep_playing(False)
    elif sys.argv[1].startswith('s'):
        keep_playing(True)
play()
