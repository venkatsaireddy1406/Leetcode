import math
def main(nums):
    if not nums:
        return []
    
    n = len(nums)
    productList = [1] * n
    preFix = 1
    for i in range(n):
        productList[i] = preFix
        preFix *= nums[i]           
    
    postFix = 1
    for i in range(n-1, -1, -1):
        productList[i] *= postFix
        postFix *= nums[i]     
    
    return productList

if __name__== '__main__':
    print(main(nums = [-1,1,0,-3,3]))