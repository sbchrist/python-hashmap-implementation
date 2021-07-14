import HashInterface

class DoubleProbeHashMap(HashInterface.HashInterface):

    _AVAIL = object()

    def _is_available(self,j):
        return self._table[j] is None or self._table[j] is DoubleProbeHashMap._AVAIL

    def _find_slot(self,j,k):
        i=0
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None:
                    return (False,firstAvail)
            elif k == self._table[j]._key:
                return (True,j)
            self._collisions+=1
            i+=1
            j = (i*( self._prime-(self._hash_function(j)%self._prime))+j)%len(self._table)
    
    def _bucket_getitem(self,j,k):
        found,s = self._find_slot(j,k)

        if not found:
            raise KeyError('key Error: ' + repr(k))

        return self._table[s]._value
    
    def _bucket_setitem(self,j,k,v):
        found, s = self._find_slot(j,k)
        if not found:
            self._table[s] = self._Item(k,v)
            #print("setting, Key: ",k,"value: ",v,"Hash: ",j, "at: ",s)
            self._n+=1
        else:
            self._table[s]._value = v
    
    def _bucket_delitem(self,j,k):
        found,s = self._find_slot(j,k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        self._table[s] = DoubleProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key
