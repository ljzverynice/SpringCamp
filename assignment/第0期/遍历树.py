#目标二叉树，None表示该节点为空
tree1 = [1,2,3,None,4,5,6,None,None,None,7,8,None,9,10]#递归二叉树
tree2 = ['a','b','c',None,'d','e','f',None,None,None,'g','h',None,'i','j']#循环二叉树
    #递归实现
class Recursion():
    def __init__(self,tree):
        self.tree = tree
    def pre(self,root = 0):
        lc = 2*root +1
        rc = 2*root +2
        if self.tree[root]:
            print(self.tree[root])
        else:pass
        if(lc<len(self.tree) and self.tree[lc]):
            self.pre(lc)
        if(rc<len(self.tree) and self.tree[rc]):
            self.pre(rc)
    def mid(self,root = 0):
        lc = 2*root +1
        rc = 2*root +2
        if(lc<len(self.tree) and self.tree[lc]):
            self.mid(lc)
        print(self.tree[root])
        if(rc<len(self.tree) and self.tree[rc]):
            self.mid(rc)
    def post(self,root = 0):
        lc = 2*root +1
        rc = 2*root +2
        if(lc<len(self.tree) and self.tree[lc]):
            self.post(lc)
        if(rc<len(self.tree) and self.tree[rc]):
            self.post(rc)
        print(self.tree[root])

    #循环实现
class Circulate():
    def __init__(self,tree):
        self.tree = tree
    def mid(self):
        mtree = []
        mtree.extend(self.tree)
        stack = []
        cur = 0
        while len(stack) or mtree[cur]:
            lc = cur*2+1
            rc = cur*2+2
            if lc<len(mtree) and mtree[lc]:
                stack.append(cur)
                cur = lc
            elif rc<len(mtree) and mtree[rc]:
                print(mtree[cur])
                mtree[cur] = None
                cur = rc
            else:
                print(mtree[cur])
                mtree[cur] = None
                if(stack):
                    cur = stack.pop()
    def pre(self):
        stack = []
        cur = 0
        ptree = []
        ptree.extend(self.tree)
        while len(stack) or ptree[cur]:
            lc = cur*2+1
            rc = cur*2+2
            if lc<len(ptree) and ptree[lc] and rc<len(ptree) and ptree[rc]:
                stack.append(rc)
                print(ptree[cur])
                ptree[cur] = None
                cur = lc
            elif rc<len(ptree) and ptree[rc]:
                print(ptree[cur])
                ptree[cur] = None
                cur = rc
            elif lc<len(ptree) and ptree[lc]:
                print(ptree[cur])
                ptree[cur] = None
                cur = lc
            else:
                print(ptree[cur])
                ptree[cur] = None
                if(stack):
                    cur = stack.pop()
    def post(self):
        stack = []
        cur = 0
        potree = []
        result = []
        potree.extend(self.tree)
        while len(stack) or potree[cur]:
            lc = cur*2+1
            rc = cur*2+2
            if lc<len(potree) and potree[lc] and rc<len(potree) and potree[rc]:
                stack.append(lc)
                result.append(potree[cur])
                potree[cur] = None
                cur = rc
            elif rc<len(potree) and potree[rc]:
                result.append(potree[cur])
                potree[cur] = None
                cur = rc
            elif lc<len(potree) and potree[lc]:
                result.append(potree[cur])
                potree[cur] = None
                cur = lc
            else:
                result.append(potree[cur])
                potree[cur] = None
                if(stack):
                    cur = stack.pop()
        result.reverse()
        for each in result:
            print(each)
    def level(self):
        queue = [self.tree[0]]
        while queue:
            cur = queue[0]
            for i in range(len(self.tree)):
                if(cur == self.tree[i]):
                    break
            del queue[0]
            print(cur)
            lc = 2*i+1
            rc = 2*i+2
            if rc<len(self.tree) and self.tree[rc]:
                queue.append(self.tree[rc])
            if lc<len(self.tree) and self.tree[lc]:
                queue.append(self.tree[lc])

R = Recursion(tree1)
R.pre()
R.mid()
R.post()

C = Circulate(tree2)
C.mid()
C.pre()
C.post()
C.level()