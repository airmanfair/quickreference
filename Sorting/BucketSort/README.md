# Bucket Sort
<table>
    <tr>
        <table>
            <tr>
                <td><strong><i>Class</i></strong></td>
                <td><strong><i>Type</i></strong></td>
                <td><strong><i>Category</i></strong></td>
                <td><strong><i><a href="/DataStructures/">Data Structure</a></i></strong></td>
                <td><strong><i>Space</i></strong></td>
                <td><strong><i>Time: Worst</i></strong></td>
                <td><strong><i>Time: Average</i></strong></td>
            </tr>
            <tr>
                <td><a href="/Sorting/">Sorting</a></td>
                <td>Linear Sort</td>
                <td>Efficient</td>
                <td><a href="/DataStructures/LinkedList/">Linked List</a></td>
                <td><i>O</i>(n + p)</td>
                <td><i>O</i>(n<sup>2</sup> + p)</td>
                <td><i>O</i>(n + p)</td>
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
                <td style="text-align: center;"><img src="BucketSort.gif" alt="Bucket Sort GIF" style="width: auto; height: 315px;"/></td>
                <td style="text-align: center;"><a href="https://youtu.be/VuXbEb5ywrU"><img src="http://img.youtube.com/vi/VuXbEb5ywrU/0.jpg" alt="Bucket Sort Video" width="560" height="315"/></a></td>
            </tr>
        </table>
    </tr>
</table>

# Python Implementation
``` python
class SortedLinkedList:
    
    class Node:
        
        def __init__(self, val, next_node=None):
            self.val, self.next = val, next_node
            
    class Iter:
        
        def __init__(self, head):
            self.current = head
    
        def __iter__(self):
            return self

        def __next__(self):
            if not self.current:
                raise StopIteration
            else:
                val = self.current.val
                self.current = self.current.next
                return val

    def __init__(self):
        self.head = None
    
    def __iter__(self):
        return self.Iter(self.head)
        
    def insert(self, val):
        if not self.head:
            self.head = self.Node(val)
        elif self.head.val > val:
            self.head = self.Node(val, self.head)
        else:
            current, prev = self.head.next, self.head
            while current:
                if current.val > val:
                    prev.next = self.Node(val, current)
                    return
                prev, current = current, current.next
            prev.next = self.Node(val)
        
def bucket_sort(ary):
    n, shift, denom = len(ary), min(ary), max(ary) + 1
    mapping, denom = [SortedLinkedList() for _ in range(n)], denom - shift
    for x in ary:
        idx = int(n*((x - shift) / denom))
        mapping[idx].insert(x)
    ary[:] = [item for sublist in mapping for item in sublist]
```

# Java Implementation
``` java
import java.util.Iterator;

public class ListNode {
    Integer val;
    ListNode next;

    public ListNode(Integer val, ListNode next_node) {
        this.val = val;
        this.next = next_node;
    }

    public ListNode(Integer val) {
        this.val = val;
        this.next = null;
    }
}

public class SortedLinkedList implements Iterable<Integer>{
    ListNode head;

    public SortedLinkedList() {
        this.head = null;
    }

    public ListIterator iterator() {
        return new ListIterator(this.head);
    }

    public void insert(Integer val) {
        if (this.head == null) {
            this.head = new ListNode(val);
        } else if (this.head.val > val) {
            this.head = new ListNode(val, this.head);
        } else {
            ListNode current = this.head.next, prev = this.head;
            while (current != null) {
                if (current.val > val) {
                    prev.next = new ListNode(val, current);
                    return;
                }
                prev = current;
                current = current.next;
            }
            prev.next = new ListNode(val);
        }
    }
}

public class ListIterator implements Iterator<Integer> {
    ListNode current;

    public ListIterator(ListNode head) {
        current = head;
    }

    public boolean hasNext() {
        return current != null;
    }

    public Integer next() {
        Integer val = this.current.val;
        this.current = current.next;
        return val;
    }
}

static void bucket_sort(int[] ary) {
    int shift = Integer.MAX_VALUE, denom = Integer.MIN_VALUE;
    for (int x: ary) {
        if (x < shift) {
            shift = x;
        }
        if (x > denom) {
            denom = x;
        }
    }
    denom = denom - shift + 1;
    SortedLinkedList[] mapping = new SortedLinkedList[ary.length];
    for (int i = 0; i < ary.length; i++) {
        mapping[i] = new SortedLinkedList();
    }
    for (int x: ary) {
        int idx = ary.length*((x - shift) / denom);
        mapping[idx].insert(x);
    }
    int i = 0;
    for (SortedLinkedList lst: mapping) {
        for (Integer x: lst) {
            ary[i++] = x;
        }
    }
}
```