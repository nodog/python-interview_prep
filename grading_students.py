#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    rounded_grades = []
    for g in grades:
        if (g > 37) and (g % 5 > 2):
            g = round(g/5)*5
        rounded_grades.append(g)

    return rounded_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
