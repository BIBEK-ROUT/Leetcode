class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def calculate(start1, dur1, start2, dur2):
            first_end = min(s + d for s, d in zip(start1, dur1))
            ans = float("inf")

            for s, d in zip(start2, dur2):
                ans = min(ans, max(first_end, s) + d)

            return ans
        land_first = calculate(landStartTime, landDuration, waterStartTime, waterDuration)
        water_first = calculate(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(land_first, water_first)