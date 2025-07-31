def climb_stairs_dp_mem_optimized(n: int):
    if 0 < n <= 2:
        return n
    
    a, b = 1, 2
    for i in range(2, n+1):
        a, b = b, + a + b
    
    return b


print(climb_stairs_dp_mem_optimized(1))
print(climb_stairs_dp_mem_optimized(2))
print(climb_stairs_dp_mem_optimized(3))
print(climb_stairs_dp_mem_optimized(4))
print(climb_stairs_dp_mem_optimized(15))
print(climb_stairs_dp_mem_optimized(25))
print(climb_stairs_dp_mem_optimized(35))
print(climb_stairs_dp_mem_optimized(45))
print(climb_stairs_dp_mem_optimized(20000))

# print(climb_stairs_dp_mem_optimized(2**20))
