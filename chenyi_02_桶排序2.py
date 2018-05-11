def bucket(list):
    s=[0 for i in range(min(list),max(list)+1)]
    for i in range(len(list)):
        s[list[i]-min(list)]+=1
    res=[]
    for i in range(len(s)):
        if s[i]!=0:
            res+=[i+min(list)]*s[i]#假如有2个的话，就申请2个空位
    return res
# def bucket(lst):
#     buckets = [0] * ((max(lst) - min(lst))+1)
#     for i in range(len(lst)):
#         buckets[lst[i]-min(lst)] += 1
#     res=[]
#     for i in range(len(buckets)):
#         if buckets[i] != 0:
#             res += [i+min(lst)]*buckets[i]
#     return res
list=[10,9,8,7,8,9]
bucket(list)
print(bucket(list))