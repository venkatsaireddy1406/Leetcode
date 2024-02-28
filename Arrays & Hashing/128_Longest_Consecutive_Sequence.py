def main(nums):

    if not nums:
        return 0

    unique_nums = set(nums)
    max_sequence_length = 0

    for current_number in unique_nums:
        if current_number - 1 not in unique_nums:
            current_sequence = 1
            while current_number + 1 in unique_nums:
                current_number += 1
                current_sequence += 1
            max_sequence_length = max(max_sequence_length, current_sequence)

    return max_sequence_length

if  __name__ == "__main__":
     print(main(nums = [100,4,200,1,3,2]))