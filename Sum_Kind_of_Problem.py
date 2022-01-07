sets = int(input())
inputs = {}

for i in range(1, sets+1):
    value = 1
    inp = input()
    inp_list = inp.split()
    inputs[inp_list[0]] = [0, 0, 0]
    inputs[inp_list[0]][0] = int(((1+int(inp_list[1]))*int(inp_list[1])/2))
    inputs[inp_list[0]][1] = int(inp_list[1])**2
    inputs[inp_list[0]][2] = int(inp_list[1])**2 + int(inp_list[1])
for key in inputs:
    print("{} {} {} {}".format(key, inputs[key][0], inputs[key][1], inputs[key][2]))
