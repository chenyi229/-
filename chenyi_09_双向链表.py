 #coding:utf8
class Node(object):
    def __init__(self,item):
        self.elem=item
        self.next=None
        self.prev=None
class DoubbleLinkList(object):
    def __init__(self,node=None):
        self.__head=None
    def is_empty(self):
        return self.__head is None
    def length(self):
        current=self.__head
        count=0
        while current!=None:
            count+=1
            current=current.next
        return count
    def travel(self):
        current=self.__head
        while current!=None:
            print(current.elem,end=" ")
            current=current.next
        print("")
    def add(self,item):
        node=Node(item)
        node.next=self.__head
       #self.__head.prev=node
        self.__head=node
        node.next.prev=node
    def append(self,item):
        node=Node(item)

        if self.is_empty():
            self.__head=node
            node.prev=None
        else:
            current = self.__head
            while current.next !=None:
                current=current.next
            current.next=node
            node.prev=current
    def insert(self,pos,item):
        node=Node(item)
        if pos<=0:
            self.add(item)
        elif pos>(len(self.length())-1):
            self.append(item)
        else:
            pre=self.__head
            count=0
            while count<=(pos-1):
                count+=1
                pre=pre.next
            node.next=pre.next
            pre.next.prev=node
            node.prev=pre
            pre.next = node
    def remove(self,item):
        current=self.__head
        while current!=None:
            if current.elem==self.__head:
                self.__head=current.next
                if current.next:
                    current.next.prev=None
                else:
                    current.prev.next=current.next
                    if current.next:
                        current.next.prev=current.prev
                break
            else:
                current=current.next


    def search(self,item):
        currenrt=self.__head
        while currenrt !=None:
            if currenrt.elem==item:
                return True
            else:
                currenrt=currenrt.next
        return False


if __name__=="__main__":
    li=DoubbleLinkList()
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