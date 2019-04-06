# Divide && Conquer分而治之小例子
# 将问题规模逐步缩小无限接近与基准条件


def sum(array):
    if len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    length = len(array)
    return array[0] + sum(array[1:length])


print(sum([1, 2, 3, 4]))
