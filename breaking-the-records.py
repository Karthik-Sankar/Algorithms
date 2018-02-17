#Question Link - https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
#My Submission Link - https://www.hackerrank.com/challenges/breaking-best-and-worst-records/submissions/code/60216624

#!/bin/python3

import sys

def getRecord(s):
    mx = s[0]
    mn = s[0]
    mx_c =0
    mn_c =0
    for i in range(len(s)):
        temp = list(s[:i+1])
        if(max(temp)>mx):
            mx=max(temp)
            mx_c += 1
        if(min(temp)<mn):
            mn=min(temp)
            mn_c += 1
    return [mx_c, mn_c]

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
