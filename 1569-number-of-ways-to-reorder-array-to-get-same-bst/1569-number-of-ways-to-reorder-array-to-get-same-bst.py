class Solution(object):
    def numOfWays(self, nums):
        n = len(nums)
        mod = 10**9 + 7

        table = []

        for i in range(n + 1):
            row = []
            for j in range(n + 1):
                row.append(0)
            table.append(row)

        for i in range(n + 1):
            table[i][0] = 1
            table[i][i] = 1

            for j in range(1, i):
                table[i][j] = (
                    table[i - 1][j - 1] + table[i - 1][j]
                ) % mod

        def countWays(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = []
            right = []

            for i in range(1, len(arr)):
                if arr[i] < root:
                    left.append(arr[i])
                else:
                    right.append(arr[i])

            leftSize = len(left)
            rightSize = len(right)

            ways = table[leftSize + rightSize][leftSize]

            leftWays = countWays(left)
            rightWays = countWays(right)

            ways = ways * leftWays % mod
            ways = ways * rightWays % mod

            return ways

        answer = countWays(nums) - 1
        return answer % mod