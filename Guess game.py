from Equal import  isEqual
from random import randint
num = randint(0, 101)
Bingo = 1
while Bingo != 0:
    answer = int(input('Please key in the number:'))
    Bingo = isEqual(answer, num)
