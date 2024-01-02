class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        s1={x for x in nums1}
        s2={y for y in nums2}

        l1=[x for x in s1 if x not in s2]
        l2=[y for y in s2 if y not in s1]

        return [l1,l2]