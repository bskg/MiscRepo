import numpy as np

def experiment():
    s = 0
    i = 0
    while s <= 1:
        s += np.random.uniform(0, 1)
        i += 1
    return i

for r in [3, 7, 15, 35]:
    for i in range(5):
        s = [experiment() for _ in range(r)]
        print(s, np.mean(s))