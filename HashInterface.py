import MapBase
from random import randrange

class HashInterface(MapBase.MapBase):
    def __init__(self,cap =191, p = 109345121):
        self._table = cap * [None]
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)
        self._collisions = 0

    def _hash_function(self,k):
        #return (hash(k)*self._scale + self._shift)%self._prime%len(self._table)
        return((k>>8)|((k&0xff)<<16)) % len(self._table)
        #return k%len(self._table)0xFFFFFFFF

    def __len__(self):
        return self._n

    def __getitem__(self,k):
        j = self._hash_function(k)
        return self._bucket_getitem(j,k)

    def __setitem__(self,k,v):
        j = self._hash_function(k)
        self._bucket_setitem(j,k,v)

    def __delitem__(self,k):
        j = self._hash_function(k)
        self._bucket_delitem(j,k)
        self._n -=1

