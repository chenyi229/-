def selectSort(list):
    for i in range(0,len(list)):
        for j in  range(i+1,len(list)):
            if list[i]>list[j]:

                list[i], list[j] = list[j], list[i]


    print(list)

list=[0,12,2,1,5,1]
selectSort(list)