from collections import Counter
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot

with open('words_alpha.txt') as word_list:
    stripped_words = (w.strip() for w in word_list)
    five_letter_words = [w for w in stripped_words if len(w) == 5]

letter_counts = sorted(Counter(''.join(five_letter_words)).items(), key=lambda x:x[1])
letters, counts = zip(*letter_counts)
y_pos = range(len(letter_counts))
pyplot.bar(y_pos, counts)
pyplot.xticks(y_pos, letters)
pyplot.show()