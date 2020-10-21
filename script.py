from random import random

for x in range(0,10000):
    print(str(random()*32767).split('.')[0])
