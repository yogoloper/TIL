from re import M


def binary_search(nums, target):
    def bs(start, end):
        if start > end:
            return -1
        
        mid = (start + end) // 2
        
        if nums[mid] < target:
            return bs(mid + 1, end)
        elif nums[mid] > target:
            return bs(start, mid - 1)
        else:
            return mid
        
    result = bs(0, len(nums) - 1)
    if result != -1:
        print(result)
    else:
        print('원소가 존재하지 않습니다.')

n, m = map(int, input().split())
nums = list(map(int, input().split()))

binary_search(nums, m)