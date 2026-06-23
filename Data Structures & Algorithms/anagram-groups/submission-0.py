class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = {}
        li = []
        for i in range(len(strs)):
            sortt = ''.join(sorted(strs[i]))
            if sortt not in mapp:
                mapp[sortt] = [strs[i]]
            else:
                mapp[sortt].append(strs[i])
        for keys in mapp:
            li.append(mapp[keys])
        return li 
        
        