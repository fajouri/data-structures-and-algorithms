"""M12 S07–S08: reference demonstrations, Python 3 (standard library only)."""
from random import Random
from time import perf_counter
from statistics import median

class ChainedMap:
    def __init__(self, capacity=8):
        if capacity < 1: raise ValueError('capacity must be positive')
        self.buckets = [[] for _ in range(capacity)]
        self.n = 0
    def put(self, key, value):
        bucket = self.buckets[hash(key) % len(self.buckets)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value); return
        bucket.append((key, value)); self.n += 1
        if self.n > len(self.buckets):
            old = self.buckets
            self.buckets = [[] for _ in range(2 * len(old))]
            self.n = 0
            for b in old:
                for k, v in b: self.put(k, v)
    def get(self, key):
        for k, v in self.buckets[hash(key) % len(self.buckets)]:
            if k == key: return v
        raise KeyError(key)
    def delete(self, key):
        bucket = self.buckets[hash(key) % len(self.buckets)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]; self.n -= 1; return
        raise KeyError(key)

_EMPTY, _DELETED = object(), object()
class LinearMap:
    def __init__(self, capacity=8):
        if capacity < 1: raise ValueError('capacity must be positive')
        self.slots = [_EMPTY] * max(4, capacity)
        self.n = self.used = 0  # used includes tombstones
    def locate(self, key):
        first_deleted = None
        m = len(self.slots)
        for j in range(m):
            i = (hash(key) + j) % m
            item = self.slots[i]
            if item is _EMPTY:
                return (i if first_deleted is None else first_deleted), False, j + 1
            if item is _DELETED:
                if first_deleted is None: first_deleted = i
            elif item[0] == key: return i, True, j + 1
        return first_deleted, False, m
    def _resize(self, m):
        old = self.slots
        self.slots = [_EMPTY] * m; self.n = self.used = 0
        for item in old:
            if item is not _EMPTY and item is not _DELETED: self.put(*item)
    def put(self, key, value):
        i, found, _ = self.locate(key)
        if found: self.slots[i] = (key, value); return
        if i is None or (self.used + 1) / len(self.slots) > 0.7:
            self._resize(2 * len(self.slots)); i, _, _ = self.locate(key)
        if self.slots[i] is _EMPTY: self.used += 1
        self.slots[i] = (key, value); self.n += 1
    def get(self, key):
        i, found, _ = self.locate(key)
        if not found: raise KeyError(key)
        return self.slots[i][1]
    def delete(self, key):
        i, found, _ = self.locate(key)
        if not found: raise KeyError(key)
        self.slots[i] = _DELETED; self.n -= 1
        if self.used > 2 * self.n and self.used > len(self.slots) // 3:
            self._resize(len(self.slots))  # clear tombstones


def sift_down(a, i, end):
    """Restore max-heap below i, assuming both child subtrees are heaps; end exclusive."""
    while 2*i + 1 < end:
        j = 2*i + 1
        if j + 1 < end and a[j+1] > a[j]: j += 1
        if a[i] >= a[j]: break
        a[i], a[j] = a[j], a[i]; i = j

def heapify(a):
    for i in range(len(a)//2 - 1, -1, -1): sift_down(a, i, len(a))

class MaxHeap:
    def __init__(self, values=()):
        self.a = list(values); heapify(self.a)
    def push(self, x):
        self.a.append(x); i = len(self.a)-1
        while i > 0:
            p = (i-1)//2
            if self.a[p] >= self.a[i]: break
            self.a[p], self.a[i] = self.a[i], self.a[p]; i = p
    def peek(self):
        if not self.a: raise IndexError('empty heap')
        return self.a[0]
    def pop(self):
        x = self.peek(); last = self.a.pop()
        if self.a: self.a[0] = last; sift_down(self.a, 0, len(self.a))
        return x

def heapsort(a):
    heapify(a)
    for end in range(len(a)-1, 0, -1):
        a[0], a[end] = a[end], a[0]; sift_down(a, 0, end)
    return a

def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]; j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]; j -= 1
        a[j+1] = key
    return a

def self_check():
    for cls in (ChainedMap, LinearMap):
        m = cls(8)
        for k in (1, 9, 17): m.put(k, str(k))
        m.delete(9); assert m.get(17) == '17'
        m.put(17, 'new'); assert m.n == 2 and m.get(17) == 'new'
        for k in range(100): m.put(k, k*k)
        for k in range(100): assert m.get(k) == k*k
        for k in range(0,100,2): m.delete(k)
        for k in range(100):
            if k%2: assert m.get(k) == k*k
            else:
                try: m.get(k)
                except KeyError: pass
                else: raise AssertionError('deleted key found')
        for op in (m.get, m.delete):
            try: op(-1)
            except KeyError: pass
            else: raise AssertionError('missing key accepted')
        rng=Random(42); ref={k:k*k for k in range(1,100,2)}
        for _ in range(500):
            k=rng.randrange(100); action=rng.randrange(3)
            if action==0: m.put(k,k+1); ref[k]=k+1
            elif action==1 and k in ref: m.delete(k); del ref[k]
            elif k in ref: assert m.get(k)==ref[k]
            else:
                try: m.get(k)
                except KeyError: pass
                else: raise AssertionError('missing key found')
            assert m.n==len(ref)
    rng=Random(42)
    for a in ([], [1], [2,2,1], list(range(10)), list(range(10,0,-1)), [rng.randrange(-20,20) for _ in range(100)]):
        assert heapsort(a.copy()) == insertion_sort(a.copy()) == sorted(a)
        h = MaxHeap(a)
        assert all(h.a[(i-1)//2]>=h.a[i] for i in range(1,len(h.a)))
        h.push(99)
        assert [h.pop() for _ in range(len(a)+1)] == sorted(a+[99], reverse=True)
        try: h.pop()
        except IndexError: pass
        else: raise AssertionError('empty pop accepted')
    print('Self-checks passed')

def benchmark():
    rng=Random(42)
    print('Median seconds (5 repeats; input copies outside timing)')
    for n in (32,128,512):
        base=[rng.randrange(10000) for _ in range(n)]
        for name,data in [('random',base),('sorted',sorted(base)),('reverse',sorted(base,reverse=True))]:
            times=[]
            for fn in (insertion_sort,heapsort):
                fn(data.copy())  # warm-up
                results=[]
                for _ in range(5):
                    work=data.copy(); start=perf_counter(); fn(work); results.append(perf_counter()-start)
                    assert work==sorted(data)
                times.append(median(results))
            print(n,name,*[f'{t:.7f}' for t in times])

if __name__=='__main__':
    self_check(); benchmark()
