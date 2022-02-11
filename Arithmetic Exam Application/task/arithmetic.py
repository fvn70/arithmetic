# Stage 2
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


def gen_task():
    ops = "+-*"
    a = randint(2, 9)
    b = randint(2, 9)
    op = choice(ops)
    t = f"{a} {op} {b}"
    print(t)
    return t


cnt = 0
for k in range(5):
    task = gen_task()
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
print(f"Your mark is {cnt}/5.")