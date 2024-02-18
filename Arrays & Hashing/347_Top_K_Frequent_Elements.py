from collections import Counter


def main(numbers, top_k):
    counter = Counter(numbers)
    max_values = sorted(counter.values(), reverse=True)[:top_k]
    top_n_keys = [key for key, value in counter.items() if value in max_values]
    return top_n_keys[:top_k]

if  __name__ == "__main__":
    print(main(nums = [1,1,1,2,2,3], k = 2))