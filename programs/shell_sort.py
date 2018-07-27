def shell_sort(arr):
    sublist=len(arr)/2
    while sublist>0:
        for i in range(sublist):
            gap_insertion_sort(arr,start,sublist)
        sublist=sublist/2
def gap_insertion_sort(arr,start,sublist):
    for i in range

