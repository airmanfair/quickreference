# Counting Sort
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
                <td>Linear Sort</td>
                <td>Efficient</td>
                <td>Array</td>
                <td><i>O</i>(n + k)</td>
                <td><i>O</i>(n + k)</td>
                <td><i>O</i>(n + k)</td>
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
                <td style="text-align: center;"><img src="CountingSort.gif" alt="Counting Sort GIF" style="width: auto; height: 315px;"/></td>
                <td style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/7zuGmKfUt7s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
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
def counting_sort(ary, k):
    n = len(ary)
    output, dist = [0]*n, [0]*(k + 1)
    for i in range(n):
        dist[ary[i]] += 1
    for i in range(1, k + 1):
        dist[i] += dist[i-1]
    for i in range(n-1, -1, -1):
        output[dist[ary[i]]-1] = ary[i]
        dist[ary[i]] -= 1
    return output
{% endhighlight %}

<td class="code" markdown="block" style="vertical-align: top;">
    
{% highlight java %}
static int[] counting_sort(int[] ary, int k) {
    int[] output = new int[ary.length], dist = new int[k+1];
    for (int x : ary) {
        dist[x]++;
    }
    for (int i = 1; i <= k; i++) {
        dist[i] += dist[i-1];
    }
    for (int i = ary.length - 1; i >= 0; i--) {
        output[dist[ary[i]]-1] = ary[i];
        dist[ary[i]]--;
    }
    return output;
}
{% endhighlight %}