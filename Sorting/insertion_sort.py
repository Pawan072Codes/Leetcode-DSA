def insertion_sort(nums):
    for i in range (1, len(nums)):
        key = nums[i]
        j = i-1
        while j>=0 and nums[j]>key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key

    return nums

n = list(map(int, input("Enter the elements separated by space we want to sort: ").split()))


print(insertion_sort(n))