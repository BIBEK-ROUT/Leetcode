from bisect import bisect_left

class Solution(object):
    def maxDistance(self, side, points, k):
        def conv(x, y):
            if x == 0:
                return y
            elif y == side:
                return side + x
            elif x == side:
                return 2 * side + (side - y)
            else:
                return 3 * side + (side - x)

        arr = sorted(conv(x, y) for x, y in points)
        n = len(arr)
        perimeter = 4 * side

        arr = arr + [x + perimeter for x in arr]

        def check(d):
            for i in range(n):
                count = 1
                first = arr[i]
                last = arr[i]
                idx = i

                while count < k:
                    nxt = bisect_left(arr, last + d, idx + 1, i + n)

                    if nxt >= i + n:
                        break

                    last = arr[nxt]
                    idx = nxt
                    count += 1

                if count == k and first + perimeter - last >= d:
                    return True

            return False

        low = 0
        high = perimeter
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans