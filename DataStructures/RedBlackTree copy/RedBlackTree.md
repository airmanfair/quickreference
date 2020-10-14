# Binary Search Tree
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
                <td>NA</td>
                <td>NA</td>
                <td><i>O</i>(log n)</td>
                <td><i>O</i>(log n)</td>
                <td><i>O</i>(log n)</td>
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
class BST:
    
    class Node:
        
        def __init__(self, val, left=None, right=None):
            self.val, self.left, self.right = val, left, right
            
        def search(self, val):
            if self == None or self.val == val: 
                return self
            elif val < self.val: 
                return self.left.search(val)
            return self.right.search(val)

    def __init__(self, ary=None):
        for val in ary:
            self.insert(val)

    def insert(self, val):
        x, y, z = self.root, None, self.Node(val)
        while x != None:
            y = x
            if z.val < x.val:
                x = x.left
            else: 
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z
            
    def delete(self, x):
        
        def transplant(u, v):
            if u.p == None:
                self.root = v
            elif u == u.p.left:
                u.p.left = v
            else:
                u.p.right = v
            if v == None:
                v.p = u.p
        
        if x.left == None:
            transplant(x, x.right)
        elif x.right == None:
            transplant(x, x.left)
        else:
            y = min(x.right)
            if y.p != x:
                transplant(y, y.right)
                y.right = x.right
                y.right.p = y
            transplant(x, y)
            y.left = x.left
            y.left.p = y
        
    def __min__(self):
        x = self.root
        while x.left != None:
            x = x.left
        return x
    
    def __max__(self):
        x = self.root
        while x.right != None:
            x = x.right
        return x
{% endhighlight %}
>
<td class="code" markdown="block" style="vertical-align: top;">
    
{% highlight java %}

{% endhighlight %}