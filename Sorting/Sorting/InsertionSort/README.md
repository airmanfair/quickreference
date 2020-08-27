# Insertion Sort
<table class="not a rip-off table">
    <tbody>
        <tr>
            <td><strong><i>Problem Class</i></strong></td>
            <td><strong><i>Problem Type</i></strong></td>
            <td><strong><i>Category</i></strong></td>
            <td><strong><i>Time Complexity</i></strong></td>
            <td><strong><i>Space Complexity</i></strong></td>
        </tr>
        <tr>
            <td>Sorting</td>
            <td>In-place</td>
            <td>Naive</td>
            <td><i>O</i>(n<sup>2</sup>)</td>
            <td><i>O</i>(1)</td>
        </tr>
    </tbody>
    <tfoot></tfoot>
</table>

# GIF and Video References

![Alt Text](https://upload.wikimedia.org/wikipedia/commons/9/9c/Insertion-sort-example.gif)[![http://img.youtube.com/vi/JU767SDMDvA/0.jpg](http://img.youtube.com/vi/JU767SDMDvA/0.jpg)](https://youtu.be/JU767SDMDvA "Insertion Sort")


# Python Implementation
``` python
def insertion_sort(ary):
    if len(ary) < 2: return ary
    for i in range(1, len(ary)):
        key, j = ary[i], i - 1
        while j >= 0 and ary[j] > key: 
            ary[j+1], j = ary[j], j - 1
        ary[j+1] = key
    return ary
```