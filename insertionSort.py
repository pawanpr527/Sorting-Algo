def insertionSort(arr):
    for i in range(1,len(arr)):
        j=i-1
        key = arr[i]
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

arr = [2,4,3,1,6,8,3]
print(insertionSort(arr))
            
