class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        freq = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                freq[nums1[i]+nums2[j]]= freq.get(nums1[i]+nums2[j],0)+1

        count = 0
        for k in range(len(nums3)):
            for l in range(len(nums4)):
                val = nums3[k]+nums4[l]
                if -val in freq:
                    count += freq[-val]
            
        return count