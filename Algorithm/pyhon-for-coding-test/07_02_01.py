from bisect import bisect_left


def search_intersection(nums1, nums2):
    ans = []
    
    nums1.sort()
    nums2.sort()
    
    for i in nums2:
        idx = bisect_left(nums1, i)
        
        if idx < len(nums1) and nums1[idx] == i:
            ans.append('yes')
        else:
            ans.append('no')
            
    print(' '.join(ans))
    
    
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
search_intersection(nums1, nums2)