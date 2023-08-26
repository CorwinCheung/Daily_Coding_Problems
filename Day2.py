def using_division(nums):
    total = 1
    for i in range(len(nums)):
        total *= nums[i]

    new_list = []

    for i in range(len(nums)):
        new_list.append(int(total / nums[i]))

    return new_list


# O(n) time, O(n) space, loop through to make the new array, using division


def save_before_after(nums):
    before = [1]
    for i in range(len(nums) - 1):
        before.append(before[i] * nums[i])

    after = [1]
    for i in range(len(nums) - 1):
        after.append(after[i] * nums[len(nums) - i - 1])

    after.reverse()

    new_list = []

    for i in range(len(nums)):
        new_list.append(before[i] * after[i])

    return new_list


# O(n) time, O(n) space, precompute the multiplication values of before and after, and for i, do before[i-1]*after[i+1]
# This approach stems from the fact that we can get the product of numbers without the current one by multiplying the numbers that come
# before that and the product of the numbers that come after that.
# For trickier code constructions like this one, make sure to run through an example as if you are the computer and whiteboard
# out what you need to do


def main():
    numbers = [1, 2, 3, 4, 5]
    print(save_before_after(numbers))


main()
