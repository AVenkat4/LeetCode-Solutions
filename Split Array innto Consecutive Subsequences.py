class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        left = collections.Counter(nums)
        end = collections.Counter()
        
        for i in nums:
            if not left[i]:
                continue
            left[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            elif left[i+1] and left[i+2]:
                end[i+2] += 1
                left[i+1] -= 1
                left[i+2] -= 1
            else:
                return False
            
        return True
            