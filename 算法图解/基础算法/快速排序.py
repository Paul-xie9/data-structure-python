# 快速排序
def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        # 假设基准点
        pivot = arr[0]
        # 找出小于基准点
        less = [i for i in arr[1:] if i <= pivot]
        # 大于基准点
        greater = [i for i in arr[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


if __name__ == '__main__':
    arr = [53, 32, 3, 11, 65, 31, 7, 5, 56]
    print(quickSort(arr))
