class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            value = 1
            for x in range(len(nums)):
                if i == x:
                    continue
                else:
                    value = value * nums[x]
        
            res.append(value)
        return res