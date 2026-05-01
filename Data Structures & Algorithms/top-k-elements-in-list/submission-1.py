class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        ans = []
        sort_freq = dict(sorted(freq.items(), key=lambda item: item[1],reverse=True)) 
        count = 0
        for key in sort_freq.keys():
            ans.append(key)
            count+=1
            if count==k:
                break       

        return ans