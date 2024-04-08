#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#

def findSum(numbers, queries):
    # Write your code here
    result = [] # for gather the result
    for i in queries: #loop the queries to get index start and index end
      result_sum = 0 # for gather the result of array which is will sum
      for j in range(i[0], i[1]+1): #loop the index of array number by index start and index end
        if i[0] == i[1]: #if the index start and index end same will loop one again to add result with 10
          for i in range(1):
            if(numbers[j-1]) == 0:
              result_sum = result_sum + 10
            else:
              result_sum = result_sum + numbers[j-1]
        if(numbers[j-1]) == 0: # if the numbers is 0 add with 10
          result_sum = result_sum + 10
        else: #if not just sum all the numbers we need
          result_sum = result_sum + numbers[j-1]
        
      result.append(result_sum)
      
          
    return(result)
    
case_1 = findSum([20,30,0,10], [[1,3]])
case_2 = findSum([-5,0], [[2,2],[1,2]])

print(f"case_1 {case_1}")
print(f"case_2 {case_2}")


# i comment because i haven't done it yet fckkk
# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     numbers_count = int(input().strip())

#     numbers = []

#     for _ in range(numbers_count):
#         numbers_item = int(input().strip())
#         numbers.append(numbers_item)

#     queries_rows = int(input('queries row').strip())
#     queries_columns = int(input('queries col').strip())

#     queries = []

#     for _ in range(queries_rows):
#         queries.append(list(map(int, input().rstrip().split())))

#     print(queries)
#     result = findSum(numbers, queries)

#     # fptr.write('\n'.join(map(str, result)))
#     # fptr.write('\n')

#     # fptr.close()
