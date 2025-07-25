# O log(log(N))
def my_sqrt_newton(x: int) -> int:
    if x == 0:
        return 0
    r = x
    while r * r > x:
        r = (r + x // r) // 2
    return r

if __name__ == "__main__":
    print(my_sqrt_newton(2))
    print(my_sqrt_newton(8))
    print(str(2**14284))
    print(str(2**14284).__len__())
    print(my_sqrt_newton(2**14284))