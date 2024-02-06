from collections import Counter


def valid_Anagram(s,t):# S=sorted(s)
    # T=sorted(t)
    # S[:]=s
    # T[:]=t
    # S.sort()
    # T.sort()

    # Compare two strings to see if they are anagrams
    # Using Counter to count characters in each string
    # Return True if both strings have the same characters with same counts
    return Counter(s) == Counter(t)

    # Note: Counter is a dictionary subclass for counting hashable objects
    # s and t are strings that we want to check if they are anagrams

if __name__=="__main__":
    print(valid_Anagram(s = "anagram", t = "nagaram"))