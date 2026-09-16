class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        freq = {}

        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # Put numbers into buckets according to frequency
        for num, count in freq.items():
            buckets[count].append(num)

        result = []

        # Start from highest frequency
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

        return result