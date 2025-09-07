def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0-9

    # Count digit occurrences
    for i in arr:
        idx = (i // exp) % 10
        count[idx] += 1

    # Prefix sum (to place elements correctly)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output (stable order)
    for i in reversed(range(n)):
        idx = (arr[i] // exp) % 10
        output[count[idx] - 1] = arr[i]
        count[idx] -= 1

    return output

def radix_sort(arr):
    if not arr:
        return []

    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10
    return arr

arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))
