#!/bin/python3

import math
import os
import random
import re
import sys

    

if __name__ == '__main__':
    
    n = int(input().strip())

    if (n%2) != 0:
        print("Weird")
    elif (1<n<6) & (n%2) == 0:
        print("Not Weird")
    elif (5<n<21):
        print("Weird")
    else:
        print("Not Weird")
   
