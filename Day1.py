def brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False


# O(n^2) time, because we use a doubly nested for loop that runs n^2 times, n times on the outside, and n times for each of those runs on the inside


def sorting(nums, target):
    def binarySearch(numbers, target):
        l = 0
        r = len(numbers) - 1
        while l <= r:
            mid = (l + r) // 2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    sorted_nums = sorted(nums)
    for i in range(len(sorted_nums)):
        res = binarySearch(sorted_nums, target - sorted_nums[i])
        if res != -1 and res != i:
            return True
    return False


# O(n log n) because binary search for the best key N times, intuitive binary search implementation, with O(1) space


def one_pass(nums, target):
    seen = set()

    for i in range(len(nums)):
        if target - nums[i] in seen:
            return True
        seen.add(nums[i])
    return False


# O(n) time, because adding to a set and looking up in a set is a O(1) operation, happens N times


def main():
    # naive solution
    example = [10, 9, 9, 15, 6, 11]
    number = 18
    print(sorting(example, number))


main()
