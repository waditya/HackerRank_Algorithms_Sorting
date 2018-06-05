#!/bin/python3
##Basic Code for Sorting
import sys

def introTutorial(V, arr):
    for i in range(0, len(arr), 1):
        if arr[i] == V:
            index = i
            break
    return(index)

if __name__ == "__main__":
    V = int(input().strip())
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = introTutorial(V, arr)
    print(result)

