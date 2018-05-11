def insertSort(list):
    for i in range(1,len(list)):
        temp=list[i]
        j=i-1
        while j>=0:
            if list[j]>temp:
                list[j+1]=list[j]
                list[j]=temp
            j-=1
    print(list)
list=[10,2,30,15,20]
insertSort(list)