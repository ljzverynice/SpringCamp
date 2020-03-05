    #小顶堆
def Heap(target):
    newlist = []
    newlist.extend(target)
    def swap(a,b):
        temp = newlist[a]
        newlist[a] = newlist[b]
        newlist[b] = temp
    def downTree(i):
        n = len(newlist) -1
        while True:
            j = i
            if 2*i +1 <=  n and newlist[2*i + 1] < newlist[j]:
                j = 2*i +1
            if 2*i +2 <=  n and newlist[2*i + 2] < newlist[j]:
                j = 2*i + 2
            if j == i:
                break
            swap(i,j)
            i = j
    for i in range(len(newlist)//2,-1,-1):
        downTree(i)
    print(newlist)

    #栈
class Stack():
    def __init__(self,target=[]):
        self.list1 = target
    def pop(self):
        if(len(self.list1)):
            temp = self.list1[-1]
            self.list1 =  self.list1[:-1]
            return temp
        else:
            print("please push somethingfirst!")
    def push(self,cnt):
        self.list1.append(cnt)
        return self.list1
target = [2134,34,5,4,56,2,3,12,2,5,34,5,23,1,434,52,4235]#目标数组
print("原数组:")
print(target)
print("小顶堆:")
Heap(target)
a = Stack()
print("栈:")
print(a.pop())
print(a.push('ljz'))

