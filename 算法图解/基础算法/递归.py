# 倒计时
def count(num):
    print(num)
    if num <= 0:
        return
    else:
        count(num - 1)


# 阶乘
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


if __name__ == '__main__':
    print(factorial(5))
