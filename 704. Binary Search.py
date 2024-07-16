#Binary search nums for target, return index or -1 if not in

def search(nums,target):
    l,r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid -1
    return -1 

def main():
    nums = [-1,0,3,5,9,12]
    target = 9
    print(search(nums,target))

main()