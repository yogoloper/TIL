class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}

        for str in strs:
            key = ''.join(sorted(str))
            if key in anagrams:
                anagrams[key].append(str)
            else:
                anagrams[key] = [str]
        for key in anagrams:
            anagrams[key] = sorted(anagrams[key])
            
        return anagrams.values()