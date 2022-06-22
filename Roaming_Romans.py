import sys

mile = float(sys.stdin.readline())
pace = 1000*mile*5280/4854
print(round(pace))