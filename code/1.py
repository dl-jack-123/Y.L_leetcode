class Solution:
	"""
	
	
	Given an array of integers, return indices of the two numbers such that they add up to a specific target.

	You may assume that each input would have exactly one solution, and you may not use the same element twice.

	Example:

	Given nums = [2, 7, 11, 15], target = 9,

	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].
	"""
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
		
		---syntax---
		dict.__contains__ is True / False assignment. 找尋dict裡的key , 有=True , 沒有=False
		
		
		---解說---
		一般人第一眼的想法會用2個for來去辦別，
		但這裡使用一個for迴圈解出來，需要想一下才知道key point
		
		list[ A , B , C,D] = Target
		A+B = Target
		Target-A = B # 運用這個邏輯
		
		範例給的是從小排序，故B>A
		for 迴圈由左至右(排序完是由小至大)，所以我們要找B , 如果沒有B就append dict , 如果找到就return A,B
		
		
        """
        dictionary = {}
        for key, A in enumerate(nums):
            B = target - A
            if dictionary.__contains__(B):
                return [dictionary.get(B), key]
            dictionary[A] = key