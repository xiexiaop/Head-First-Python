import math


# it_list:输入数组
# iv_value：查找的最终数值
def binarySearch(it_list, iv_value):
    low_index = 0
    high_index = len(it_list)-1

    while low_index <= high_index:
        mid_index = math.floor((low_index + high_index) / 2)
        guess = it_list[int(mid_index)]
        if guess == iv_value:
            return mid_index
        if guess > iv_value:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1

    return None


myList = [1, 3, 5, 7, 9]
result = binarySearch(myList, 7)
print(result)
if result is not None:
    print(myList[result])

