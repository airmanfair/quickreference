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
                <td>NA</td>
                <td>NA</td>
                <td>NA</td>
                <td>NA</td>
                <td>NA</td>
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
class Stack:
    
    def __init__(self, ary=[]):
        self.ary = ary
        
    def __str__(self):
        return str(self.ary)
    
    def empty(self):
        return len(self.ary) == 0
    
    def push(self, x):
        self.ary.append(x)
        
    def pop(self):
        return self.ary.pop()
{% endhighlight %}

<td class="code" markdown="block" style="vertical-align: top;">
    
{% highlight java %}
import java.util.LinkedList;

public class Stack {

    LinkedList<Integer> ary;

    public Stack(int[] ary) {
        this.ary = new LinkedList<>();
        for (int x: ary) {
            this.ary.add(x);
        }
    }

    public Stack() {
        this.ary = new LinkedList<>();
    }

    public String toString() {
        return this.ary.toString();
    }

    public boolean empty() {
        return this.ary.size() == 0;
    }

    public void push(int x) {
        this.ary.add(x);
    }

    public int pop() {
        return this.ary.removeLast();
    }
}
{% endhighlight %}