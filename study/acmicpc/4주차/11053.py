# 11053
# 가장 긴 증가하는 부분수열

n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
  for j in range(0, i):
    if nums[j] < nums[i]:
      dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))