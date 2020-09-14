# Radix Sort
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
                <td><i>O</i>(n + d)</td>
                <td><i>O</i>(d*(n + b))</td>
                <td><i>O</i>(d*(n + b))</td>
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
                <td style="text-align: center;"><img src="RadixSort.gif" alt="Radix Sort GIF" style="width: auto; height: 315px;"/></td>
                <td style="text-align: center;"><a href="https://youtu.be/nu4gDuFabIM"><img src="http://img.youtube.com/vi/nu4gDuFabIM/0.jpg" alt="Radix Sort Video" width="560" height="315"/></a></td>
            </tr>
        </table>
    </tr>
</table>

# Python Implementation
``` python
def radix_sort(ary):
    
    def counting_sort(output):
        ary, dist = output[:], [0]*10
        for x in ary:
            dist[(x//denom)%10] += 1
        for i in range(1, 10):
            dist[i] += dist[i-1]
        for i in range(n-1, -1, -1):
            j = (ary[i] // denom) % 10
            output[dist[j]-1] = ary[i]
            dist[j] -= 1
    
    n, m, denom = len(ary), max(ary), 1
    
    while m > denom:
        counting_sort(ary)
        denom *= 10
```

# Java Implementation
``` java
static void counting_sort(int[] output, int denom) {
    int[] ary = new int[output.length], dist = new int[10];
    System.arraycopy(output, 0, ary, 0, output.length);
    for (int x : ary) {
        dist[(x/denom)%10]++;
    }
    for (int i = 1; i < 10; i++) {
        dist[i] += dist[i-1];
    }
    for (int i = ary.length - 1; i >= 0; i--) {
        int j = (ary[i] / denom) % 10;
        output[dist[j]-1] = ary[i];
        dist[j]--;
    }
}

static void radix_sort(int[] ary) {
    int m = Integer.MIN_VALUE, denom = 1;
    for (int x: ary) {
        if (x > m) {
            m = x;
        }
    }
    while (m > denom) {
        counting_sort(ary, denom);
        denom *= 10;
    }
}
```