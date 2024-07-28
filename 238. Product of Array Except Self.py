#Compute the product of the array except for the current index, without using division, return the array
def product_except_self(array):
    #preorder = [1,1,2,6]
    #postorder = [24,12,4,1]
    preorder = [1]
    running_product = 1
    for i in range(len(array)-1):
        running_product *= array[i]
        preorder.append(running_product)
    
    postorder = [1]
    running_product = 1
    for i in range(len(array)-1, 0, -1):
        running_product *= array[i]
        postorder.append(running_product)
    postorder.reverse()

    ans = []
    for i in range(len(array)):
        ans.append(preorder[i] * postorder[i])
    
    return ans

def constant_space_complexity(array):
    ans = [1] * len(array)
    #ans = [1,1,1,1]
    current = 1
    #preorder comp
    for i in range(len(array)):
        ans[i] = ans[i] * current
        current = current * array[i]
    #ans = [1,1,2,6]
    current = 1
    #postorder comp
    for i in range(len(array)-1,-1,-1):
        ans[i] = ans[i] * current
        current = current * array[i]
    #ans = [24,12,8,6]
    return ans
    

def main():
    nums = [1,2,3,4]
    print(product_except_self(nums))
    print(constant_space_complexity(nums))
main()