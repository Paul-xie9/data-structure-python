# 线性表:由若干个【相同类型】的元素组成的有限序列

# ===================初始化顺序表=============================
def _init_(self):
    self.SeqList = []


# ===================创建顺序表=============================
def CreateSequenceList(self):
    print("==== 请输入数据后按回车确认,若想结束请输入“#” ====")
    Element = input("请输入元素:")
    while Element != '#':
        self.SeqList.append(int(Element))
        Element = input("请输入元素:")


# ===================查找顺序表元素=============================
def FindElement(self):
    key = int(input("请输入想要查找的元素值:"))
    if key in self.SeqList:
        ipos = self.SeqList.index(key)
        print("查找成功!值为", self.SeqList[ipos], "的元素,位于当前顺序表的第", ipos + 1, "个位置.")
    else:
        print("查找失败!当前顺序表不存在值为", key, "的元素.")


# ===================插入元素到顺序表中=============================
def InsertElement(self):
    iPos = int(input("请输入待插入元素的位置:"))
    Element = int(input("请输入待插入元素的值:"))
    self.SeqList.insert(iPos, Element)
    print("插入元素之后,当前顺序表的值为:\n", self.SeqList)


# ===================删除顺序表中指定位置元素=============================
def DeleteElement(self):
    dPos = int(input("请输入待删除的元素位置:"))
    print("正在删除元素", self.SeqList[dPos], "...")
    self.SeqList.remove(self.SeqList[dPos])
    print("删除后顺序表为:\n", self.SeqList)


# ===================遍历顺序表元素=============================
def TraverseElement(self):
    SeqLitLen = len(self.SeqList)
    print("=================遍历顺序表中的元素========================")
    for i in range(SeqLitLen):
        print("第", i + 1, "个元素的值为:", self.SeqList[i])


# ===================求出顺序表最大元素=============================
def MaxAndMinSequence(self):
    maxNum = self.SeqList[0]
    minNum = self.SeqList[0]
    for j in range(len(self.SeqList)):
        if maxNum < self.SeqList[j]:
            maxNum = self.SeqList[j]
        if minNum > self.SeqList[j]:
            minNum = self.SeqList[j]
    print("最大值为:", maxNum)
    print("最小值为:", minNum)


# 顺序表结构
class SequenceList:
    SeqList = []


# 顺序表的操作
def SequenceOperate():
    print("==== 顺序表 ====")
    print("===== 初始化顺序表 =====")
    _init_(SequenceList)
    print("==== 请输入对于的数字操作 ====")
    print("1.创建顺序表\n2.查找\n3.插入元素\n4.删除元素\n5.遍历元素\n6.最大值和最小值\n110.退出")
    num = int(input("开始输入:"))
    while num != 110:
        if num == 1:
            print("===== 创建顺序表 =====")
            CreateSequenceList(SequenceList)
        if num == 2:
            print("==== 查找元素 ====")
            FindElement(SequenceList)
        if num == 3:
            print("==== 插入元素 ====")
            InsertElement(SequenceList)
        if num == 4:
            print("==== 删除元素 ====")
            DeleteElement(SequenceList)
        if num == 5:
            print("==== 遍历元素 ====")
            TraverseElement(SequenceList)
        if num == 6:
            print("==== 最大值 ====")
            MaxAndMinSequence(SequenceList)
        print("\n==== 请输入对于的数字操作 ====")
        print("1.创建顺序表\n2.查找\n3.插入元素\n4.删除元素\n5.遍历元素\n6.最大值和最小值\n110.退出")
        num = int(input("开始输入:"))


if __name__ == '__main__':
    SequenceOperate()
