def CountingSort(arr):
    #count frequency
    max_element = max(arr)
    n = max_element+1
    freq = [0]*n
    for i in arr:
        freq[i]+=1
    # print(freq)
    #cumulative freq
    for i in range(1,n):
        freq[i]+=freq[i-1]
    print(freq)
    output = [None]*len(arr)
    
    for i in range(len(arr)-1,-1,-1):
        num = arr[i]
        pos = freq[num]-1
        output[pos]=num
        freq[num]-=1
    return output

arr= [12,5,18,8,3,2,24,6]
print(CountingSort(arr))
