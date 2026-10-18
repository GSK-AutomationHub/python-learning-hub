
def find_max_1(nums):
    if not nums:
        return None
    max_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val

def find_max_2(nums):
    return max(nums)


print(find_max_1([3, 7, 2, 9, 5]))  # Output: 9
print(find_max_2([3, 7, 2, 9, 5]))  # Output: 9
