#coding：utf-8
def ShellSort(alist):
     """希尔排序"""
     n=len(alist)
     gap=n//2
     #gap变化到0之前，插入算法执行的次数
     while gap>=1:
         # 希尔算法，与普通的插入算法的区别就是gap步长
         for i in range(gap,n):
            while i>0:
                if alist[i]<alist[i-gap]:
                    alist[i],alist[i-gap]=alist[i-gap],alist[i]
                    i-=gap
                else:
                    break
         gap //=2
     return alist

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    li1=ShellSort(li)
    print(li1)
