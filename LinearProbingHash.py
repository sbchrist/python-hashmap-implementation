import copy
import HashInterface

class LinearProbeHashMap(HashInterface.HashInterface):

    _AVAIL = object()

    def _is_available(self,j):
        return self._table[j] is None #or self._table[j] is LinearProbeHashMap._AVAIL

    def _find_slot(self,j,k):
        i = copy.deepcopy(j)
        while True:
            if self._is_available(i):
                return (False,i)
            elif k == self._table[i]._key:
                return (True,i)
            self._collisions+=1
            i +=1
            i=i%len(self._table)
    
    def _bucket_getitem(self,j,k):
        found,s = self._find_slot(j,k)

        if not found:
            raise KeyError('key Error: ' + repr(k))

        return self._table[s]._value
    
    def _bucket_setitem(self,j,k,v):
        found, s = self._find_slot(j,k)
        #print('found for slot: ',s)
        if not found:
            self._table[s] = self._Item(k,v)
            self._n+=1
            
        else:
            self._table[s]._value = v
    
    def _bucket_delitem(self,j,k):
        found,s = self._find_slot(j,k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        self._table[s] = LinearProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key
