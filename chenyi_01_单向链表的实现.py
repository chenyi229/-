#1 Node的实现，每个NOde分为两部分，一部分分为含有链表的元素，另外一部分为指针
class Node():
    __slots__ = ["__item","__next"] #限制Node实例的属性
    def __init__(self,item):
        self.__item=item
        self.__next=None #Node的指针默认只想None

    def getItem(self): #获得链表中的元素
        return self.__item #返回链表中的元素
    def getNext(self): #获得指针
        return self.__next #返回链表中的下一个迭代对象
    def setItem(self,newitem):#设置新的内容
        self.__item=newitem #返回新的内容
    def setNext(self,newNext):#设置新的指针
        self.__next=newNext#返回新的指针
#2.单向链表的实现

class SinglelinkedList ():
    def __init__(self):
        self.__head=None #初始化链表为空表
        self.__size=0 #大小为0,__size 私有属性


#3.检查链表是否为空

    def isEmpty(self):
        return self.__head==None #头文件为空或者说没有
#4.在链表的前端添加元素
    def add(self,item):
        temp=Node(item) #temp是Node的对象
        temp.setNext(self.__head)#？？？？？
        temp.__item=temp#？？？
#5.append在链表的尾部添加元素

    def append(self,item):
        temp=Node(item)
        if self.isEmpty():
            self.__head=temp #若列表为空表，将添加的元素设为第一个元素
        else:
            current=self.__head
            while current.getNext()!=None:
                current=current.getNext() #遍历链表
            current.setNext(temp) #此时current为链表的最后的元素
#6.搜索元素是否在链表中
    def search(self,item):
        current=self.__head
        founditem=False
        while current!=None and not founditem:
            if current.getItem()==item:
                founditem=True
            else:
                current=current.getNext()
        return founditem
#7index 索引元素在链表中的位置

    def Index(self,item):
        current=self.__head
        count=0
        found=None
        while current!=None and not found:
            count +=1
            if current.getItem()==item:
                found=True
            else:
                current-current.getNext()
            if found:
                return count
            else:
                raise ValueError
                print("%s is not in linkedist"%item)
#8remove 删除链表中的某项元素
    def remove(self,item):
        current=self.__head
        pre=None
        while current!=None:
            if current.getItem()==item:
                if not pre:
                    self.__head=current.getNext()
                else:
                    pre.setNext(current.getNext())
                break

            else:
                pre=current
                current=current.getNext()

    def insert(self, pos, item):
        if pos <= 1:
            self.add(item)
        elif pos > self.size():
            self.append(item)
        else:
            temp = Node(item)
            count = 1
            pre = None
            current = self._head
            while count < pos:
                count += 1
                pre = current
                current = current.getNext()
            pre.setNext(temp)
            temp.setNext(current)

if __name__=='__main__':
    a=SinglelinkedList()
    for i in range(1,10):
        a.append(i)
    print(a.size())
    a.travel()
    print(a.search(6))
    print(a.index(5))
    a.remove(4)
    a.travel()
    a.insert(4,100)
    a.travel()
