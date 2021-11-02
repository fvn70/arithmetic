import re
from random import randint, choice

def calc(s):
    cmd = s.split()
    if len(cmd) == 3:
        a = int(cmd[0])
        b = int(cmd[2])
        if cmd[1] == '+':
            res = a + b
        elif cmd[1] == '-':
            res = a - b
        else:
            res = a * b
    else:
        a = int(cmd[0])
        res = a * a
    return res

def gen_task(l):
    if l == 1:
        ops = "+-*"
        a = randint(2, 9)
        b = randint(2, 9)
        op = choice(ops)
        t = f"{a} {op} {b}"
    else:
        a = randint(11, 29)
        t = str(a)
    print(t)
    return t

def read_level():
    while True:
        print('Which level do you want? Enter a number:')
        print('1 - simple operations with numbers 2-9')
        print('2 - integral squares of 11-29')
        l = input()
        if l in ['1', '2']:
            break
        else:
            print("Incorrect format.")
    return int(l)

cnt = 0
level = read_level()
for k in range(5):
    task = gen_task(level)
    while True:
        try:
            answer = int(input())
            if answer == calc(task):
                print("Right!")
                cnt += 1
            else:
                print("Wrong!")
            break
        except ValueError:
            print("Incorrect format.")

print(f"Your mark is {cnt}/5. Would you like to save the result? Enter yes or no.")
answer = input().lower()
if answer in ['yes', 'y']:
    name = input('What is your name?\n')
    msg = f'{name}: {cnt}/5 in level '
    if level == 1:
        msg += '1 (simple operations with numbers 2-9)'
    else:
        msg += '2 (integral squares of 11-29)'
    f_name = 'results.txt'
    fl = open(f_name, 'a')
    fl.write(msg)
    fl.close()
    print('The results are saved in "results.txt".')