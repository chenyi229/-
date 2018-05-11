#coding:utf-8
def merge_sort(alist):
    n=len(alist)
    if n<=1:
        return alist
    mid=n//2
    #left 采用归并排序后形成的有序的新的列表
    left_li=merge_sort(alist[:mid])
    # right 采用归并排序后形成的有序的新的列表
    right_li=merge_sort(alist[mid:])
    #merge(letf,right)
    #将2个字序列合并成一个整体
    left_pointer,right_porinter=0,0
    result=[]
    while left_pointer<len(left_li) and right_porinter <len(right_li):
        if left_li[left_pointer] <right_li[right_porinter]:
            result.append(left_li[left_pointer])
            left_pointer+=1
        else:
            result.append(right_li[right_porinter])
            right_porinter+=1
    result+=left_li[left_pointer:]
    result+=right_li[right_porinter:]
    return result

if __name__=="__main__":
    alist=[54,26,21,12,32,43,23]
    sorted_li=merge_sort(alist)
    print(sorted_li)