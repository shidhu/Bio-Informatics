# -*- coding: utf-8 -*-
"""
@author: Pranta Sarker

"""

from __future__ import print_function;
from random import *;

RNA = {
1: 'A',
2: 'U',
3: 'C',
4: 'G'
}

fl = False;

while True:
    k = input('Enter the length to see the RNA sequence (Press 0 to end) : ');
    if k == 0:
        if fl == True:
            print("Checking finish! End console", end="\n");
        else:
            print("Not checked, End console", end="\n");
        break;
    
    for i in range(0 , k):
        fl =True;
        n = randint(1 , 4);
        print(RNA[n] , end = " ");
    print("\n");

