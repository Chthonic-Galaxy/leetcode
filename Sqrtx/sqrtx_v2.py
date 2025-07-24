# O log(N)
def my_sqrt_binary_search(x: int) -> int:
    if x < 2:
        return x
    
    left, right = 0, x // 2 # Root cannot be bigger than x/2 for x >= 2

    ans = 0
    while left <= right:
        mid = left + (right - left) // 2

        mid_squared = mid * mid

        if mid_squared == x:
            return mid
        elif mid_squared > x:
            right = mid - 1
        else:
            ans = mid
            left = mid + 1
    return ans


if __name__ == "__main__":
    print(my_sqrt_binary_search(2))
    print(my_sqrt_binary_search(8))
    # print(str(2**14284))
    # print(str(2**14284).__len__())
    print(my_sqrt_binary_search(2**14284))
