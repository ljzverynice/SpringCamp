target = [12312,34534,6,45,74,45,2,3,5,46,44,2,35,346,323,42,5,34,52,4,56,3,4,24,3,1,2,13,3,46,58,9,6,57,4,22]#目标数组

    #冒泡排序
def Bubble(target):
    newlist = []
    newlist.extend(target)
    for i in range(len(newlist)):
        for j in range(len(newlist)-i-1):
            if(newlist[j+1] >= newlist[j]):
                pass
            else:
                temp = newlist[j]
                newlist[j] = newlist[j+1]
                newlist[j+1] = temp
    print("冒泡排序：每趟最多比较j次，比较n-1躺，总开销n-1*(n-2)/2，时间复杂度为O(n^2)")
    print(newlist)

    #插入排序
def Insert(target):
    list1 = []
    list1.extend(target)
    list2 = []
    for i in range(len(list1)):
        if (len(list2) == 0):
            list2.append(list1[0])
        else:
            for j in range(len(list2)):
                if(j == len(list2)-1):
                    list2.append(list1[i])
                else:
                    if(list1[i] >= list2[j]):
                        pass
                    else:
                        list2.insert(j,list1[i])
                        break
    print("插入排序，每趟最多比较j次，共比较n-1躺，总开销n-1*(n-2)/2，时间复杂度为O(n^2)")
    print(list2) 

#归并排序
def Merge(target):
    def sort(templist):
        if(len(templist)<=1):
            return templist
        else:
            mid = len(templist)//2
            left = sort(templist[:mid])
            right = sort(templist[mid:])
            return merge(left,right)
    def merge(left,right):
        result = []
        i = 0
        j = 0
        while (i<len(left) and j<len(right)):
            if(left[i]<right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i <len(left):
            result.append(left[i])
            i += 1
        while j <len(right):
            result.append(right[j])
            j += 1
        if(len(result) == len(target)):
            print("归并排序：每层最多比较n次，共有log2n层，开销为nlog2n，时间复杂度为O(nlogn)")
            print(result)
        return result
    sort(target)

    #快速排序
def Quick(target):
    newlist = []
    newlist.extend(target)
    def part(left,right):
        if(left == right):
            pass
        else:
            (i,j) = sort(left,right)
            part(left,i)
            part(j,right)
    def sort(left,right):
        flag = right
        l = left
        leftlist = []
        rightlist = []
        midlist = []
        while l<=flag:
            if(newlist[l] < newlist[flag]):
                leftlist.append(newlist[l])
            elif(newlist[l] == newlist[flag]):
                midlist.append(newlist[l])
            elif(newlist[l] > newlist[flag]):
                rightlist.append(newlist[l])
            l += 1
        i = left + len(leftlist)-1
        j = left + len(leftlist) + len(midlist)-1
        leftlist.extend(midlist)
        leftlist.extend(rightlist)
        n = 0
        while left <= right:
            newlist[left] = leftlist[n]
            left += 1
            n += 1
        return i,j
    part(0,len(newlist)-1)
    print("快速排序:每层比较n次，最多比较log2n层，平均开销为nlog2n，时间复杂度为O(nlogn)")
    print(newlist)

    #堆排序
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
    list1 = []
    for i in range(len(newlist)):
        list1.append(newlist[0])
        newlist[0] = newlist[-1]
        del newlist[-1]
        downTree(0)
    print("堆排序:建立小顶堆开销为n,每次下沉开销为log2n,共下沉n次，总开销为n(log2n+1),时间复杂度为O(n)")
    print(list1)
print("原数组:")
print(target)       
Bubble(target)
Insert(target)
Merge(target)
Quick(target)
Heap(target)