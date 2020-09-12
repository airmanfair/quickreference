# Heap
<table>
    <tr>
        <table>
            <tr>
                <td><strong><i>Insert</i></strong></td>
                <td><strong><i>Delete</i></strong></td>
                <td><strong><i>Balance</i></strong></td>
                <td><strong><i>Get at Index</i></strong></td>
                <td><strong><i>Search</i></strong></td>
                <td><strong><i>Minimum</i></strong></td>
                <td><strong><i>Maximum</i></strong></td>
                <td><strong><i>Space</i></strong></td>
            </tr>
            <tr>
                <td><i>O</i>(log n)</td>
                <td><i>O</i>(log n)</td>
                <td><i>O</i>(log n)</td>
                <td>NA</td>
                <td><i>O</i>(n)</td>
                <td><i>O</i>(1) for MinHeap, <i>O</i>(n) for MaxHeap</td>
                <td><i>O</i>(1) for MaxHeap, <i>O</i>(n) for MinHeap</td>
                <td><i>O</i>(n)</td>
            </tr>
        </table>
    </tr>
</table>

# Python Implementation
``` python
import math

class MaxHeap:
    
    def __init__(self, ary):
        self.ary, self.heap_size = ary, len(ary)
        for i in range(self.heap_size//2 - 1, -1, -1):
            self.balance(i)
    
    def balance(self, i):
        left, right  = i*2 + 1, i*2 + 2
        if left < self.heap_size and self.ary[left] > self.ary[i]:
            largest = left
        else:
            largest = i
        if right < self.heap_size and self.ary[right] > self.ary[largest]:
            largest = right
        if largest != i:
            self.ary[i], self.ary[largest] = self.ary[largest], self.ary[i]
            self.balance(largest)
            
    def maximum(self):
        return self.ary[0]
    
    def extract_max(self):
        if self.heap_size < 1:
            raise Exception("You are attempting to return the maximum of an empty heap.")
        maximum, self.ary[0] = self.ary[0], self.ary[self.heap_size-1]
        self.heap_size -= 1
        self.balance(0)
        return maximum
    
    def increase_key(self, i, key):
        if key < self.ary[i]:
            raise Exception("You are attempting to increase the key at index " + str(i) + " with a smaller key value.")
        self.ary[i], parent = key, (i - 1) // 2
        while i > 0 and self.ary[parent] < self.ary[i]:
            self.ary[i], self.ary[parent], i, parent = self.ary[parent], self.ary[i], parent, (parent - 1) // 2
    
    def insert(self, key):
        self.ary.append(float("-inf"))
        self.heap_size += 1
        self.increase_key(self.heap_size - 1, key)
    
    def __str__(self):
        # Works when heap elements can be represented by a single character. Breaks for any heap element of len(str(elem)) > 1.
        i, j, u, s, b, ret = 2**int(math.log(self.heap_size, 2)) - 1, self.heap_size, 0, 0, 1, ""
        while i > 0:
            to_add = s*" " + u*"_" + ("_"*u + (b-u*2)*" " + "_"*u).join([str(e) for e in self.ary[i:j]]) + u*"_" + s*" " + "\n"
            slashes = (s + u)*" " + (b*" ").join(["/" if x % 2 else "\\" for x in range(i, j)]) + (s + u)*" " + "\n"
            u, j = s + u, i
            ret, s = slashes + to_add + ret, u + 1
            b, i = (s + u)*2 + 1, i//2
        return s*" " + u*"_" + (b*" ").join([str(elem) for elem in self.ary[i:j]]) + u*"_" + s*" " + "\n" + ret

class MinHeap:
    
    def __init__(self, ary):
        self.ary, self.heap_size = ary, len(ary)
        for i in range(self.heap_size//2 - 1, -1, -1):
            self.balance(i)
    
    def balance(self, i):
        left, right  = i*2 + 1, i*2 + 2
        if left < self.heap_size and self.ary[left] < self.ary[i]:
            smallest = left
        else:
            smallest = i
        if right < self.heap_size and self.ary[right] < self.ary[smallest]:
            smallest = right
        if smallest != i:
            self.ary[i], self.ary[smallest] = self.ary[smallest], self.ary[i]
            self.balance(smallest)
            
    def minimum(self):
        return self.ary[0]
    
    def extract_min(self):
        if self.heap_size < 1:
            raise Exception("You are attempting to return the minimum of an empty heap.")
        minimum, self.ary[0] = self.ary[0], self.ary[self.heap_size-1]
        self.heap_size -= 1
        self.balance(0)
        return minimum
    
    def decrease_key(self, i, key):
        if key > self.ary[i]:
            raise Exception("You are attempting to decrease the key at index " + str(i) + " with a larger key value.")
        self.ary[i], parent = key, (i - 1) // 2
        while i > 0 and self.ary[parent] > self.ary[i]:
            self.ary[i], self.ary[parent], i, parent = self.ary[parent], self.ary[i], parent, (parent - 1) // 2
    
    def insert(self, key):
        self.ary.append(float("inf"))
        self.heap_size += 1
        self.decrease_key(self.heap_size - 1, key)
    
    def __str__(self):
        # Works when heap elements can be represented by a single character. Breaks for any heap element of len(str(elem)) > 1.
        i, j, u, s, b, ret = 2**int(math.log(self.heap_size, 2)) - 1, self.heap_size, 0, 0, 1, ""
        while i > 0:
            to_add = s*" " + u*"_" + ("_"*u + (b-u*2)*" " + "_"*u).join([str(e) for e in self.ary[i:j]]) + u*"_" + s*" " + "\n"
            slashes = (s + u)*" " + (b*" ").join(["/" if x % 2 else "\\" for x in range(i, j)]) + (s + u)*" " + "\n"
            u, j = s + u, i
            ret, s = slashes + to_add + ret, u + 1
            b, i = (s + u)*2 + 1, i//2
        return s*" " + u*"_" + (b*" ").join([str(elem) for elem in self.ary[i:j]]) + u*"_" + s*" " + "\n" + ret
```

# Java Implementation
``` java
import java.util.ArrayList;
import java.lang.Math.log;
```