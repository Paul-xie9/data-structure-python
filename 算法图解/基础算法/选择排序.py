# 选择排序
# 思想:从待排序的数据元素集合中选取关键字最小的数据元素并将它与原始数据元素集合中的第一个数据元素交换位置;
# 然后从不包括第一个位置上数据元素的集合中选取关键字最小的数据元素，并将它与原始数据元素集合中的第二个数据元素交换位置;
# 如此重复，直到数据元素集合中只剩一个数据元素为止。
# 特点:不会产生新的空间消耗，都是在原来的数组上做比较
def selectionSort(arr):
    for i in range(0, len(arr)):
        smallest = arr[i]
        for j in range(1+i, len(arr)):
            # 找出小标最小的一个元素
            if arr[j] < smallest:
                # 记录下小的元素temp
                temp = arr[j]
                arr[i] = temp
                arr[j] = smallest
                smallest = arr[i]
    return arr


if __name__ == '__main__':
    arr = [1, 4, 12, 3, 644, 323, 0,4231]
    print(selectionSort(arr))

    # res = findSmallest(arr)
    # print(res)
