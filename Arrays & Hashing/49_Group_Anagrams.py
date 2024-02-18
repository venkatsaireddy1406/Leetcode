from typing import List
from collections import defaultdict

def group_anagrams(strs: List[str]) -> List[List[str]]:
    if strs is None or not isinstance(strs, list):
        return []
    anagram_groups = defaultdict(list)
    for s in strs:
        sorted_string = ''.join(sorted(s))
        anagram_groups[sorted_string].append(s)
    return list(anagram_groups.values())

if __name__=="__main__":
    pass
    print(group_anagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
