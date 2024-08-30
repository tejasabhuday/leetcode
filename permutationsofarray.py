class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(cur):
            if len(nums) == len(cur):
                res.append(cur.copy())
                return
            for j in nums:
                if j not in cur:
                    cur.append(j)
                    dfs(cur)
                    cur.pop()
        dfs([])
        return res