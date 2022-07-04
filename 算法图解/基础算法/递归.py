# 倒计时
def count(num):
    print(num)
    if num <= 0:
        return
    else:
        count(num - 1)


if __name__ == '__main__':
    count(10)
