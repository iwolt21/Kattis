import sys

nums = sys.stdin.readline().split()
task_times = sys.stdin.readline().split()
quiet_times = sys.stdin.readline().split()

task_times = [int(i) for i in task_times]
quiet_times = [int(i) for i in quiet_times]

task_times.sort()
quiet_times.sort()
count = 0
"""
for task in task_times:
    lo = 0
    hi = len(quiet_times)-1
    while len(quiet_times) > 0:
        mid = (lo + hi) // 2
        if task <= quiet_times[mid]:
            hi = mid
        elif task > quiet_times[mid]:
            lo = mid+1
        if lo == hi:
            if task <= quiet_times[lo]:
                count += 1
                quiet_times = quiet_times[lo + 1:]
            elif lo > 0 and task <= quiet_times[lo-1]:
                count += 1
                quiet_times = quiet_times[lo:]
            break
print(count)
"""

for task in task_times:
    while len(quiet_times) > 0:
        quiet = quiet_times.pop(0)
        if task <= quiet:
            count += 1
            quiet_i = 0
            break
print(count)
