# Stack
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
                <td><i>O</i>(1)</td>
                <td><i>O</i>(1)</td>
                <td>NA</td>
                <td>NA</td>
                <td>NA</td>
                <td>NA</td>
                <td>NA</td>
                <td><i>O</i>(n)</td>
            </tr>
        </table>
    </tr>
</table>

# Python Implementation
``` python
class Stack:
    
    def __init__(self, ary=[]):
        self.ary = []
        for item in ary: self.push(item)
        
    def __str__(self):
        return str(self.ary)
    
    def __len__(self):
        return len(self.ary)
    
    def push(self, x):
        self.ary.append(x)
        
    def pop(self):
        return self.ary.pop()
```

# Java Implementation
``` java
import java.util.Iterator;

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

    
public class Stack implements Iterable<Integer> {

    ListNode head;
    Integer n;

    public Stack() {
        this.head = null;
        this.n = 0;
    }

    public ListIterator iterator() {
        return new ListIterator(this.head);
    }

    public void push(Integer val) {
        this.head = new ListNode(val, this.head);
        this.n++;
    }

    public Integer pop() {
        Integer ret = this.head.val;
        this.head = this.head.next;
        this.n--;
        return ret;
    }

    public Integer length() {
        return this.n;
    }

    public String toString() {
        StringBuilder s = new StringBuilder("[");
        for (Integer x: this) {
            s.append(x.toString()).append(", ");
        }
        return s.substring(0, s.length() - 2) + "]";
    }
}
```