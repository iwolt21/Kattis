import sys

cases = int(sys.stdin.readline())

for i in range(cases):
    ant_pos = []
    info = sys.stdin.readline().split()
    length = int(info[0])
    ants = int(info[1])
    while len(ant_pos) < ants:
        ant_pos.extend(sys.stdin.readline().split())
    ant_pos = [int(ant) for ant in ant_pos]

    # Shortest distance
    shortest_list = [min(ant, length - ant) for ant in ant_pos]
    shortest_list.sort()
    ant_pos.sort()

    # Longest distance
    """
    longest = 0
    for j in range(len(ant_pos)):
        if j != len(ant_pos)-1:
            longest += (ant_pos[j+1]-ant_pos[j])/2
        else:
            longest = int(length-ant_pos[j]+longest+longest)
    """
    longest = max(ant_pos[ants-1], length - ant_pos[0])
    print(shortest_list[-1], longest)
