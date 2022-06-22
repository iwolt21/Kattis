import sys

fn_count = {}
names = []
for name in sys.stdin:
    name = name.strip().split()
    names.append(name)
    if name[0] in fn_count:
        fn_count[name[0]] += 1
    else:
        fn_count[name[0]] = 1
names.sort(key=lambda x: (x[1], x[0]))
for name in names:
    if fn_count[name[0]] > 1:
        print(name[0], name[1])
    else:
        print(name[0])
