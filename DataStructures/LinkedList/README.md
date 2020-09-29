# Linked List
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
                <td><i>O</i>NA</td>
                <td><i>O</i>NA</td>
                <td><i>O</i>(n)</td>
                <td><i>O</i>NA</td>
                <td><i>O</i>NA</td>
                <td><i>O</i>NA</td>
            </tr>
        </table>
    </tr>
</table>

# Python Implementation
``` python
class LinkedList:
    
    class Node:
        
        def __init__(self, val, next_node=None, prev_node=None):
            self.val, self.next, self.prev = val, next_node, prev_node
            
    class Iter:
        
        def __init__(self, nil):
            self.nil, self.current = nil, nil.next
    
        def __iter__(self):
            return self

        def __next__(self):
            if self.current is self.nil:
                raise StopIteration
            else:
                val = self.current.val
                self.current = self.current.next
                return val

    def __init__(self):
        self.nil, self.n = self.Node(None), 0
        self.nil.next = self.nil.prev = self.nil
    
    def __iter__(self):
        return self.Iter(self.nil)
        
    def __str__(self):
        return str(list(self))
    
    def search(self, key):
        node = self.nil.next
        while node is not self.nil and node.val != key: 
            node = node.next
        return node if node.val != None else None
    
    def insert(self, val):
        node = self.Node(val if type(val) == int else val.val, self.nil.next, self.nil)
        self.nil.next.prev = node
        self.nil.next = node
    
    def delete(self, node):
        if node:
            node.prev.next, node.next.prev = node.next, node.prev
```

# Java Implementation
``` java
import java.util.Iterator;

public class ListNode {
    
    Integer val;
    ListNode next;
    ListNode prev;

    public ListNode(Integer val, ListNode next_node, ListNode prev_node) {
        this(val, next_node);
        this.prev = prev_node;
    }

    public ListNode(Integer val, ListNode next_node) {
        this(val);
        this.next = next_node;
    }

    public ListNode(Integer val) {
        this.val = val;
    }
}


public class LinkedListIterator implements Iterator<Integer> {

    ListNode current;
    ListNode nil;

    public LinkedListIterator(ListNode nil) {
        this.current = nil.next;
        this.nil = nil;
    }

    public boolean hasNext() {
        return this.current != this.nil;
    }

    public Integer next() {
        Integer val = this.current.val;
        this.current = current.next;
        return val;
    }
}

public class LinkedList implements Iterable<Integer> {

    ListNode nil;
    Integer n;

    public LinkedList() {
        this.nil = new ListNode(null, null, null);
        this.nil.next = this.nil.prev = this.nil;
        this.n = 0;
    }

    public LinkedListIterator iterator() {
        return new LinkedListIterator(this.nil);
    }

    public ListNode search(Integer key) {
        ListNode node = this.nil.next;
        while (node != this.nil && !node.val.equals(key)) {
            node = node.next;
        }
        return node != this.nil ? node : null;
    }

    public void insert(Integer val) {
        insert(new ListNode(val));
    }

    public void insert(ListNode node) {
        node.next = this.nil.next;
        this.nil.next.prev = node;
        this.nil.next = node;
        node.prev = this.nil;
    }

    public void delete(ListNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
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