from collections import Counter
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot
import string

with open('RO2012.opslagsord.med.homnr.og.ordklasse.txt', encoding='utf-8') as f:
    alfabet = set(string.ascii_lowercase + 'æøå')
    ord = (line.split(';')[0] for line in f)
    five_letter_words = [w for w in ord if len(w) == 5 and all(c in alfabet for c in w)]
        # and not any(c in w for c in 'grnpatm')
        # and all(c in w for c in 'iles')]
    
letter_counts = sorted(Counter(''.join(five_letter_words)).items(), key=lambda x:x[1])
letters, counts = zip(*letter_counts)
y_pos = range(len(letter_counts))
pyplot.bar(y_pos, counts)
pyplot.xticks(y_pos, letters)
pyplot.show()