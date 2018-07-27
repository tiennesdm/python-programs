def selection(arr):
    for i in range(len(arr)-1,0,-1):
        positionofmax=0
        for location in range(1,i+1):
            if arr[location]>arr[positionofmax]:
                positionofmax=location
        temp=arr[i]
        arr[i]=arr[positionofmax]
        arr[positionofmax]=temp
arr=[1,25,4,66,77,12,14]
selection(arr)
print arr


