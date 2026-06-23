class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = {}
        for i in range(len(strs)):
            sortt = ''.join(sorted(strs[i]))
            if sortt not in mapp:
                mapp[sortt] = [strs[i]]
            else:
                mapp[sortt].append(strs[i])
        return list(mapp.values()) 
        