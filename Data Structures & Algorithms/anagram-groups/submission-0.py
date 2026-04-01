class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        w_dict = {}
        
        for s in strs:
            key = ''.join(sorted(s))
            if key in w_dict.keys():
                w_dict[key].append(s)
            else:
                w_dict[key] = [s]

        return list(w_dict.values())