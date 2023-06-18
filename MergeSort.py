def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) //2
    left=arr[:mid]
    right=arr[mid:]

    left=merge_sort(left)
    right=merge_sort(right)

    return merge_two_list(left,right)

def merge_two_list(left,right):
    sorted_list=[]
    len_a= len(left)
    len_b = len(right)
    i = j = 0

    while i< len_a and len_b:
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1
    while i< len_a:
        sorted_list.append(left[i])
        i+=1

    while j< len_b:
        sorted_list.append(right[j])
        j+=1
    return sorted_list






n=int(input("Enter the size of array="))
arr=[]
for i in range(0,n):
    arr.append(int(input()))
merge_sort(arr)