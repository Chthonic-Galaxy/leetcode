def climb_stairs_dp(n: int):
    if 0 < n <= 2:
        return n
    
    dp = [0] * (n)
    dp[0] = 1
    dp[1] = 2
    
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n-1]


print(climb_stairs_dp(1))
print(climb_stairs_dp(2))
print(climb_stairs_dp(3))
print(climb_stairs_dp(4))
print(climb_stairs_dp(15))
print(climb_stairs_dp(25))
print(climb_stairs_dp(35))
print(climb_stairs_dp(45))

print(climb_stairs_dp(2**20))
