def insertion(arr):
    for i in range(1,len(arr)):
        currentvale=arr[i]
        position=i
        while position>0  and arr[position-1]>currentvale:
            arr[position]=arr[position-1]
            position=position-1
        arr[position]=currentvale

arr =[3,5,4,6,8,1,2,12,41,25]
insertion(arr)
print arr

