# Bubble Sort
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
                <td>Naive</td>
                <td><i>O</i>(1)</td>
                <td><i>O</i>(n<sup>2</sup>)</td>
                <td><i>O</i>(n<sup>2</sup>)</td>
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
                <td><img src="BubbleSort.gif" alt="Bubble Sort GIF" width="525" height="315"/></td>
                <td><iframe width="560" height="315" src="https://www.youtube.com/embed/xli_FI7CuzA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
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
def bubble_sort(ary):
    n = len(ary)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if ary[j] > ary[j+1]:
                ary[j], ary[j+1] = ary[j+1], ary[j]
{% endhighlight %}
                    
<td class="code" markdown="block" style="vertical-align: top;">
    
{% highlight java %}
static void bubble_sort(int[] ary) {
    for (var i = ary.length-1; i > 0; i--) {
        for (var j = 0; j < i; j++) {
            if (ary[j] > ary[j+1]) {
                int temp = ary[j];
                ary[j] = ary[j+1];
                ary[j+1] = temp;
            }
        }
    }
}
{% endhighlight %}