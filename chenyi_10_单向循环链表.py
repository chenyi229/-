class Node(object):
    def __init__(self,elem):
        self.elem=elem
class singleCycleLinkList(object):
    def __init__(self):
        self.__head=None
    def is_empty(self):
        """判断链表是否为空链表"""
        return self.__head is None
    def length(self):
        """计算单向循环链表的长度"""
        if self.is_empty():
            return 0
        else:
            current=self.__head
            count=1
            while current.next != self.__head:
                count+=1
                current=current.next
            return count
    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return 0
        else:
            current=self.__head
            while current.next !=self.__head:
                print(current,end="")
                current=current.next
            print(current,end="")
    def add(self,item):
        """给单向循环链表头添加元素"""
        node=Node(item)
        if self.is_empty():
            self.__head=node
            node.next=node
        else:
            current=self.__head
            while current.next !=self.__head:
                current=current.next
            node.next=self.__head
            self.__head = node
            current.next=node
    def append(self,item):
        """给单向循环链表尾添加元素"""
        node=Node(item)
        if self.is_empty():
            self.__head=node
            node.next=node
        else:
            current=self.__head
            while current.next !=self.__head:
                current=current.next
            current.next=node
            node.next=self.__head
    def insert(self,pos,item):
        """在某个位置添加元素"""
        node = Node(item)
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        pre=self.__head
        count=0
        while count <(pos-1):
            count+=1
            pre=pre.next
        node.next=pre.next
        pre.next = node

    def remove(self,item):
        if self.is_empty():
            return
        node=Node(item)
        current=self.__head
        pre=None
        while current.next !=self.__head:
            if current.elem==item:
                """判断是否是头节点"""
                if  current==self.__head:
                    rear=self.__head
                    while rear.next !=self.__head:
                        rear=rear.next
                    self.__head=current.next
                    rear.next=self.__head
                else:
                    """中间节点"""
                    pre.next=current.next
                return
            else:
                pre=current
                current=current.next
        #退出循环，cur指向尾节点
        if current.elem==item:
            if current==self.__head:
                #链表只有一个节点
                self.__head==None
            else:
                pre.next=current.next

    def search(self,item):
        if self.is_empty():
            return False
        current=self.__head
        while current.next !=self.__head:
            if current.elem==item:
                return  True
            else:
                current=current.next
        if  current.elem==item:
            return True
        return False


