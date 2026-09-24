# To sort the list in Acending order if list are sorted/unsorted using bubble sort algorithm.
def bubble_sort(nums):
    for i in range (len(nums)-2 , -1 ,-1 ):
        for j in range(0 , i+1):
            if nums[j] >nums [j+1]:

                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return nums            

n = list(map(int, input("Enter the elements separated by space we want to sort: ").split()))


print(bubble_sort(n))