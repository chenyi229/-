#非冒泡排序-选择排序
def bubbleSort(list):
    for i in range(0,len(list) ):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
    return list

list=[10,30,76,5,18]
print(bubbleSort(list))