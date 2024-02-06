def contains_duplicates(nums):
    myset = set(nums)
    return not len(nums) == len(myset)

if __name__=="__main__":
    print(contains_duplicates(nums = [1,2,3,1]))