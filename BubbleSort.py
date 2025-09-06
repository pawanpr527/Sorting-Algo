def BubbleSort(arr):
    for i in range(0,len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1] 
        print(arr)
    return arr
arr = [5,2,4,6,2,9,8]
print(BubbleSort(arr))
