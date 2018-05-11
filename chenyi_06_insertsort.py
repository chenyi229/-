def insertsort(alist):
    for i in range(0,len(alist)):
        for j in range(i,0,-1):
            if alist[j]<alist[j-1]:
                alist[j],alist[j-1]=alist[j-1],alist[j]
    return alist

if __name__=="__main__":
    alist=[2,1,3,2]
    print(insertsort(alist))