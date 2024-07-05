def dict_solution(nums, target):
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen:
            return (seen[nums[i]],i)
        else:
            seen[target - nums[i]] = i #the corresponding pair for future searchs

def brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i,j)

def main():
    nums = [2,7,11,15]
    target = 9
    print(dict_solution(nums,target))
    print(brute_force(nums,target))
main()