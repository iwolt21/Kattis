import sys


def find_bracket_tax(lo, hi, taxes, income, toGive):
    """
    Finds tax bracket of friend and return how much to pay them
    :param income: income of friend
    :param lo: lowest possible tax bracket
    :param hi: highest possible tax bracket
    :param taxes: list of tax brackets and percentages
    :param toGive: how much to give friend after tax
    :return: money to pay friend before tax
    """

    mid = int((lo+hi)/2)
    if taxes[-2][0] <= income:
        tax = taxes[-1][1]
        return toGive/(1-float(tax/100))
    elif taxes[mid][0] <= income:
        return find_bracket_tax(mid, hi, taxes, income, toGive)
    elif taxes[mid][0] > income >= taxes[mid - 1][0]:
        toPay = 0
        bracket = mid
        while toGive > 0:
            if bracket == len(taxes)-1:
                toPay += toGive / (1 - float(taxes[bracket][1] / 100))
                return toPay
            least = min(toGive, taxes[bracket][0] - income)
            toPay += least/(1-float(taxes[bracket][1]/100))
            toGive -= least
            bracket += 1
        return toPay

    elif taxes[mid][0] > income:
        return find_bracket_tax(lo, mid, taxes, income, toGive)


bands = int(sys.stdin.readline())
taxes = []
for i in range(bands):
    both = sys.stdin.readline().split()
    both[0] = float(both[0])
    both[1] = float(both[1])
    taxes.append(both)
taxes.append([-1.0, float(sys.stdin.readline())])

friendsMoney = []
friends = int(sys.stdin.readline())

for i in range(friends):
    both = sys.stdin.readline().split()
    both[0] = float(both[0])
    both[1] = float(both[1])
    friendsMoney.append(find_bracket_tax(0, len(taxes)-1, taxes, both[0], both[1]))

for money in friendsMoney:
    print(money)
