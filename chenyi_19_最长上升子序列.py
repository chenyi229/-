n = int(input())
li = list(map(int, input().rstrip().split()))
li_a = [1 for i in range(len(li))]
for i in range(1,len(li)):
    for j in range(i):
        if li[j]<li[i]:
            li_a[i]=max(li_a[i],li_a[j]+1)
print(li_a)
