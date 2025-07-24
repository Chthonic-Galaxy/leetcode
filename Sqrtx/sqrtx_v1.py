# O N
def my_sqrt_linear(x: int) -> int:
    i = 1
    while i * i <= x:
        i += 1
    return i - 1

if __name__ == "__main__":
    print(my_sqrt_linear(2))
    print(my_sqrt_linear(8))
    print(str(2**81))
    print(str(2**81).__len__())
    print(my_sqrt_linear(2**81))
