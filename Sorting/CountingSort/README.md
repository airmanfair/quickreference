# Counting Sort
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
                <td style="text-align: center;"><a href="https://youtu.be/7zuGmKfUt7s"><img src="http://img.youtube.com/vi/7zuGmKfUt7s/0.jpg" alt="Counting Sort Video" width="560" height="315"/></a></td>
            </tr>
        </table>
    </tr>
</table>

# Python Implementation
``` python
def counting_sort(ary, k):
    n = len(ary)
    output, dist = [0]*n, [0]*(k + 1)
    for x in ary:
        dist[x] += 1
    for i in range(1, k + 1):
        dist[i] += dist[i-1]
    for i in range(n-1, -1, -1):
        output[dist[ary[i]]-1] = ary[i]
        dist[ary[i]] -= 1
    return output
```

# Java Implementation
``` java
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
```