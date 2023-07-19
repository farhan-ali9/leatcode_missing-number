#first solution

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)  # Store the length of the input list
        expected_sum = (n * (n + 1)) // 2  # Calculate the sum of a consecutive sequence from 0 to n
        actual_sum = sum(nums)  # Calculate the sum of the elements in the input list
        return expected_sum - actual_sum

second solution

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        for i in range(len(nums)):#len(2) #0#1#2
            result=result+(nums[i]-i) #0+(3-0)=3 #3+(0-1)=2
        return result
