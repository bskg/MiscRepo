from collections import Counter

lines = open("chat.txt").read().replace("Avatar","").replace(".", " ").split("\n")
b = []
s = []

s_talking = False
for i in range(len(lines)):
    if lines[i][:7] == "bjorn96":
        s_talking = False
        continue
    if lines[i][:4] == "weir":
        s_talking = True
        continue

    if s_talking:
        s.append(lines[i])
    else:
        b.append(lines[i])

b_words = ' '.join(b).split(' ')
s_words = ' '.join(s).split(' ')
bc = Counter(b_words)
sc = Counter(s_words)

for w in sc.keys():
    sc[w] = sc[w] / (bc[w]+0.00001)
print(sc.most_common(100))
