def main(numbers,target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return [] 

if  __name__ == "__main__":
    print(main( numbers = [2,7,11,15], target = 9))