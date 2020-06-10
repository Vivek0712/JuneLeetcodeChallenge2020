class Solution:
    def searchInsert(self,nums, target):

        left = 0
        right = len(nums)-1

        while left<=right:

            mid = (left+right)//2

            if target==nums[mid]:
                return mid

            
            elif right-left<=1:

                
                if target>=nums[left] and target<=nums[right]:
                    return left+1

                
                elif target>nums[right]:
                    return right+1

                elif target<nums[left]:
                    return left

            elif target>nums[mid]:
                left = mid+1
            elif target<nums[mid]:
                right = mid-1

        return -1