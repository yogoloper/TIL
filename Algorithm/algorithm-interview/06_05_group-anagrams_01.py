class Solution(object):
    def groupAnagrams(self, strs):
        result = []
        check = [0]*len(strs)

        for i in range(len(strs)):
            if check[i] == 0:
                group = [strs[i]]
                check[i] = 1
            else:
                continue

            temp_1 = ''.join(sorted(strs[i]))
            for j in range(i+1, len(strs)):
                temp_2 = ''.join(sorted(strs[j]))
                if temp_1 == temp_2 and check[j] == 0:
                    group.append(strs[j])
                    check[j] = 1
            result.append(sorted(group))

        return result