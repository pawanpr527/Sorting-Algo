def ShellSort(arr):
    n = len(arr)
    gap = n // 2   # start with a big gap

    while gap > 0:
        print(f"\nGap = {gap}")
        
        # Do a gapped insertion sort
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # Shift elements that are greater than temp
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        
        print("Array after this gap:", arr)
        gap //= 2   # reduce the gap
    
    return arr


# Example
arr = [8, 5, 3, 7, 6, 2, 4, 1]
print("Original:", arr)
sorted_arr = ShellSort(arr)
print("\nFinal Sorted:", sorted_arr)
