inp = input()
listInp = list(inp)
revList = []
for i in range(len(inp)):
    revList.append(listInp[len(inp)-i-1])
revInp = "".join(revList)
print(revInp)
