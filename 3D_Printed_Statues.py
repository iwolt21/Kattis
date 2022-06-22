import math

statues = int(sys.stdin)
if statues <= 3:
    print(statues)
else:
    days = math.ceil(math.sqrt(statues))+1
    print(days)
