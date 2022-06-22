papers = int(input())
cites = []
count = 0
for i in range(papers):
    cites.append(int(input()))

cites.sort(reverse=True)
for i in range(len(cites)):
    if cites[i] >= i+1:
        count = i+1
print(count)
