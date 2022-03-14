import collections


class Solution(object):
  def groupAnagrams(self, strs):
      anagrams = collections.defaultdict(list)
      for i in strs:
          anagrams[''.join(sorted(i))].append(i)
      return anagrams.values()