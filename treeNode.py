#二叉树广度优先遍历，
# 通过队列的先进先出，
#先把根节点放入队列，利用队列的先进先出，访问队列中取出的节点。
#并分别把左子节点和右子节点放入队列
#循环下去，知道队列为空

#1，先定义二叉树的节点
class TreeNode(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

#定义一个二叉树
class BinaryTree(object):
    def __init__(self,root=None):
        self.root = root
    def breachSearch(self):
        if self.root == None:
            return None
        retList = []
        queue = Queue()
        queue.put(self.root)    #先把根节点放入队列中
        #如果队列不为空，则遍历子节点，并把左子节点和右子节点分别放到队列中
        while queue.empty() is not True:
            node = queue.get()
            retList.append(node.var)
            if node.left != None:
                retList.append(node.left)
            if node.right != None:
                retList.append(node.right)
        return retList

#对二叉树做广度优先遍历
if  __name__ == "__main__":
    rootNode = TreeNode(50)  #构造根节点
    rootNode.left = TreeNode(20,TreeNode(15),TreeNode(30))
    rootNode.right = TreeNode(60,right=TreeNode(70))
    tree = BinaryTree(rootNode)
    retList = tree.breachSearch()
    print(retList)





