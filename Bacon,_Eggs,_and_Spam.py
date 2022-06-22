import sys
"""
customers = int(sys.stdin.readline())
while customers != 0:
    people = []
    for i in range(customers):
        people.append(sys.stdin.readline().split())
    final = []
    for person in people:
        for i in range(1, len(person)):
            final.append((person[i], person[0]))
    final.sort(key=lambda x: (x[0], x[1]))
    sec_final = []
    index = -1
    for tup in final:
        if index == -1 or sec_final[index][0] != tup[0]:
            index += 1
            sec_final.append([tup[0], tup[1]])
        else:
            sec_final[index].append(tup[1])
    for food in sec_final:
        print(" ".join(food))
    print("")

    customers = int(sys.stdin.readline())
"""

customers = int(sys.stdin.readline())
while customers != 0:
    orders = {}
    for i in range(customers):
        person = sys.stdin.readline().split()
        for i in range(1, len(person)):
            if person[i] not in orders:
                orders[person[i]] = [person[0]]
            else:
                orders[person[i]].append(person[0])
    for food in orders.keys():
        orders.get(food).sort()
    orders = {key:orders[key] for key in sorted(orders.keys())}

    for food, names in orders.items():
        print(food, " ".join(names))
    print("")
    customers = int(sys.stdin.readline())
