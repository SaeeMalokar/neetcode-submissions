class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        li = []
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        for i in range(k):
            max_key = max(hashmap, key = hashmap.get)
            li.append(max_key)
            del hashmap[max_key]
        return li
        