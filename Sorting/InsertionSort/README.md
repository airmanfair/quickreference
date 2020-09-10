# Insertion Sort
<table>
    <tr>
        <table>
            <tr>
                <td><strong><i>Class</i></strong></td>
                <td><strong><i>Type</i></strong></td>
                <td><strong><i>Category</i></strong></td>
                <td><strong><i>Space</i></strong></td>
                <td><strong><i>Time</i></strong></td>
                <td><strong><i>Average</i></strong></td>
            </tr>
            <tr>
                <td><a href="/Sorting/">Sorting</a></td>
                <td>In-place</td>
                <td>Naive</td>
                <td><i>O</i>(1)</td>
                <td><i>O</i>(n<sup>2</sup>)</td>
                <td><i>Θ</i>(n<sup>2</sup>)</td>
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

# Java Implementation
``` java
static void insertion_sort(int[] ary) {
    if (ary.length < 2) { 
        return;
    }
    for (var i = 1; i < ary.length; i++) {
        int key = ary[i], j = i - 1;
        while (j >= 0 && ary[j] > key) {
            ary[j+1] = ary[j];
            j -= 1;
        } 
        ary[j+1] = key;
    }
}
```