# Merge Sort
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
                <td><a href="/Sorting/">Sorting</a></td>
                <td>Divide & Conquer</td>
                <td>Efficient</td>
                <td><i>O</i>(n log n)</td>
                <td><i>O</i>(n)</td>
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
                <td><img src="MergeSort.gif" alt="Merge Sort GIF" width="525" height="315"/></td>
                <td><a href="https://youtu.be/4VqmGXwpLqc"><img src="http://img.youtube.com/vi/4VqmGXwpLqc/0.jpg" alt="Merge Sort Video" width="560" height="315"/></a></td>
            </tr>
        </table>
    </tr>
</table>

# Python Implementation
``` python
def merge_sort(ary):
    
    def merge(start, mid, end):
        left, right = ary[start:mid+1] + [float('inf')], ary[mid+1:end+1] + [float('inf')]
        i, j = 0, 0
        for k in range(start, end+1):
            if left[i] <= right[j]:
                ary[k], i = left[i], i + 1
            else:
                ary[k], j = right[j], j + 1
    
    def sort(start, end):
        if start < end:
            mid = (start+end)//2
            sort(start, mid)
            sort(mid+1, end)
            merge(start, mid, end)
    
    sort(0, len(ary)-1)
```

# Java Implementation
``` java
static void merge(int[] ary, int start, int mid, int end) {
    int n = mid - start + 1, m = end - mid;
    int[] left = new int[n+1], right = new int[m+1];
    for (var i = 0; i < n; i++) {
        left[i] = ary[i+start];
    }
    for (var i = 0; i < m; i++) {
        right[i] = ary[i+mid+1];
    }
    left[n] = right[m] = Integer.MAX_VALUE;
    int i = 0, j = 0;
    for (var k = start; k <= end; k++) {
        if (left[i] <= right[j]) {
          ary[k] = left[i++];
        } else {
            ary[k] = right[j++];
        }
    }
}

static void sort(int[] ary, int start, int end) {
    if (start < end) {
        int mid = (start + end) / 2;
        sort(ary, start, mid);
        sort(ary, mid+1, end);
        merge(ary, start, mid, end);
    }
}

static void merge_sort(int[] ary) {
    sort(ary, 0, ary.length-1);
}
```