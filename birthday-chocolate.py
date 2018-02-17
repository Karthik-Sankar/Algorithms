#Question Link - https://www.hackerrank.com/challenges/the-birthday-bar/problem
#My Submission - https://www.hackerrank.com/challenges/the-birthday-bar/submissions/code/60220772

#!/bin/python3
import itertools
import sys

def solve(n, s, d, m):
    cnt = 0
    ls = []
    magic = (n-m)+1
    for i in range(magic):
        temp = 0
        for j in range(i,i+m):
            temp = temp+s[j]
        if(temp==d):
            cnt+=1
    return cnt
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
