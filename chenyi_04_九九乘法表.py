# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d\t"%(i,j,i*j),end=" ")
#     print()
# # raw=0
# com=0
# while com<9:
#     com+=1
#     while raw<9:
#         raw+=1
#         print("%d*%d=%d\t"%(com,raw,raw*com),end=" ")
#         if raw==com:
#             raw=0
#             print("")
#             break
#左上三角形
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("#",end="")
#     print()
#  #左下三角形
# for i in range(1,10):
#     for j in range(1,10-i):
#         print("#",end="")
#     print()
#
#右上三角形
# for i in range(10):
#     for j in range(1,10-i):
#         print(" ",end="")
#
#     for k in range(10-i,11):
#         print("#",end="")
#     print()

# #右下三角形
for i in range(10):
    for j in range(0,i):
        print(" ",end=" ")
    for j in range(i,10):
        print("#",end=" ")
    print()