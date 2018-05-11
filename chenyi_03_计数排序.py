# def countsort(lista):
#     leng=len(lista)
#     c=[]
#     res=[]
#     for i in range(0,10000):
#         c.append(0)
#     for i in range(0,leng):
#         c[lista[i]]=c[lista[i]]+1
#         res.append(0)
#     for i in range(0,10000):
#         c[i]=c[i-1]+c[i]       #c中此时存放的是小于或者等于i的数字的个数
#     for i in range(leng-1,-1,-1):#倒序遍历
#         res[c[lista[i]]-1]=lista[i]
#         c[lista[i]]=c[lista[i]]-1
#     return res
# lista=[5,4,2,5,1,7]       #计数排序测试代码
# lista=countsort(lista)
# print(lista)

#计数排序
def countSort(list):
    a=[0 for i in range(len(list))]
    b=[0 for i in range(max(list)+1)]
    #统计出现的次数，统计出现的频率
    for i in list:
        b[i]+=1
    #对所有的计数累加，每项和前面一项进行累加和
    for i in  range(1,len(b)):
        b[i]=b[i-1]+b[i]
    for i in list:#遍历一波，然后存入数组中
        a[b[i]-1]=i
        b[i]-=1
    return a
if __name__=="__main__":
    list=[7,2,3,8]
    print(countSort(list))