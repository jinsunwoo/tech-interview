from typing import List

class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool:
        # brute force
        # t/c: O(n^2), s/c: O(1)
        for i in range(len(nums)-1): 
            for j in range(i+1, len(nums)): 
                if nums[i] == nums[j]:
                    return True
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        # optimal - hashtable 
        # t/c: O(n), s/c: O(n)
        hashtable = {}
        for num in nums:
            if num not in hashtable:
                hashtable[num] = 1
            else:
                return True
        return False

    def containsDuplicate3(self, nums: List[int]) -> bool:
        # optimal - sorting
        # t/c: O(n logn), s/c: O(1)
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    
    