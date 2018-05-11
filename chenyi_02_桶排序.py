import random

class BucketSort(object):
    def _max(self,oldlist):
        _max=oldlist[0]
        for i in oldlist:
            if i>_max:
                _max=i
        #print(_max)
        return _max
    def _min(self,oldlist):
        _min=oldlist[0]
        for i in oldlist:
            if i<_min:
                _min=i
        #print(_min)
        return _min
    def sort(self,oldlist):
        _max=self._max(oldlist)
        _min=self._min(oldlist)
        s=[0 for i in range(_min,_max+1)]
        for i in oldlist:
            s[i-_min]+=1
        current=_min
        n=0
        for i in s:
            while i>0:
                oldlist[n]=current
                i-=1
                n+=1
            current+=1

    def __call__(self, oldlist):
        self.sort(oldlist)
        return oldlist
if __name__=="__main__":
    a=[10,9,8,7,8,5,7,6,5]
    BucketSort()(a)


    print(a)