# 利用Divide && Conquer实现快速排序


def quickSort(array):
    # 基线条件 Base Condition
    if len(array) < 2:
        return array

    pivot = array[0]
    # 分区 Partitioning
    left = []
    right = []
    for element in array:
        if (element < pivot):
            left.append(element)
        elif (element > pivot):
            right.append(element)
    return quickSort(left) + [pivot] + quickSort(right)


print(quickSort([
    3,
    1,
    10,
    9,
]))
