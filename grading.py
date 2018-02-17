#!/bin/python3
#Difficulty Level - Easy
#Quesstion Link - https://www.hackerrank.com/challenges/grading/problem
#My Submission Link - https://www.hackerrank.com/challenges/grading/submissions/code/52600497
import sys

def solve(grades):
    # Complete this function
    res = []
    nf = 0
    for i in grades:
        if(i<38):
            res.append(i)
        else:
            nf = int(i/10)
            if(int(i%10)>=5):
                nf = nf+1
                nf = nf*10
            else:
                nf = nf*10+5
            if((nf-i)<3):
                res.append(nf)
            else:
                res.append(i)
    return res

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
