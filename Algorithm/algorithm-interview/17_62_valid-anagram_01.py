class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst1 = sorted(list(s))
        lst2 = sorted(list(t))
        
        if ''.join(lst1) == ''.join(lst2):
            return True
        else:
            return False

s = "anagram"
t = "nagaram"
o = Solution()
print(o.isAnagram(s, t))
