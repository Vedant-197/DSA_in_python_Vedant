import numpy as np

def swap(x,y):
    x,y = y,x
    return x,y

def partition(arr,st,end):
    idx = st - 1
    pivot = arr[end]

    for j in range(st,end):
        if (arr[j] <= pivot):
            idx += 1
            arr[j],arr[idx] = arr[idx],arr[j]

    idx += 1
    arr[end],arr[idx] = arr[idx],arr[end]
    return idx
        

def quick_sort(arr,st,end):
    if (st < end):
        pividx = partition(arr,st,end)
        quick_sort(arr,st,pividx - 1)
        quick_sort(arr,pividx + 1,end)



arr = np.array(list(map(int,input("Enter the Elements of an Array: ").split())))
quick_sort(arr,0,len(arr) - 1)
print(arr," ")
