import sys

trees = {}
total = 0
for tree in sys.stdin:
    tree = tree.strip()
    total += 1
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

trees = {key: trees[key] for key in sorted(trees.keys())}
for tree in trees:
    print(tree, round(trees[tree]/total*100, 6))
