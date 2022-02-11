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

print(calc(input()))
