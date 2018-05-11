#coding:utf8
"""
@author:ChenYi

"""
class Node(object):
    """节点"""
    def __init__(self,elem):
        self.elem=elem
        self.next=None
    pass
class singleLinkList(object):
    """单链表"""
    def __init__(self,node=None):
        """初始化"""
        self.__head=node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head==None
    def length(self):
        current=self.__head
        count=0
        while current!=None:
            count+=1
            current=current.next
        return count
    def travel(self):
        current=self.__head
        while current !=None:
            print(current.elem,end=" ")
            current=current.next
        print("")
    def add(self,item):
        """头插法"""
        node=Node(item)
        node.next=self.__head
        self.__head=node

    def append(self,item):
        node=Node(item)
        if self.is_empty():
            self.__head=node
        else:
            current=self.__head
            while current.next!=None:
                current=current.next
            current.next=node
    def insert(self,pos,item):
        """制定位置添加元素"""
        if pos<=0:
            self.add(item)
        elif pos >(self.length()-1):
            self.append(item)
        else:
            pre=self.__head
            count=0
            while count<(pos-1):
                count += 1
                pre=pre.next
            #当循环退出之后，pre只想pos-1
            node=Node(item)
            node.next=pre.next

            pre.next=node


    def remove(self,item):
        """删除节点"""
        current=self.__head
        pre=None
        while  current!=None:
            if current.elem==item:
                #先判断此节点是否是头结点
                #如果是头结点：
                if current==self.__head:
                    self.__head=current.next
                else:
                    pre.next=current.next
                break
            else:
                pre=current
                current=current.next
    def search(self,item):
        current=self.__head
        while current!=None:
            if current.elem==item:
                return True
            else:
                current=current.next

        return False

if __name__=="__main__":
    li=singleLinkList()
    print(li.is_empty())
    print(li.length())
    li.append(1)
    li.add(8)
    li.append(1)
    li.append(1)
    li.append(1)
    li.append(1)
    print(li.is_empty())
    print(li.length())
    li.insert(-1,4)
    li.travel()
    li.remove(4)
    li.remove(1)
    li.travel()