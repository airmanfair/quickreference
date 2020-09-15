# Quick Sort
<table>
    <tr>
        <table>
            <tr>
                <td><strong><i>Class</i></strong></td>
                <td><strong><i>Type</i></strong></td>
                <td><strong><i>Category</i></strong></td>
                <td><strong><i><a href="/quickreference/DataStructures/DataStructures">Data Structure</a></i></strong></td>
                <td><strong><i>Space</i></strong></td>
                <td><strong><i>Time: Worst</i></strong></td>
                <td><strong><i>Time: Average</i></strong></td>
            </tr>
            <tr>
                <td><a href="/quickreference/OrderStatistic/OrderStatistic">Order Statistic</a></td>
                <td>Randomized</td>
                <td>Efficient</td>
                <td>Array</td>
                <td><i>O</i>(log n)</td>
                <td><i>O</i>(n)</td>
                <td><i>O</i>(n)</td>
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
                <td style="text-align: center;"><img src="QuickSelect.gif" alt="Quick Select GIF" style="width: auto; height: 315px;"/></td>
                <td style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/TlJhgPWM_Kc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
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
import random as r

def quick_select(ary, i): 
    
    def random_partition(start, end):
        k = r.randint(start, end)
        ary[end], ary[k] = ary[k], ary[end]
        x, k = ary[end], start - 1
        for j in range(start, end):
            if ary[j] <= x:
                k += 1
                ary[k], ary[j] = ary[j], ary[k]
        ary[k+1], ary[end] = ary[end], ary[k+1]
        return k + 1
    
    def recurse(start, end, i):
        if start == end:
            return ary[start]
        mid = random_partition(start, end)
        k = mid - start + 1
        if i == k:
            return ary[mid]
        elif i < k:
            return recurse(start, mid - 1, i)
        else:
            return recurse(mid + 1, end, i - k)
    
    return recurse(0, len(ary) - 1, i)
{% endhighlight %}

<td class="code" markdown="block" style="vertical-align: top;">
    
{% highlight java %}
static int quick_select(int[] ary, int i) {
    return recurse(ary, 0, ary.length - 1, i);
}

static int recurse(int[] ary, int start, int end, int i) {
    if (start == end) {
        return ary[start];
    }
    int mid = random_partition(ary, start, end);
    int k = mid - start + 1;
    if (i == k) {
        return ary[mid];
    } else if (i < k) {
        return recurse(ary, start, mid - 1, i);
    } else {
        return recurse(ary, mid + 1, end, i - k);
    }
}

static int random_partition(int[] ary, int start, int end) {
    int k = new Random().nextInt(end - start) + start, temp = ary[end];
    ary[end] = ary[k];
    ary[k] = temp;
    int x = ary[end], i = start - 1;
    for (int j = start; j < end; j++) {
        if (ary[j] <= x) {
            temp = ary[++i];
            ary[i] = ary[j];
            ary[j] = temp;
        }
    }
    temp = ary[i+1];
    ary[i+1] = ary[end];
    ary[end] = temp;
    return i + 1;
}
{% endhighlight %}