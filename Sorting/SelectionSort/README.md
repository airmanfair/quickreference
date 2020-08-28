# Selection Sort
<table>
    <tbody>
        <tr>
            <td><strong><i>Class</i></strong></td>
            <td><strong><i>Type</i></strong></td>
            <td><strong><i>Category</i></strong></td>
            <td><strong><i>Time</i></strong></td>
            <td><strong><i>Space</i></strong></td>
        </tr>
        <tr>
            <td><a href="/Sorting/">Sorting</a></td>
            <td>In-place</td>
            <td>Naive</td>
            <td><i>O</i>(n<sup>2</sup>)</td>
            <td><i>O</i>(1)</td>
        </tr>
    </tbody>
    <tfoot></tfoot>
</table>

# GIF and Video References

![Alt Text](SelectionSort.gif)[![http://img.youtube.com/vi/g-PGLbMth_g/0.jpg](http://img.youtube.com/vi/g-PGLbMth_g/0.jpg)](https://youtu.be/g-PGLbMth_g "Selection Sort")

# Python Implementation
``` python
def selection_sort(ary):
    n = len(ary)
    for i in range(n):
        i_min = i
        for j in range(i+1, n):
            if ary[j] < ary[i_min]:
                i_min = j
        ary[i], ary[i_min] = ary[i_min], ary[i]
```