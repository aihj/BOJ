num = int(input())
string = input()

check = ["*", "+", "/", "-"]

dic = {}
li = []

for s in string:
    if s in check:
        first = li.pop()
        second = li.pop()

        if s == "+":
            li.append(second + first)

        elif s == "-":
            li.append(second - first)

        elif s == "*":
            li.append(second * first)

        elif s == "/":
            li.append(second / first)

    else:
        if s not in dic:
            dic[s] = int(input())

        li.append(dic[s])

print("%0.2f" % (li[0]))
 