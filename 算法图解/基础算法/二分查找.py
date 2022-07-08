# list:数组，item:需要查找到元素
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = mid
        if list[guess] == item:
            return "元素" + str(item) + "找到了,位于数组的第" + str((guess + 1)) + "个位置处。"
        elif list[guess] > item:
            high = mid - 1
        elif list[guess] < item:
            low = mid + 1
        else:
            return "数组中没有你要查找的" + str(item) + "元素"

if __name__ == '__main__':
    my_list = [1, 3, 4, 6, 21, 23, 34, 35]
    result = binary_search(my_list, 34)
    print(result)
