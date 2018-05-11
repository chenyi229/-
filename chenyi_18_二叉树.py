#coding:utf-8
class Node(object):
    """初始化参数"""
    def __init__(self,item):
        self.elem=item
        self.lchild=None
        self.rchild=None
class Tree(object):
    def __init__(self):
        self.root=None
    def add(self,item):
        node=Node(item)
        if self.root is None:
            self.root=node
            return
        queue=[self.root]
        while queue:
            current_node=queue.pop(0)
            if current_node.lchild is None:
                current_node.lchild=node
                return
            else:
                queue.append(current_node.lchild)
            if current_node.rchild is None:
                current_node.rchild=node
                return
            else:
                queue.append(current_node.rchild)
    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue=[self.root]
        while queue:
            current_node=queue.pop(0)
            print(current_node.elem)
            if current_node.lchild is not None:
                queue.append(current_node.lchild)
            if current_node.rchild is not None:
                queue.append(current_node.rchild)
    def preorder(self,root_node):
        """先序遍历"""
        if root_node is None:
            return
        print(root_node.elem)
        self.preorder(root_node.lchild)
        self.preorder(root_node.rchild)
    def midorder(self,root_node):
        """中序遍历"""
        if root_node is None:
            return
        self.midorder(root_node.lchild)
        print(root_node.elem)
        self.midorder(root_node.rchild)

    def backorder(self, root_node):
        """后序遍历"""
        if root_node is None:
            return
        self.backorder(root_node.lchild)
        self.backorder(root_node.rchild)
        print(root_node.elem)


if __name__=="__main__":
    tree=Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" ")
    tree.preorder(tree.root)
    print(" ")
    tree.midorder(tree.root,)
    print(" ")
    tree.backorder(tree.root)
    print(" ")
