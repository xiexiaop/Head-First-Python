# 递归必须具备2个条件：
# 1.Base Condition[基线/退出条件]
# 2.Recursion Condition[递归条件]


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(4))
