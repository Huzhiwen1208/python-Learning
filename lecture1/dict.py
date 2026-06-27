# 目的：学会使用字典
# 题目：http://43.142.151.52/problem/G1050

count = {}

# 换行读
n = eval(input())
for i in range(n):
    item = eval(input())

    # get方法判断 item 是否出现过
    # count[item] 表示访问 出现次数
    if count.get(item) is None:
        count[item] = 1
    else:
        count[item] = count[item] + 1

for key in count:
    value = count[key]
    print(key, value)