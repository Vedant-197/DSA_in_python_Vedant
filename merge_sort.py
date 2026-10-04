import numpy as np

def merge(arr,st,mid,end):
    temp = []
    i = st
    j = mid + 1

    while((i <= mid) and (j <= end)):
        if (arr[i] <= arr[j]):
            temp.append(arr[i]) 
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= end:
        temp.append(arr[j])
        j += 1

    for index in range(0,len(temp)):
        arr[index + st] = temp[index]

def merge_sort(arr,st,end):
    if st >= end: 
        return
    mid = st + (end - st)//2
    merge_sort(arr,st,mid)
    merge_sort(arr,mid + 1, end)
    merge(arr,st,mid,end)

arr = np.array(list(map(int,input("Enter Elements of an Array: ").split())))
merge_sort(arr,0,(len(arr)-1)) 
print(f"Sorted Elements in Given Array: {arr}")