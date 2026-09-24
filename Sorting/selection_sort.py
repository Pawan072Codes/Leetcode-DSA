# To sort the list in Acending order using selection sort algorithm.

def selection_sort(nums):
    for i in range(0 , len(nums)-1):
        min_index = i 
        for j in range (i +1 , len(nums)):
            if nums[j] < nums[min_index]:
                    min_index = j
        temp = nums[i]
        nums[i]= nums[min_index]
        nums[min_index] = temp
    return nums



n = list(map(int, input("Enter the elements separated by space we want to sort: ").split()))


print(selection_sort(n))

