# Selection Sort
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
			    <td><a href="/quickreference/Sorting/Sorting">Sorting</a></td>
			    <td>In-place</td>
			    <td>Naive</td>
			    <td><i>O</i>(n<sup>2</sup>)</td>
			    <td><i>O</i>(1)</td>
			</tr>
		</table>
	</tr>
	<tr>
		<table>
			<tr style="text-align: center; font-size:20px;">
				<td><strong>GIF</strong></td>
				<td><strong>Video</strong></td>
			</tr>
		    <tr>
		        <td><img src="SelectionSort.gif" alt="Selection Sort GIF" width="100" height="315"/></td>
		        <td><href="https://youtu.be/g-PGLbMth_g"><img src="http://img.youtube.com/vi/g-PGLbMth_g/0.jpg" alt="Selection Sort Video" width="560" height="315"/></href></td>
		    </tr>
		</table>
	</tr>
</table>

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