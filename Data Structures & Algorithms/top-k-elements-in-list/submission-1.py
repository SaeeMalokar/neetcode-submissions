class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        li = []
        lis = []
        hashh = {}
        for i in nums:
            if i not in hashh:
                hashh[i] = -1
            else:
                hashh[i] -= 1
        for num, freq in hashh.items():
            li.append((freq, num))
        import heapq
        heapq.heapify(li)
        for i in range(k):
            freq, num = heapq.heappop(li)
            lis.append(num)
        return lis
        