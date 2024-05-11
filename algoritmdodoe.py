def binerysearch (list,target):
    left , right = 0, len(list)-1

    while left<= right:
        mid=(left+right)//2
        if list[mid] == target:
            return mid
        elif list[mid]<target:
            left= mid+1
        else:
            right=mid-1
        return -1
list=[1,2,3,4,5]
target= 6
result = binerysearch(list,target)
if result != -1:
    print("yaft shod index = ", result)
else:
    print("yaft nakardam =" , result) 
