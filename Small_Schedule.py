import math
import sys

dataArray = sys.stdin.readline().split()
longs = int(dataArray[3])
shorts = int(dataArray[2])
longTime = int(dataArray[0])
slots = int(dataArray[1])
slotTimes = []
maxTime = 0
for i in range(slots):
    slotTimes.append(0)

while longs>0:
    for i in range(slots):
        if longs>0:
            slotTimes[i]+=longTime
            longs-=1
        else:
            maxTime = slotTimes[i-1]
            break
while shorts>0:
    for i in range(slots-1,-1,-1):
        if shorts>0:
            if maxTime-slotTimes[i]==0:
                perSlot = math.ceil(float(shorts)/slots)
                least = min(shorts, perSlot)
                slotTimes[i] += least
                shorts -= least
                maxTime = slotTimes[i]
            else:
                least = min(shorts, maxTime-slotTimes[i])
                slotTimes[i] += least
                shorts -= least
        else:
            break
slotTimes.sort()
print(slotTimes[-1])
