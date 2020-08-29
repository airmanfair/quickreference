# Insertion Sort
<table>
    <tr>
        <table>
            <tr>
                <td><strong><i>Class</i></strong></td>
                <td><strong><i>Type</i></strong></td>
                <td><strong><i>Category</i></strong></td>
                <td><strong><i>Time</i></strong></td>
                <td><strong><i>Space</i></strong></td>
            </tr>
            <tr>
                <td><a href="/quickreference/Sorting/Sorting">Sorting</a></td>
                <td>In-place</td>
                <td>Naive</td>
                <td><i>O</i>(n<sup>2</sup>)</td>
                <td><i>O</i>(1)</td>
            </tr>
        </table>
    </tr>
    <tr>
        <table>
            <tr style="text-align: center; font-size:20px;">
                <td><strong>GIF</strong></td>
                <td><strong>Video</strong></td>
            </tr>
            <tr>
                <td><img src="InsertionSort.gif" alt="Insertion Sort GIF" width="525" height="315"/></td>
                <td><iframe width="560" height="315" src="https://www.youtube.com/embed/JU767SDMDvA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></td>
            </tr>
        </table>
    </tr>
    <tr>
        <table>
            <tr style="text-align: center; font-size:20px;">
                <td><strong>Python Implementation</strong></td>
            </tr>
            <tr>
                <td markdown="block">
                    
{% highlight python %}
def insertion_sort(ary):
    if len(ary) < 2: return
    for i in range(1, len(ary)):
        key, j = ary[i], i - 1
        while j >= 0 and ary[j] > key: 
            ary[j+1], j = ary[j], j - 1
        ary[j+1] = key
{% endhighlight %}
                    
            </td></tr>
        </table>
    </tr>
</table>