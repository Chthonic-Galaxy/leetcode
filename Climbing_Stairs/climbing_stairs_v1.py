def climb_stairs_recursive(n: int):
    if 0 < n <= 2:
        return n
    return climb_stairs_recursive(n-1) + climb_stairs_recursive(n-2)

print(climb_stairs_recursive(1))
print(climb_stairs_recursive(2))
print(climb_stairs_recursive(3))
print(climb_stairs_recursive(4))
print(climb_stairs_recursive(15))
print(climb_stairs_recursive(25))
print(climb_stairs_recursive(35))
print(climb_stairs_recursive(45))
