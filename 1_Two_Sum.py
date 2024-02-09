def main(nums,target):
    numMap = {}
    n = len(nums)
    for i in range(n):
        dif = target - nums[i]
        if dif in numMap:
            return [numMap[dif], i]
        numMap[nums[i]] = i

if __name__=="__main__":
    print(main(nums = [2,7,11,15], target = 9))