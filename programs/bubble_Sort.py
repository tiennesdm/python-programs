def bubble_sort(arr):
    for n in range(len(arr)-1,0,-1):
        for k in range(n):
            if arr[k]>arr[k+1]:
                temp=arr[k+1]
                arr[k+1]=arr[k]
                arr[k+1]=temp




arr=[1,2,3,5,4,6,7]
bubble_sort(arr)
print arr
