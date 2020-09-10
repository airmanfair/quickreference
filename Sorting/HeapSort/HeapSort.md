# Heap Sort
<table>
    <tr>
        <table>
            <tr>
                <td><strong><i>Class</i></strong></td>
                <td><strong><i>Type</i></strong></td>
                <td><strong><i>Category</i></strong></td>
                <td><strong><i>Space</i></strong></td>
                <td><strong><i>Time: Worst</i></strong></td>
                <td><strong><i>Time: Average</i></strong></td>
            </tr>
            <tr>
                <td><a href="/quickreference/Sorting/Sorting">Sorting</a></td>
                <td>In-place</td>
                <td>Efficient</td>
                <td><i>O</i>(1)</td>
                <td><i>O</i>(n log n)</td>
                <td><i>O</i>(n log n)</td>
            </tr>
        </table>
    </tr>
    <tr>
        <table>
            <tr style="text-align: center; font-size:20px;">
                <td><strong><i>GIF</i></strong></td>
                <td><strong><i>Video</i></strong></td>
            </tr>
            <tr>
                <td><img src="HeapSort.gif" alt="Heap Sort GIF" width="342" height="315"/></td>
                <td><iframe width="560" height="315" src="https://www.youtube.com/embed/2DmK_H7IdTo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
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
class MaxHeap:
    
    def __init__(self, ary):
        self.ary = ary
        self.heap_size = len(ary)
        for i in range(self.heap_size//2 - 1, -1, -1):
            self.heapify(i)
      
    def heapify(self, i):
        left, right  = i*2 + 1, i*2 + 2
        if left < self.heap_size and self.ary[left] > self.ary[i]:
            largest = left
        else:
            largest = i
        if right < self.heap_size and self.ary[right] > self.ary[largest]:
            largest = right
        if largest != i:
            self.ary[i], self.ary[largest] = self.ary[largest], self.ary[i]
            self.heapify(largest)
        
def heap_sort(ary):
    h = MaxHeap(ary)
    for i in range(h.heap_size - 1, 0, -1):
        h.ary[0], h.ary[i] = h.ary[i], h.ary[0]
        h.heap_size -= 1
        h.heapify(0)
{% endhighlight %}

<td class="code" markdown="block" style="vertical-align: top;">
    
{% highlight java %}
class MaxHeap {
    
    public int[] ary;
    public int heap_size;

    public MaxHeap(int[] ary) {
        this.ary = ary;
        this.heap_size = this.ary.length;
        for (int i = this.heap_size/2 - 1; i >= 0; i--) {
            this.heapify(i);
        }
    }

    public void heapify(int i) {
        int left = i*2 + 1, right = i*2 + 2, largest = 0;
        if (left < this.heap_size && this.ary[left] > this.ary[i]) {
            largest = left;
        } else {
            largest = i;
        }
        if (right < this.heap_size && this.ary[right] > this.ary[largest]) {
            largest = right;
        }
        if (largest != i) {
            int temp = this.ary[i];
            this.ary[i] = this.ary[largest];
            this.ary[largest] = temp;
            this.heapify(largest);
        }
    }
}
    
static void heap_sort(int[] ary) {
    MaxHeap h = new MaxHeap(ary);
    for (int i = h.heap_size - 1; i > 0; i--) {
        int temp = h.ary[0];
        h.ary[0] = h.ary[i];
        h.ary[i] = temp;
        h.heap_size -= 1;
        h.heapify(0);
    }
}
{% endhighlight %}