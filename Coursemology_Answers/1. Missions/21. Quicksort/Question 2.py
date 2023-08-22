def quick_sort(k, first, last):
    low = first
    high = last
    list_separator = k[int((first + last)/2)]
    while low <= high:
        while k[low] < list_separator:
            low += 1
        while k[high] > list_separator:
            high -= 1
        if low <= high:
            k[low], k[high] = k[high], k[low]
            low += 1
            high -= 1
    if first < high:
        quick_sort(k, first, high)
    if low < last:
        quick_sort(k, low, last)
    return k
