# def radixSort(list,d):
#     for k in range(1,d):
#         s=[[] for i in range(10)]
#         for i in list:
#             s[i/(10**k)%10].append(k)
#         list=[a for b in s for a in b]
#     return list
#
# if __name__=="__main__":
#     a=[10,234,12334]
#     a=radixSort(a,5)
#     print(a)


from random import randint
def main():
  A = [randint(1, 99999999) for _ in range(9999)]
  for k in range(8):
    S = [ [] for _ in range(10)]
    for j in A:
      S[j / (10 ** k) % 10].append(j)
    A = [a for b in S for a in b]
  for i in A:
    print(i)
main()