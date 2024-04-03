n = int(input())
nums = [0, 1]

for i in range(n-1):
    result = nums[i] + nums[i+1]
    nums.append(result)

print(nums[n])