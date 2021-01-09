import nltk
from collections import Counter

txt = open("output.txt").read().replace(',','').replace('.','').replace(';','')

tokenized = nltk.word_tokenize(txt)
total = len(tokenized)
top = Counter(tokenized).most_common(10)
print('\n'.join([g[0] for g in top]))
print(sum([g[1] for g in top]) * 100 / total)