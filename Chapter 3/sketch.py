# sketch.py

data = open('sketch.txt')

for line in data:
    (role, line_spoken) = line.split(':', 1)
    print(role, end='')
    print(' said: ', end='')
    print(line_spoken, end='')

