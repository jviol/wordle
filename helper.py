from itertools import chain

# def partition(words):
#     for word  in words:

    

with open('words_alpha.txt') as word_list:
    stripped_words = [w.strip() for w in word_list]
    five_letter_words = [w for w in stripped_words if len(w) == 5]
    four_letter_words = {w for w in stripped_words if len(w) == 4}
    three_letter_words = {w for w in stripped_words if len(w) == 3}
    plurals = [w for w in five_letter_words 
                if w[:3] in three_letter_words and w[3:] == 'es']
        # and not any(x in w for x in 'arnightck') 
        # and w[1]+w[3:] == 'oes'] 
    print(plurals)
    # print(set(chain.from_iterable(five_letter_words)))