class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums = (nums1 + nums2)
        nums.sort()

        aux = int(len(nums)/2)

        if len(nums)%2 == 0:

            return ((nums[aux-1] + nums[aux])/2)

        else:
            return (nums[aux])
