#coding：utf-8
#二分查找收缩就必须是一个有序的列表
#递归就是函数调用本身
# def binary_search(alist,item):
#     """二分查找递归版本"""
#     n=len(alist)
#     if n>0:
#         mid=n//2
#         if alist[mid]==item:
#             return True
#         elif item <alist[mid]:
#             return binary_search(alist[:mid],item)
#         else:
#             return binary_search(alist[mid+1:],item)
#     else:
#         return False

def binary_search(alist, item):
    """二分查找,递归"""
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid + 1:], item)
    return False
# def binary_search(alist,item):
#     """二分查找，非递归版本（根据起始位置和终止位置）"""
#     n=len(alist)
#     first=0
#     last=n-1
#     while first<=last:
#         mid=(first+last)//2
#         if alist[mid]==item:
#             return True
#         elif item<alist[mid]:
#             last=mid-1
#         else:
#             first=mid+1
#     return False
if __name__ == "__main__":
    li=[3,2,1,5,6,7]
    print(binary_search(li,2))
