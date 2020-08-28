# Sorting Algorithms
<head>
    <link rel="stylesheet" href="/quickreference/assets/css/table.css">
</head>
<body>
    <table class="full">
        <tr>
            <td><strong><i>Name</i></strong></td>
            <td><strong><i>Type</i></strong></td>
            <td><strong><i>Category</i></strong></td>
            <td><strong><i>Time</i></strong></td>
            <td><strong><i>Space</i></strong></td>
        </tr>
        <tr>
            <td><a href="/quickreference/Sorting/InsertionSort/InsertionSort">Insertion Sort</a></td>
            <td>In-place</td>
            <td>Naive</td>
            <td><i>O</i>(n<sup>2</sup>)</td>
            <td><i>O</i>(1)</td>
        </tr>
        <tr>
            <td><a href="/quickreference/Sorting/SelectionSort/SelectionSort">Selection Sort</a></td>
            <td>In-place</td>
            <td>Naive</td>
            <td><i>O</i>(n<sup>2</sup>)</td>
            <td><i>O</i>(1)</td>
        </tr>
    </table>
</body>

# Python Implementations
``` python
def insertion_sort(ary):
    if len(ary) < 2: return
    for i in range(1, len(ary)):
        key, j = ary[i], i - 1
        while j >= 0 and ary[j] > key: 
            ary[j+1], j = ary[j], j - 1
        ary[j+1] = key
        
def selection_sort(ary):
    n = len(ary)
    for i in range(n):
        i_min = i
        for j in range(i+1, n):
            if ary[j] < ary[i_min]:
                i_min = j
        ary[i], ary[i_min] = ary[i_min], ary[i]
```