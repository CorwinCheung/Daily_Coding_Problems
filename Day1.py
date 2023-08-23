
def brute_force(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False
# O(n^2) time, because we use a doubly nested for loop that runs n^2 times, n times on the outside, and n times for each of those runs on the inside


def one_pass(nums, target):
    seen = set()

    for i in range(len(nums)):
        if(target - nums[i] in seen):
            return True
        seen.add(nums[i])
    return False
# O(n) time, because adding to a set and looking up in a set is a O(1) operation, happens N times

def main():
    #naive solution
    example = [10,15,3,5]
    number = 17
    print(one_pass(example, number))


main()