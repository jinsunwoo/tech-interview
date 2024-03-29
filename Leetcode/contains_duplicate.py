from typing import List

class Solution:
    # brute force
    # t/c: O(n^2), s/c: O(1)
    def containsDuplicate1(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1): 
            for j in range(i+1, len(nums)): 
                if nums[i] == nums[j]:
                    return True
        return False
    
    # optimal - hashtable 
    # t/c: O(n), s/c: O(n)
    def containsDuplicate2(self, nums: List[int]) -> bool:
        hashtable = {}
        for num in nums:
            if num not in hashtable:
                hashtable[num] = 1
            else:
                return True
        return False

    # optimal - sorting
    # t/c: O(n logn), s/c: O(1)
    def containsDuplicate3(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    
    