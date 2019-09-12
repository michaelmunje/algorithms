def twoSum(nums: [int], target: int) -> [int]:
    old_indices = dict()
    for i in range(len(nums)):
        if nums[i] in old_indices.keys():
            old_indices[nums[i]] += [i]
        else:
            old_indices[nums[i]] = [i]
    sorted_nums = sorted(nums)
    i = 0
    j = len(sorted_nums) - 1
    while not i == j:
        if sorted_nums[i] + sorted_nums[j] == target:
            if sorted_nums[i] == sorted_nums[j]:
                return old_indices[sorted_nums[i]][0], old_indices[sorted_nums[i]][1]
            else:
                return (old_indices[sorted_nums[i]][0], old_indices[sorted_nums[j]][0]) if old_indices[sorted_nums[i]][0] < old_indices[sorted_nums[j]][0] else (old_indices[sorted_nums[j]][0], old_indices[sorted_nums[i]][0])
        elif sorted_nums[i] + sorted_nums[j] > target:
            j -= 1
        else:
            i += 1


arr = [3, 5, 2, 7, 1]
print(twoSum(arr, 10))

arr = [3, 3]
print(twoSum(arr, 6))
