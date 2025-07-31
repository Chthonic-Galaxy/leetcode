cache = {}
def climb_stairs_cached(n:int):
    if n in cache:
        return cache[n]
    if 0 < n <= 2:
        return n
    
    result = climb_stairs_cached(n-1) + climb_stairs_cached(n-2)
    cache[n] = result
    return result

print(climb_stairs_cached(1))
print(climb_stairs_cached(2))
print(climb_stairs_cached(3))
print(climb_stairs_cached(4))
print(climb_stairs_cached(15))
print(climb_stairs_cached(25))
print(climb_stairs_cached(35))
print(climb_stairs_cached(45))
