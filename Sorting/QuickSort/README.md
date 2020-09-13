# Quick Sort
<table>
    <tr>
        <table>
            <tr>
                <td><strong><i>Class</i></strong></td>
                <td><strong><i>Type</i></strong></td>
                <td><strong><i>Category</i></strong></td>
                <td><strong><i><a href="/DataStructures/">Data Structure</a></i></strong></td>
                <td><strong><i>Space</i></strong></td>
                <td><strong><i>Time: Worst</i></strong></td>
                <td><strong><i>Time: Average</i></strong></td>
            </tr>
            <tr>
                <td><a href="/Sorting/">Sorting</a></td>
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
                <td><a href="https://youtu.be/Hoixgm4-P4M"><img src="http://img.youtube.com/vi/Hoixgm4-P4M/0.jpg" alt="Quick Sort Video" width="560" height="315"/></a></td>
            </tr>
        </table>
    </tr>
</table>

# Python Implementation
``` python
def quick_sort(ary, start, end):
    
    def partition(start, end):
        x, i = ary[end], start - 1
        for j in range(start, end):
            if ary[j] <= x:
                i += 1
                ary[i], ary[j] = ary[j], ary[i]
        ary[i+1], ary[end] = ary[end], ary[i+1]
        return i + 1
    
    if start < end:
        mid = partition(start, end)
        quick_sort(ary, start, mid - 1)
        quick_sort(ary, mid + 1, end)
```

# Java Implementation
``` java
static int partition(int[] ary, int start, int end) {
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

static void quick_sort(int[] ary, int start, int end) {
    if (start < end) {
        int mid = partition(ary, start, end);
        quick_sort(ary, start, mid - 1);
        quick_sort(ary, mid + 1, end);
    }
}
```