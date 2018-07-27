def binary(search,ele):
    fisrt=0
    last=len(search)-1
    found=False
    while fisrt<=last and not found:
        mid=(fisrt+last)/2
        if search[mid]==ele:
            found=True
        else:
            if ele<search[mid]:
                return binary(search[:mid],ele)
            else:
                return binary(search[mid+1:],ele)
    return found
s=[1,2,3,4,5,6,7,8,9]
ele=15
print binary(s,ele)
