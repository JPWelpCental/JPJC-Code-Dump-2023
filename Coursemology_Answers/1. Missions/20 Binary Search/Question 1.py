def BinarySearch(arr,key,low,high):
    if low>high:
        return -1
    mid = (low+high)//2
    if arr[mid]==key:
        return mid
    elif arr[mid]>key:
        return BinarySearch(arr,key,low,mid-1)
    else:
        return BinarySearch(arr,key,mid+1,high)
