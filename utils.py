import os
import sys
import random
import math


def helper():
    print("helper")


def helper2():
    print("helper")


def helper3():
    print("helper")


def calculate(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
    result = a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p
    return result


def bad_loop():
    arr = []

    for i in range(1000):
        arr.append(i)

    for i in range(len(arr)):
        print(arr[i])
