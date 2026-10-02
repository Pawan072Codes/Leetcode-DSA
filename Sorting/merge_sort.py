def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)
    return merge_sorted_array(left_arr, right_arr)

def merge_sorted_array(left , right):
    final_array=[]
    i =0
    j =0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            final_array.append(left[i])
            i += 1
        else:
            final_array.append(right[j])
            j += 1
    if i <len(left):
        while i < len(left):
            final_array.append(left[i])
            i += 1
    if j < len(right):
        while j < len(right):
            final_array.append(right[j])
            j += 1
    return final_array

n = list(map(int, input("Enter the elements separated by space we want to sort: ").split()))
print(merge_sort(n))


