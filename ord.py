import string

with open('RO2012.opslagsord.med.homnr.og.ordklasse.txt', encoding='utf-8') as f:
    alfabet = set(string.ascii_lowercase + 'æøå')
    ord = (line.split(';')[0] for line in f)
    ord = (line.split('.')[1] if '.' in line else line for line in ord)
    fem_bogstavs_ord = [w for w in ord if len(w) == 5 and all(c in alfabet for c in w)
        and not any(c in w for c in 'butmlongris')
        and all(c in w for c in 'ke')
        # and w[2] == 's'
    ]
    
print(fem_bogstavs_ord)