import sys

info = sys.stdin.readline().split()
while info != ["0", "0"]:
    info[0] = int(info[0])
    info[1] = int(info[1])
    heads = []
    knights = []
    for i in range(info[0]):   #For each head...
        heads.append(int(sys.stdin.readline()))
    for j in range(info[1]):    #For each knight...
        knights.append(int(sys.stdin.readline()))
    heads.sort()
    knights.sort()

    if len(heads) > len(knights):
        print("Loowater is doomed!")
    else:
        coins = 0
        skipped = 0
        diff = len(knights)-len(heads)
        for i in range(len(heads)):
            while heads[i] > knights[i+skipped] and skipped <= diff:
                skipped += 1
            coins += knights[i+skipped]
            if skipped > diff:
                print("Loowater is doomed!")
                break
        if skipped <= diff:
            print(coins)
    info = sys.stdin.readline().split()
