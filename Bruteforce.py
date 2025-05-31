def two_sum_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum_brute_force(nums, target)
print("Indices (Brute Force) of numbers that sum to", target, ":", result)

