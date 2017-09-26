from collections import Counter

n = int(input())
bou_array = list(map(int, input().split()))

bou_collection = Counter(bou_array)

len_square = 0
len_array = []

for id, value in bou_collection.items():
    if value >= 4 :
        len_array.append(id)
        len_array.append(id)

    elif value >= 2 :
        len_array.append(id)

len_array = sorted(len_array)[::-1]

if len(len_array) < 2 :
    print(0)
else:
    ans_rectangle = len_array[0] * len_array[1]
    print(ans_rectangle)

##  https://beta.atcoder.jp/contests/arc081/tasks/arc081_a
