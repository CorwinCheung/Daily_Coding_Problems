def largest_sum(nums):
    best_sum_before_current = 0
    best_sum_before_current_no_prev = 0
    for i in range(len(nums)):
        if best_sum_before_current < best_sum_before_current_no_prev + nums[i]:
            temp = best_sum_before_current
            best_sum_before_current = best_sum_before_current_no_prev + nums[i]
            best_sum_before_current_no_prev = temp
        else:
            best_sum_before_current_no_prev = best_sum_before_current
    return best_sum_before_current


# think about using two different pointers, one that tracks the best up to that point, and
# one that tracks without the previous one, then compare which is optimal and update
# this is the O(n), O(1) space solution, under is the reasoning.
"""
best sum before current 2
best sum before current not including previous 0

"""


def inefficient(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return max(nums[0], 0)
    include = nums[0] + inefficient(nums[2:])
    exclude = inefficient(nums[1:])

    return max(include, exclude)

# recursively either include the current and do the best of the rest excluding the next one
# or exclude the current one, take the max of these two to see the best way. O(2^n)


def memoize(nums):
    memory = {}

    def recurse(nums, i):
        if i >= len(nums):
            return 0
        if i == len(nums) - 1:
            return max(0, nums[i])
        if i in memory:
            return memory[i]
        include = recurse(nums, i+2) + nums[i]
        exclude = recurse(nums, i+1)
        memory[i] = max(include, exclude)
        return memory[i]
    return (recurse(nums, 0))

# Memoize the solutions based on the index, so the time complexity shrinks to O(n)
# because there is no longer exponential branching in calculating the remaining best values


def dynamic_programming(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums, default=0)

    sums = []
    sums.append(max(nums[0], 0))
    sums.append(max(nums[1], sums[0]))

    for i in range(2, len(nums)):
        sums.append(max(sums[i-1], nums[i]+sums[i-2]))

    return sums[-1]

# dynamically get the base case sums and then propagate outwards with the recurrence relation
# corresponding to include or exclude. O(n) time O(n) space.


def main():
    arr = [2, 4, 6, 2, 5]
    print(largest_sum(arr))
    print(inefficient(arr))
    print(dynamic_programming(arr))
    print(memoize(arr))


main()
