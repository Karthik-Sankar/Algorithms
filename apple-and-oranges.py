# Question Link - https://www.hackerrank.com/challenges/apple-and-orange/problem
# My Submission - https://www.hackerrank.com/challenges/apple-and-orange/submissions/code/38348065
#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
ap = 0
o = 0
"""
#print(s,t)
print(m,n)
print(apple)
print(orange)"""
for i in range(m):
    #t = apple[i]+b
    temp = apple[i]+a
    if(temp>=s and temp<=t):
        ap += 1
for i in range(n):
    temp = orange[i]+b
    if(temp>=s and temp<=t):
        o += 1
print(ap)
print(o)
