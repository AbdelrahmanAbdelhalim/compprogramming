import math
from math import sqrt

# My original solution. Passes the tests just fine. Extra memory is needed however
def perfect_squares(n: int) -> int:
    sq = []
    for i in range(int(sqrt(n)) + 1):
        if i*i > n:
            break
        sq.append(i*i)
        
    dp = [math.inf for i in range(n + 1)]
    dp[0] = 0
    for i in range(n + 1):
          for s in sq:
              if s + i < len(dp):
                  dp[i + s] = min(dp[i] + 1, dp[i + s])
    return dp[-1]

# My modified solution with optimized memory. Iterate over the perfect squares without storing them
import math
from math import sqrt
def perfect_squares(n: int) -> int:
    dp = [math.inf for i in range(n + 1)]
    dp[0] = 0
    for i in range(n + 1):
          s = 1
          while s*s <= n:
              cur = s*s
              if cur + i < len(dp):
                  dp[i + cur] = min(dp[i] + 1, dp[i + cur])
              s += 1
    return dp[-1]
