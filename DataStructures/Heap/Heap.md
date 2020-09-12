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
    <tr>
        <table>
            <tr style="text-align: center; font-size:20px;">
                <td><strong><i>Python Implementation</i></strong></td>
                <td><strong><i>Java Implementation</i></strong></td>
            </tr>
            <tr>
                <td class="code" markdown="block" style="vertical-align: top;">
                    
{% highlight python %}
import math

class Heap:
    
    def __init__(self, ary):
        self.ary, self.heap_size = ary, len(ary)
        for i in range(self.heap_size//2 - 1, -1, -1):
            self.balance(i)
    
    def __str__(self):
        warning = "Warning: this is only designed to cast heaps with single digit elements to string.\n"
        i, j, u, s, b, ret = 2**int(math.log(self.heap_size, 2)) - 1, self.heap_size, 0, 0, 1, ""
        while i > 0:
            to_add = s*" " + u*"_" + ("_"*u + (b-u*2)*" " + "_"*u).join([str(e) for e in self.ary[i:j]]) + u*"_" + s*" " + "\n"
            slashes = (s + u)*" " + (b*" ").join(["/" if x % 2 else "\\" for x in range(i, j)]) + (s + u)*" " + "\n"
            u, j = s + u, i
            ret, s = slashes + to_add + ret, u + 1
            b, i = (s + u)*2 + 1, i//2
        return warning + s*" " + u*"_" + str(self.ary[i]) + u*"_" + s*" " + "\n" + ret

class MaxHeap(Heap):
    
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
    

class MinHeap(Heap):
    
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
{% endhighlight %}

<td class="code" markdown="block" style="vertical-align: top;">
    
{% highlight java %}
import java.util.ArrayList;
import java.lang.Math;
    
class Heap {
    public ArrayList<Integer> ary;
    public int heap_size;

    public String toString() {
        int i = (int) Math.pow(2, (int) (Math.log(this.heap_size)/Math.log(2))) - 1, j = this.heap_size, u = 0, s = 0, b = 1;
        String ret = "", warning = "Warning: this is only designed to cast heaps with single digit elements to string.\n";
        while (i > 0) {
            String s_space = new String(new char[s]).replace("\0", " "), u_underscore = new String(new char[u]).replace("\0", "_");
            String to_add = s_space + u_underscore, buffer = u_underscore + new String(new char[b-u*2]).replace("\0", " ") + u_underscore;
            for (int k = i; k < j-1; k++) {
                to_add += this.ary.get(k).toString() + buffer;
            }
            to_add += this.ary.get(j-1).toString() + u_underscore + s_space + "\n";
            String slashes = new String(new char[s+u]).replace("\0", " ");
            buffer = new String(new char[b]).replace("\0", " ");
            for (int k = i; k < j-1; k++) {
                slashes += (k % 2 == 1 ? "/" : "\\") + buffer;
            }
            slashes += ((j - 1) % 2 == 1 ? "/" : "\\") + new String(new char[s+u]).replace("\0", " ") + "\n";
            ret = slashes + to_add + ret;
            u = s + u;
            s = u + 1;
            b = (s + u)*2 + 1;
            j = i;
            i = i / 2;
        }
        String s_space = new String(new char[s]).replace("\0", " "), u_underscore = new String(new char[u]).replace("\0", "_");
        return warning + s_space + u_underscore + this.ary.get(0).toString() + u_underscore + s_space + "\n" + ret;
    }
}

class MaxHeap extends Heap {

    public MaxHeap(ArrayList<Integer> ary) {
        this.ary = ary;
        this.heap_size = this.ary.size();
        for (int i = this.heap_size/2 - 1; i >= 0; i--) {
            this.balance(i);
        }
    }

    public void balance(int i) {
        int left = i*2 + 1, right = i*2 + 2, largest = 0;
        if (left < this.heap_size && this.ary.get(left) > this.ary.get(i)) {
            largest = left;
        } else {
            largest = i;
        }
        if (right < this.heap_size && this.ary.get(right) > this.ary.get(largest)) {
            largest = right;
        }
        if (largest != i) {
            int temp = this.ary.get(i);
            this.ary.set(i, this.ary.get(largest));
            this.ary.set(largest, temp);
            this.balance(largest);
        }
    }

    public int maximum() {
        return this.ary.get(0);
    }

    public int extract_max() throws Exception {
        if (this.heap_size < 1) {
            throw new Exception("You are attempting to return the maximum of an empty heap.");
        }
        int maximum = this.ary.get(0);
        this.ary.set(0, this.ary.get(this.heap_size-1));
        this.heap_size--;
        this.balance(0);
        return maximum;
    }

    public void increase_key(int i, int key) throws Exception {
        if (key < this.ary.get(i)) {
            throw new Exception("You are attempting to increase the key at index " + i + " with a smaller key value.");
        }
        this.ary.set(i, key);
        int parent = (i - 1) / 2;
        while (i > 0 && this.ary.get(parent) < this.ary.get(i)) {
            int temp = this.ary.get(i);
            this.ary.set(i, this.ary.get(parent));
            this.ary.set(parent, temp);
            i = parent;
            parent = (parent - 1) / 2;
        }
    }

    public void insert(int key) throws Exception {
        this.ary.add(Integer.MIN_VALUE);
        this.heap_size++;
        this.increase_key(this.heap_size - 1, key);
    }
}

class MinHeap extends Heap {

    public MinHeap(ArrayList<Integer> ary) {
        this.ary = ary;
        this.heap_size = this.ary.size();
        for (int i = this.heap_size/2 - 1; i >= 0; i--) {
            this.balance(i);
        }
    }

    public void balance(int i) {
        int left = i*2 + 1, right = i*2 + 2, smallest = 0;
        if (left < this.heap_size && this.ary.get(left) < this.ary.get(i)) {
            smallest = left;
        } else {
            smallest = i;
        }
        if (right < this.heap_size && this.ary.get(right) < this.ary.get(smallest)) {
            smallest = right;
        }
        if (smallest != i) {
            int temp = this.ary.get(i);
            this.ary.set(i, this.ary.get(smallest));
            this.ary.set(smallest, temp);
            this.balance(smallest);
        }
    }

    public int minimum() {
        return this.ary.get(0);
    }

    public int extract_min() throws Exception {
        if (this.heap_size < 1) {
            throw new Exception("You are attempting to return the minimum of an empty heap.");
        }
        int minimum = this.ary.get(0);
        this.ary.set(0, this.ary.get(this.heap_size-1));
        this.heap_size--;
        this.balance(0);
        return minimum;
    }

    public void decrease_key(int i, int key) throws Exception {
        if (key > this.ary.get(i)) {
            throw new Exception("You are attempting to decrease the key at index " + i + " with a larger key value.");
        }
        this.ary.set(i, key);
        int parent = (i - 1) / 2;
        while (i > 0 && this.ary.get(parent) > this.ary.get(i)) {
            int temp = this.ary.get(i);
            this.ary.set(i, this.ary.get(parent));
            this.ary.set(parent, temp);
            i = parent;
            parent = (parent - 1) / 2;
        }
    }

    public void insert(int key) throws Exception {
        this.ary.add(Integer.MAX_VALUE);
        this.heap_size++;
        this.decrease_key(this.heap_size - 1, key);
    }
}
{% endhighlight %}