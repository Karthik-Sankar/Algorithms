#Question Link - https://www.hackerrank.com/challenges/circular-array-rotation/problem
#My Submission - https://www.hackerrank.com/challenges/circular-array-rotation/submissions/code/38264429

#!/bin/python3

import sys


n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = list (map(int, input().split()))
for a0 in range(q):
    print (a[(int(input()) + n - k) % n])
