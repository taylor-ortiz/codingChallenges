class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        mrgeArr = nums1 + nums2
        mrgeArr.sort()
        if len(mrgeArr) % 2 == 0:
            el1 = int(len(mrgeArr) / 2)
            el2 = int((len(mrgeArr) / 2) - 1)
            
            return float(str((mrgeArr[el1] + mrgeArr[el2]) / 2))
        else:
            el1 = int(floor(len(mrgeArr) / 2))
            return float(str(mrgeArr[el1]))
        
