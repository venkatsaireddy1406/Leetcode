def contains_duplicates(nums): # Function to check for duplicates in list
   myset = set(nums) # Create a set from list (duplicates removed)
   return not len(nums == len(myset)) # Compare lengths of list and set

if __name__=="__main__":
    print(contains_duplicates(nums = [1,2,3,1]))