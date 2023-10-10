#Quick SOrt
def qsorting(arr,start,end):
    pivot=arr[end]
    i=start-1
    for j in range(start,end):
        if arr[j]<pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[end]=arr[end],arr[i+1]
    return i+1
def quicksort(arr,start,end):
    if start<end:
        pivot=qsorting(arr,start,end)
        quicksort(arr,0,pivot-1)
        quicksort(arr,pivot+1,end)
        
arr=list(map(int,input().split()))
l=len(arr)
quicksort(arr,0,l-1)
print(arr)
