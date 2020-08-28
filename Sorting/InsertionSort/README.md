# Insertion Sort
<table  width=100% cellspacing=0%>
    <tr>
        <table  width=100%>
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
        <table width=100%>
            <tr style="text-align: center; font-size:20px;">
                <td><strong>GIF</strong></td>
                <td><strong>Video</strong></td>
            </tr>
            <tr>
                <td><img src="InsertionSort.gif" alt="Insertion Sort GIF" width="525" height="315"/></td>
                <td><a href="https://youtu.be/JU767SDMDvA"><img src="http://img.youtube.com/vi/JU767SDMDvA/0.jpg" alt="Insertion Sort Video" width="560" height="315"/></a></td>
            </tr>
        </table>
    </tr>
</table>

# Python Implementation
``` python
def insertion_sort(ary):
    if len(ary) < 2: return
    for i in range(1, len(ary)):
        key, j = ary[i], i - 1
        while j >= 0 and ary[j] > key: 
            ary[j+1], j = ary[j], j - 1
        ary[j+1] = key
```