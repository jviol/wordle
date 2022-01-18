with open('words_alpha.txt') as f:
    for line in f:
        w = line.strip()
        if len(w) == 5:
            print(w.lower())