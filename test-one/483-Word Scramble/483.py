# Accepted
import sys
for line in sys.stdin:
    line = line.strip('\n')
    print(' '.join([word[::-1] for word in line.split(' ')]))