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


if __name__ == '__main__':
    print(sequence(-1))
