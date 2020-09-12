# Bubble Sort
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
                <td>In-place</td>
                <td>Naive</td>
                <td>Array</td>
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
                <td><a href="https://youtu.be/xli_FI7CuzA"><img src="http://img.youtube.com/vi/xli_FI7CuzA/0.jpg" alt="Bubble Sort Video" width="560" height="315"/></a></td>
            </tr>
        </table>
    </tr>
</table>

# Python Implementation
``` python
def bubble_sort(ary):
    n = len(ary)
    for i in range(n):
        for j in range(n-1, i, -1):
            if ary[j] < ary[j-1]:
                ary[j], ary[j-1] = ary[j-1], ary[j]
```

# Java Implementation
``` java
static void bubble_sort(int[] ary) {
    for (int i = ary.length - 1; i > 0; i--) {
        for (int j = 0; j < i; j++) {
            if (ary[j] > ary[j+1]) {
                int temp = ary[j];
                ary[j] = ary[j+1];
                ary[j+1] = temp;
            }
        }
    }
}
```