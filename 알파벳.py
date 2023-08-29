import sys
input = sys.stdin.readline
text_lst = list(input())
alphabet_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(alphabet_lst)) :
    print(text_lst.count(alphabet_lst[i]),end=" ")

## 가령 ['h','e'].count('e') 는 1이다.  