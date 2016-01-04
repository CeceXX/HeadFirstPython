# sketch.py

man = []
other = []

try:
    data = open('sketch.txt')

    for line in data:
        try:
            (role, line_spoken) = line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
except IOError:
    print('The data file is missing!')

try:
    manFile = open("manScript.txt", 'w')
    otherFile = open('otherManScript.txt', 'w')
    print(man, file=manFile)
    print(other, file=otherFile)
except IOError:
    print("I couldn't write to the file")
finally:
    manFile.close()
    otherFile.close()
    
