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

def bubble_sort(ary):
    n = len(ary)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if ary[j] > ary[j+1]:
                ary[j], ary[j+1] = ary[j+1], ary[j]
    
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


ary1 = [6,8,4,8,3,9,3,0,1,2,5,4,3,7,9,4,5]
insertion_sort(ary1)
print(ary1)
ary2 = [6,8,4,8,3,9,3,0,1,2,5,4,3,7,9,4,5]
selection_sort(ary2)
print(ary2)
ary3 = [6,8,4,8,3,9,3,0,1,2,5,4,3,7,9,4,5]
bubble_sort(ary3)
print(ary3)
ary4 = [6,8,4,8,3,9,3,0,1,2,5,4,3,7,9,4,5]
merge_sort(ary4)
print(ary4)


ary = [1,2,3,4]
print(ary[0:0])



