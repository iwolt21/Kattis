photos = int(input())
time = 0
dist = 0
speed = 0

for i in range(photos):
    both = input().split()
    if int(both[0]) == 0 & int(both[1]) == 0:
        pass
    else:
        new_time = int(both[0])
        new_dist = int(both[1])
        if (new_dist - dist) / (new_time - time) > speed:
            speed = (new_dist - dist) / (new_time - time)
        time = new_time
        dist = new_dist
print(int(speed))
