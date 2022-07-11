import math


# 求解正整数的阶乘
def multiple(n):
    if n <= 0:
        return "输入错误!"
    elif n == 1:
        return n
    else:
        return n * multiple(n - 1)


# 利用双重循环输出99乘法表
def multiplicationTable(n):
    n += 1
    for i in range(1, n):
        for j in range(1, i + 1):
            print(f'{i}*{j}={i * j}\t', end='')  # 存放输出格式
        print("\n")


# 判断一个数字是否为素数
# 素数(质数):除了1与她本身之外没有其他因数
def primeNumber(n, types):
    # 方法一:遍历每一个数看余数是否为0
    if types == 0:
        for i in range(2, n):
            if n % i == 0:
                return print(n, "不是素数")
        return print(n, "是素数")
    elif types == 1:
        # 方法二:对n/2个数进行取模判断
        for i in range(2, int(n / 2) + 1):
            if n % i == 0:
                return print(n, "不是素数")
        return print(n, "是素数")
    elif types == 2:
        # 方法三:对根号下n个数进行取模运算
        t = int(math.sqrt(n))
        for i in range(2, t + 1):
            if n % i == 0:
                return print(n, "不是素数")
        return print(n, "是素数")


# 计算1,2,3,5,8,…的第n项
def sequence(n):
    if n >= 1:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return sequence(n - 1) + sequence(n - 2)
    else:
        return "error!"


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


# 找出一组数中最大的一个数
def searchMax(arr):
    # 先快速排序按照从小到大的顺序
    arr = forQuickSort(arr)
    return arr[len(arr) - 1]


# for循环快速排序
def forQuickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                less.append(arr[i])
        greater = []
        for i in range(1, len(arr)):
            if arr[i] > pivot:
                greater.append(arr[i])
        return forQuickSort(less) + [pivot] + forQuickSort(greater)


# 选择排序
# 思想:从待排序的数据元素集合中选取关键字最小的数据元素并将它与原始数据元素集合中的第一个数据元素交换位置;
# 然后从不包括第一个位置上数据元素的集合中选取关键字最小的数据元素，并将它与原始数据元素集合中的第二个数据元素交换位置;
# 如此重复，直到数据元素集合中只剩一个数据元素为止。
# 特点:不会产生新的空间消耗，都是在原来的数组上做比较
def selectionSort(arr):
    length = len(arr)
    for i in range(length):
        index = arr[i]
        for j in range(i + 1, length):
            if arr[j] < index:
                arr[i] = arr[j]
                arr[j] = index
                index = arr[i]
    return arr


if __name__ == '__main__':
    arr = [1, 3, 2, 8, 54, 232, 1, 2432, 57]
    print(selectionSort(arr))
