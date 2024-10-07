def binarysearch(seq,low,high,elem):
    if low > high:
        return -1
    else:
        middle=(low+high)//2

        if elem == seq[middle]:
            return middle
        elif elem < seq[middle] :
            return binarysearch(seq,low,middle-1,elem)
        else:
            return binarysearch(seq,middle+1,high,elem)

mylist=[1,2,3,4,5,6,7]

print(binarysearch(mylist,0,len(mylist),6))