from typing import List
def find_two_sum_indices(nums: List[int], target: int) -> List[int]:
    """
    Finds the indices of two numbers in the given list that add up to the target value.

    Args:
        nums (List[int]): The list of numbers.
        target (int): The target value.

    Returns:
        List[int]: The indices of the two numbers that add up to the target value.
    """
    num_to_index = {}
    for i, num in enumerate(nums):
        dif = target - num
        if dif in num_to_index:
            return [num_to_index[dif], i]
        num_to_index[num] = i

print(find_two_sum_indices(nums=[2, 7, 11, 15], target=9))