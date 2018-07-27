def binary(ele,search):
    first=0
    last=len(search)-1
    found=False
    while first<=last and not found:
        mid=(first+last)/2
        if search[mid]==ele:
            found=True
        else:
            if ele<search[mid]:
                last=mid-1
            else:
                first=mid+1
    return found
s=[1,2,3,4,6,9]
ele=4
print binary(ele,s)

