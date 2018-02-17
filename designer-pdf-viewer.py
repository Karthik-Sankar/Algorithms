#Question Link - https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
#My Submission - https://www.hackerrank.com/challenges/designer-pdf-viewer/submissions/code/38431581

#!/bin/python3

import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()
hn = []
for i in range(len(word)):
    t = h[ord(word[i])-97]
    hn.append(t)
ht = max(hn)
print(len(word)*ht)
