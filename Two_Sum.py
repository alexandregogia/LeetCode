class Solution():
    def twoSum(self, nums, target):
        n = len(nums)

        for i in range(n):
            if not -10**9 <= nums[i] <= 10**9:
                    raise ValueError("Invalid input")

        if not 2 <= n <= 10**4:
            raise ValueError("Invalid input")

        if not -10**9 <= target <= 10**9:
            raise ValueError("Invalid input")

        x = {}

        for i in range(n):
            current = nums[i]
            snd = target - current
            if snd in x:
                return (x[snd], i)
                break
            x[current] = i

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
      