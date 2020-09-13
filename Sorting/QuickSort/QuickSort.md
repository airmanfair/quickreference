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
                <td><a href="/quickreference/Sorting/Sorting">Sorting</a></td>
                <td>Divide & Conquer</td>
                <td>Efficient</td>
                <td>Array</td>
                <td><i>O</i>(log n)</td>
                <td><i>O</i>(n<sup>2</sup>)</td>
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
                <td><img src="QuickSort.gif" alt="Quick Sort GIF" style="width: auto; height: 315px;"/></td>
                <td><iframe width="560" height="315" src="https://www.youtube.com/embed/Hoixgm4-P4M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
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

def quick_sort(ary, start, end, random=False):
    
    def deterministic_partition(start, end):
        x, i = ary[end], start - 1
        for j in range(start, end):
            if ary[j] <= x:
                i += 1
                ary[i], ary[j] = ary[j], ary[i]
        ary[i+1], ary[end] = ary[end], ary[i+1]
        return i + 1
    
    def random_partition(start, end):
        i = r.randint(start, end)
        ary[end], ary[i] = ary[i], ary[end]
        return deterministic_partition(start, end)
    
    def helper(start, end):
        if start < end:
            mid = partition(start, end)
            helper(start, mid - 1)
            helper(mid + 1, end)
    
    partition = random_partition if random else deterministic_partition
    helper(start, end)
{% endhighlight %}

<td class="code" markdown="block" style="vertical-align: top;">
    
{% highlight java %}
import java.util.Random;

static int deterministic_partition(int[] ary, int start, int end) {
    int x = ary[end], i = start - 1;
    for (int j = start; j < end; j++) {
        if (ary[j] <= x) {
            int temp = ary[++i];
            ary[i] = ary[j];
            ary[j] = temp;
        }
    }
    int temp = ary[i+1];
    ary[i+1] = ary[end];
    ary[end] = temp;
    return i + 1;
}

static int random_partition(int[] ary, int start, int end) {
    int i = new Random().nextInt(end - start) + start, temp = ary[end];
    ary[end] = ary[i];
    ary[i] = temp;
    return deterministic_partition(ary, start, end);
}

static void quick_sort(int[] ary, int start, int end, boolean random) {
    if (start < end) {
        int mid = random ? random_partition(ary, start, end) : deterministic_partition(ary, start, end);
        quick_sort(ary, start, mid - 1, random);
        quick_sort(ary, mid + 1, end, random);
    }
}
{% endhighlight %}