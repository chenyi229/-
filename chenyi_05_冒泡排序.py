# def bubbleSort(list):
#     length=len(list)
#     for i in range(1,length):#需要比较多少次
#     #for i in range(0,length-1):
#         # print("i=%d"%i)
#         for j in range(0,length-i):#表示的是元素的下标
#         #for j in range(0,length-1-i):
#             if list[j]>list[j+1]:
#                 temp=list[j]
#                 list[j]=list[j+1]
#                 list[j+1]=temp
#         for item in  list:
#             print(item)
#         print("=======================")
def bubbleSort(alist):

    for i in range(len(alist)-1,0,-1):#表示的排序的次数
        for j in range(i):#表示的元素的下标
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
    return alist

print("冒泡排序开始")
list=[10,30,76,5,18,3]
print(bubbleSort(list))