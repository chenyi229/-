n=int(input())
m=list(map(int,input().rstrip().split()))
result=[1 for i in range(len(m))]
for i in range(len(m)):
    for j in range(i):
        if m[j]<m[i]:
            result[i]=max(1,result[j]+1)
print(min(result))