
# Think about sorting as well, O(1) space, O(N log n) time

def sort(arr):
    arr = sorted(arr)
    arr = [a for a in arr if a > 0]

    for i in range(1, len(arr)+1):
        if i != arr[i-1]:
            return i
    return len(arr) + 1


def with_space(arr):
    if not arr:
        return 1

    arr_set = set(arr)

    for i in range(len(arr)):
        if i+1 not in arr_set:
            return i+1

# O(N) time, O(n) space, hash set, at most n lookups, each lookup is O(1)


def constant_space(arr):
    if not arr:
        return 1

    counter = 0
    while counter < len(arr):
        i = counter
        if arr[i] != i and arr[i] >= 0 and arr[i] < len(arr):
            temp = arr[i]
            arr[i], arr[temp] = arr[temp], arr[i]
        else:
            counter += 1

    for i in range(1, len(arr)):
        if i != arr[i]:
            return i
    return len(arr)


# O(N) time, O(1) space, gotta be in place swaps and checks if it is in the right place
# Loop through after and see if 1 is in the 1s place, 2 is in the 2s place, etc.

def main():
    arr = [3, 4, -1, 1]
    arr2 = [1, 2, 0]

    # print(with_space(arr))
    # print(with_space(arr2))

    print(constant_space(arr))
    print(constant_space(arr2))

    # print(sort(arr))
    # print(sort(arr2))


main()
