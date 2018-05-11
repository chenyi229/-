#coding:utf-8
class Dque(object):
    """双端队列"""
    def __init__(self):
        self.__list=[]
    def is_empty(self):
        """判断列表是否为空"""
        return self.__list==[]
    def add_front(self,item):
        """在头部添加一个元素"""
        self.__list.insert(0,item)
    def add_rear(self,item):
        """在尾部添加一个元素"""
        self.__list.append(item)
    def pop_front(self):
        """在头部删除一个元素"""
        return self.__list.pop(0)
    def pop_rear(self):
        return self.__list.pop()
    def size(self):
        """队列的大小"""
        return len(self.__list)

if __name__=="__main__":
    deq=Dque()
    deq.add_front(1)
    deq.add_front(2)
    deq.add_rear(3)
    deq.add_rear(4)
    print(deq.size())
    print()