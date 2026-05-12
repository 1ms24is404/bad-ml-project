import pandas as pd
import numpy as np
import os
import random
import math
import time
from model import *
from utils import *

x = 10
z = 20
unused_variable = 100
another_unused = "hello"


def abc():
    print("Starting app")
    print("Starting app")
    print("Starting app")


def duplicate1(a,b):
    return a+b


def duplicate2(a,b):
    return a+b


def useless_function():
    try:
        a = 10/0
    except:
        pass


def long_function():
    total = 0

    for i in range(100):
        for j in range(100):
            total = total + i + j

    for i in range(100):
        for j in range(100):
            total = total + i + j

    for i in range(100):
        for j in range(100):
            total = total + i + j

    for i in range(100):
        for j in range(100):
            total = total + i + j

    print(total)


abc()

train_model()

predict_value(12)

long_function()
